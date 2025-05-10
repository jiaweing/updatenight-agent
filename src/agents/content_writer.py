import hashlib
from crewai import Agent
from typing import List, Dict
import os
import time
import urllib.parse
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from src.utils.model_provider import ModelProvider
from src.utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('ContentWriter')

class ContentWriterAgent:
    def __init__(self, samples_dir: str = "samples", content_dir: str = "content"):
        logger.info("🤖 Initializing ContentWriterAgent")
        self.agent = Agent(
            role='Content Writer',
            goal='Write informative newsletter content in Update Night style',
            backstory="""You are a specialized agent that analyzes content and writes
            engaging summaries in the style of Update Night newsletter. You understand
            technical concepts and can highlight key insights while maintaining a
            consistent tone and format."""
        )
        self.samples_dir = samples_dir
        self.content_dir = content_dir
        self.style_examples = self.load_style_examples()
        self._category_data = None  # Initialize category data cache
        self.links_file = "links.md"  # Default links file
        logger.info(f"📚 Loaded {len(self.style_examples)} style examples")

    def load_style_examples(self) -> List[str]:
        """Load and parse writing style examples from samples directory"""
        logger.debug(f"📖 Loading style examples from {self.samples_dir}")
        examples = []
        if not os.path.exists(self.samples_dir):
            logger.warning(f"⚠️ Samples directory not found: {self.samples_dir}")
            return examples

        for file in os.listdir(self.samples_dir):
            if file.endswith('.md'):
                logger.debug(f"📄 Loading style example: {file}")
                with open(os.path.join(self.samples_dir, file), 'r', encoding='utf-8') as f:
                    examples.append(f.read())
        return examples

    def generate_newsletter_intro(self, articles: List[Dict]) -> str:
        """Generate engaging title, description and intro based on article content"""
        logger.debug("🎨 Generating newsletter intro")

        llm = ModelProvider.get_model()
        prompt = PromptTemplate(
            input_variables=["articles", "style_examples"],
            template="""Write an engaging newsletter intro about these topics:

{articles}

Write two parts:

1. Title (2-5 words):
- Make it viral and eye-catching
- Focus on most shocking/surprising aspect
- Make readers think "Wait, what? How is that possible?"
- Must be true to content (not clickbait)
Examples:
- Write PHP in React
- You can now play DOOM in a PDF
- AI Writes Better Tests

2. Newsletter Intro:
- Begin with "Let's talk about..." and list 3-4 most exciting topics
- Follow with 2-3 sentences welcoming readers
- Use conversational tone and show enthusiasm
- Add a rhetorical question to engage readers

Example:
Let's talk about the new memory model in Rust, breakthrough error handling in quantum computing, and some fascinating hidden projects in systems programming.

Welcome back to another mind-bending week in tech! We've uncovered some incredible developments that are reshaping how we think about programming. Ready to dive into these game-changing updates?

IMPORTANT:
- Keep it casual but informative
- No special formatting or quotes
- Focus on the excitement and impact"""
        )

        # Extract summaries and titles for context
        article_briefs = []
        for article in articles:
            article_briefs.append(f"- {article.get('title', '')}")

        result = llm.invoke(
            prompt.format(
                articles="\n".join(article_briefs),
                style_examples="\n---\n".join(self.style_examples[:2])
            )
        ).content.strip()

        # Find and split sections
        lines = result.strip().split("\n")

        # Get the title (first non-empty line)
        title = next((line for line in lines if line.strip()), "Tech Updates")

        # Find first "Let's talk about" line for subheadline
        subheadline = next((line for line in lines if line.strip().startswith("Let's talk about")),
                          "Let's talk about the latest in tech and some really cool hidden projects")

        # Get remaining text after subheadline for intro
        intro_start = next((i for i, line in enumerate(lines) if line.strip() == subheadline), 0) + 1
        intro_text = [" ".join(line.strip() for line in lines[intro_start:] if line.strip())]

        # Clean all text
        clean_title = self._clean_text(title)
        clean_subheadline = self._clean_text(subheadline)
        clean_text = [self._clean_text(t) for t in intro_text]

        # Format the complete intro section with minimal formatting
        # Add podcast link with UTM parameters
        podcast_link = self._add_utm_params("https://updatenight.com/podcast")
        intro_section = f"""# {clean_title}

{clean_subheadline}

{"\n\n".join(clean_text)}

---

Wanna listen to the podcast instead and follow along?

[link]({podcast_link})

---

"""
        return self._clean_text(intro_section)

    def _generate_title_and_summary_with_link(self, content: str, url: str) -> tuple[str, str]:
        """Special version of content generation that emphasizes link requirement"""
        logger.debug("🔄 Regenerating content with emphasis on link requirement")

        # Split content into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(content)

        # Use a more focused prompt that heavily emphasizes the link requirement
        prompt = PromptTemplate(
            input_variables=["content"],
            template="""Write a title and summary with a mandatory embedded link marker:

CRITICAL LINK REQUIREMENTS:
For regular articles (non-YouTube):
- You MUST embed exactly one [[LINK_TEXT]] marker in your summary
- The link text must be a natural part of the sentence
- NEVER use phrases like "click here", "read more", "check it out", etc.
- Link text should be 3-7 words that capture the most interesting aspect
- Place link early in the content (first or second paragraph)

For YouTube videos:
- Do NOT embed any link markers in the content
- Do NOT use [[ ]] markers anywhere in the content
- Just write engaging, natural text without any special markup

Content to summarize:
{content}

Format:
1. Title (2-5 words, shocking/surprising aspect)
2. Summary that:
   - Naturally integrates the link
   - Uses engaging, conversational tone
   - Balances technical accuracy with accessibility
   - Keeps paragraphs focused (1-3 sentences)

Examples for regular articles:
✅ [[The new memory model in Rust]] is revolutionizing how we think about systems programming.
✅ What started as a small experiment has grown into [[a game-changing approach to neural networks]].
✅ Developers are excited about [[these breakthrough improvements in TypeScript 5.4]].

Bad examples for regular articles:
❌ Click here to [[learn more about the update]]
❌ [[Read the full details]] about this development
❌ You can [[explore the documentation here]]

Example for YouTube content:
✅ This game-changing demo shows how they achieved incredible performance with their innovative approach.
[rest of summary]"""
        )

        llm = ModelProvider.get_model()
        result = llm.invoke(
            prompt.format(content="\n".join(chunks))
        )

        parts = result.content.strip().split('\n\n', 1)
        if len(parts) == 2:
            title = parts[0].strip().strip('"').replace('"', '').strip()
            summary = parts[1].strip()
        else:
            raise ValueError("Failed to generate properly formatted content with link marker")

        return self._clean_text(title), self._clean_text(summary)

    def _generate_title_and_summary(self, content: str, url: str) -> tuple[str, str]:
        """Generate an engaging title and summary based on article content"""
        start_time = time.time()
        logger.debug("🎯 Starting title and summary generation")

        # Split content into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(content)
        logger.debug(f"📦 Split content into {len(chunks)} chunks")

        # Create combined prompt template for title and summary
        prompt = PromptTemplate(
            input_variables=["content", "style_examples", "url"],
            template="""Based on this content:

{content}

1. Write a viral, eye-catching title (2-5 words) that:
- Focuses on the most shocking/surprising aspect
- Makes readers think "Wait, what? How is that possible?"
- Is true to the content (not clickbait)
- NO bold formatting, NO asterisks, NO special characters
Examples:
- "Write PHP in React" (about React's new PHP support)
- "You can now play DOOM in a PDF" (about PDF gaming capabilities)
- "AI Writes Better Tests" (about AI-powered testing)

2. Write a summary that balances technical depth with accessibility:

CRITICAL LINK REQUIREMENTS:
For regular articles (non-YouTube):
- You MUST embed exactly one [[LINK_TEXT]] marker in your summary
- The link text must be a natural part of the sentence
- NEVER use phrases like "click here", "read more", "check it out", etc.
- Link text should be 3-7 words that capture the most interesting aspect
- Place link early in the content (first or second paragraph)

For YouTube videos:
- Do NOT embed any link markers in the content
- Do NOT use [[ ]] markers anywhere in the content
- Just write engaging, natural text without any special markup

Examples for regular articles:
✅ [[The new memory model in Rust]] is revolutionizing how we think about systems programming.
✅ What started as a small experiment has grown into [[a game-changing approach to neural networks]].
✅ Developers are excited about [[these breakthrough improvements in TypeScript 5.4]].

Bad examples for regular articles:
❌ Click here to [[learn more about the update]]
❌ [[Read the full details]] about this development
❌ You can [[explore the documentation here]]

Example for YouTube content:
✅ This game-changing demo shows how they achieved incredible performance with their innovative approach.

WRITING REQUIREMENTS:
- Start with an engaging hook that includes the link naturally
- Keep technical terms but explain them clearly
- Use analogies and real-world comparisons
- Show genuine excitement and personal insights
- Balance technical details with accessibility
- Keep paragraphs focused (2-3 sentences max)

Example:
[[Rust just got a game-changing memory model upgrade]] that's making waves in systems programming. Remember how careful you had to be with pointers? Those days might be numbered.

The headline feature is what they're calling "Partial Borrowing" - think of it like being able to lend different parts of your Swiss Army knife to different friends at the same time, instead of having to hand over the whole thing.

For the systems programmers: It introduces fine-grained field-level borrowing with lifetime inference, supporting disjoint mutable access to struct fields. The borrow checker now understands field-level independence, eliminating many common ownership headaches.

The compiler's new polonius-based analysis is so smart it can track individual field accesses across async boundaries and closures. Even better, it maintains full backward compatibility with existing code.

Testing this on our production service cut memory usage by 30% and caught three potential race conditions we didn't even know about. Rust just took another big step toward making memory safety the default, not the exception.

Return the title on first line, then blank line, then summary with the link marker. Make sure to separate paragraphs with blank lines."""
        )

        logger.debug("🤔 Generating title and summary using AI model")
        # Use AI model to generate title and summary
        llm = ModelProvider.get_model()
        result = llm.invoke(
            prompt.format(
                content="\n".join(chunks),
                style_examples="\n---\n".join(self.style_examples[:2])
            )
        )

        # Parse response to extract title and summary
        parts = result.content.strip().split('\n\n', 1)
        if len(parts) == 2:
            title = parts[0].strip().strip('"').replace('"', '').strip()  # Remove quotes
            summary = parts[1].strip()
        else:
            title = ""
            summary = ""

        if not title or not summary:
            logger.warning("⚠️ Failed to parse title or summary from LLM response")
            title = title or "Technical Update"
            summary = summary or content[:200] + "..."

        processing_time = time.time() - start_time
        logger.info(f"✨ Generated title and summary in {processing_time:.2f}s")
        return self._clean_text(title), self._clean_text(summary)

    def create_section(self, article_data: Dict) -> str:
        """
        Create a newsletter section for a single article

        Args:
            article_data (Dict): Dictionary containing article content and metadata

        Returns:
            str: Formatted markdown section
        """
        logger.debug(f"✍️ Creating section for article: {article_data.get('url')}")

        # Extract key information
        url = article_data.get('url', '')
        content = article_data.get('content', '')
        screenshot_path = article_data.get('screenshot_path', '')

        # Generate title and summary using LLM
        title, summary = self._generate_title_and_summary(content, url)

        # Build section components
        clean_title = title.strip('"').replace('"', '').strip().strip('*').strip('#')
        section_parts = [f"\n### {clean_title}\n"]

        # Get screenshot path if available and not a YouTube link
        screenshot_block = ""
        if screenshot_path and not ('youtube.com' in url or 'youtu.be' in url):
            rel_path = os.path.relpath(
                screenshot_path,
                os.path.dirname(self.output_file)
            )
            logger.debug(f"🖼️ Using screenshot at relative path: {rel_path}")
            screenshot_block = f"\n![Screenshot]({rel_path})\n"

        import random

        # Add UTM parameters to the URL
        url_with_utm = self._add_utm_params(url)

        # For YouTube links
        if 'youtube.com' in url or 'youtu.be' in url:
            youtube_block = f"\n{url_with_utm}\n"
            content_block = f"\n{summary}\n"

            # Randomly place YouTube link at start or end
            if random.choice([True, False]):
                if screenshot_block:
                    section_parts.extend([youtube_block, screenshot_block, content_block])
                else:
                    section_parts.extend([youtube_block, content_block])
            else:
                if screenshot_block:
                    section_parts.extend([screenshot_block, content_block, youtube_block])
                else:
                    section_parts.extend([content_block, youtube_block])
        else:
            # For non-YouTube links
            # Check if the LLM has marked a link text with [[LINK_TEXT]]
            import re
            link_match = re.search(r'\[\[(.*?)\]\]', summary)

            attempts = 0
            max_attempts = 3
            while attempts < max_attempts:
                if link_match:
                    # Extract the link text and replace the markers with actual link
                    link_text = link_match.group(1)
                    content_block = f"\n{summary.replace(f'[[{link_text}]]', f'[{link_text}]({url_with_utm})')}\n"
                    break
                else:
                    # No link marker found, regenerate content with stronger emphasis on link requirement
                    logger.debug(f"No link marker found in attempt {attempts + 1}, regenerating content")
                    title, summary = self._generate_title_and_summary_with_link(content, url)
                    link_match = re.search(r'\[\[(.*?)\]\]', summary)
                    attempts += 1

            if not link_match:
                # If still no link after max attempts, something is wrong with the LLM
                logger.error("Failed to generate content with embedded link after multiple attempts")
                raise ValueError("Content generation failed: No link marker found in summary")

            # For non-YouTube content, randomly place screenshot
            if screenshot_block:
                if random.choice([True, False]):
                    section_parts.extend([screenshot_block, content_block])
                else:
                    section_parts.extend([content_block, screenshot_block])
            else:
                section_parts.extend([content_block])

        section = "".join(section_parts)
        return self._clean_text(section)

    def _load_article_content(self, url: str) -> Dict:
        """
        Load article content and metadata from content directory

        Args:
            url (str): Article URL to load content for

        Returns:
            Dict: Article data including content and metadata
        """
        logger.debug(f"📥 Loading content for URL: {url}")
        link_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()[:16]

        article_data = {'url': url}

        # Load content file
        content_path = os.path.join(self.content_dir, f"{link_hash}_content.txt")
        if os.path.exists(content_path):
            logger.debug(f"📄 Found content file: {content_path}")
            with open(content_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Skip metadata lines and separator
                content_start = 4  # Skip URL, title, and separator lines
                article_data['content'] = self._clean_text(''.join(lines[content_start:]))
                # Extract title from content file
                for line in lines[:2]:
                    if line.startswith('Title: '):
                        article_data['title'] = line[7:].strip()
                        break
        else:
            logger.warning(f"⚠️ Content file not found: {content_path}")

        # Add screenshot path if exists
        screenshot_path = os.path.join(self.content_dir, f"{link_hash}.png")
        if os.path.exists(screenshot_path):
            logger.debug(f"🖼️ Found screenshot: {screenshot_path}")
            article_data['screenshot_path'] = screenshot_path
        else:
            logger.warning(f"⚠️ Screenshot not found: {screenshot_path}")

        return article_data

    def collect_batch_articles(self, urls: List[str]) -> List[Dict]:
        """Collect article data for a batch of URLs"""
        articles = []
        for idx, url in enumerate(urls, 1):
            logger.info(f"[{idx}/{len(urls)}] 📥 Loading content")
            article_data = self._load_article_content(url)
            if article_data.get('content'):
                articles.append(article_data)
            else:
                logger.warning(f"[{idx}/{len(urls)}] ⚠️ No content found for URL: {url}")
        return articles

    def _add_utm_params(self, url: str) -> str:
        """Add UTM parameters to a URL

        Args:
            url (str): Original URL

        Returns:
            str: URL with UTM parameters added
        """
        try:
            # Parse the URL
            parsed_url = urllib.parse.urlparse(url)

            # Get existing query parameters
            query_params = dict(urllib.parse.parse_qsl(parsed_url.query))

            # Add UTM parameters
            utm_params = {
                'utm_source': 'updatenight.com',
                'utm_medium': 'newsletter',
                'utm_campaign': 'weekly_update',
                'utm_content': 'article_link'
            }

            # Update query parameters
            query_params.update(utm_params)

            # Build new query string
            new_query = urllib.parse.urlencode(query_params)

            # Reconstruct the URL
            new_url = urllib.parse.urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))

            logger.debug(f"🔗 Added UTM parameters to URL: {new_url}")
            return new_url
        except Exception as e:
            logger.error(f"Error adding UTM parameters to URL: {str(e)}")
            return url  # Return original URL if there's an error

    def _clean_text(self, text: str) -> str:
        """Clean text by fixing encoding issues and special characters"""
        try:
            # Handle common encoding issues
            text = text.encode('ascii', 'ignore').decode('ascii')

            # Replace problematic characters
            replacements = {
                '�': "'",  # Replace replacement char with apostrophe
                '"': '"',  # Replace opening curly quote
                '"': '"',  # Replace closing curly quote
                ''': "'",  # Replace opening curly apostrophe
                ''': "'",  # Replace closing curly apostrophe
                '—': '-',  # Replace em dash
                '–': '-',  # Replace en dash
                '…': '...', # Replace ellipsis
                '\u00A0': ' ',  # Replace non-breaking space
                '\u2019': "'",  # Replace right single quotation mark
                '\u2018': "'",  # Replace left single quotation mark
                '\u201C': '"',  # Replace left double quotation mark
                '\u201D': '"',  # Replace right double quotation mark
            }
            for old, new in replacements.items():
                text = text.replace(old, new)

            # Remove any remaining non-ASCII characters
            text = ''.join(char for char in text if 32 <= ord(char) <= 126 or char in '\n\r\t')

            return text.strip()
        except Exception as e:
            logger.error(f"Error cleaning text: {str(e)}")
            return text.strip()

    def write_category_headers(self, categories: List[str]):
        """Write category headers in order from links.md"""
        with open(self.output_file, 'a') as f:
            for category in categories:
                f.write(f"\n# {category}\n\n")

    def process_batch(self, category: str, urls: List[str]):
        """
        Process a batch of articles for a specific category

        Args:
            category (str): Category name from links.md
            urls (List[str]): List of article URLs in this category
        """
        logger.info(f"🔄 Processing batch for category: {category}")
        articles = self.collect_batch_articles(urls)
        logger.info(f"📊 Found content for {len(articles)} out of {len(urls)} URLs")

        # Process each article in the category
        for idx, article in enumerate(articles, 1):
            try:
                start_time = time.time()
                section = self.create_section(article)

                # Find where to insert this section
                with open(self.output_file, 'r') as f:
                    content = f.read()

                # Find the category header position
                category_pos = content.find(f"\n# {category}\n")
                if category_pos != -1:
                    # Get next category position
                    next_category_pos = float('inf')

                    # Use cached categories from initialization
                    if self._category_data is None:
                        self._category_data = self.parse_links_md()
                    next_categories = list(self._category_data.keys())
                    current_idx = next_categories.index(category)

                    # Only look at categories after current one
                    if current_idx + 1 < len(next_categories):
                        next_category = next_categories[current_idx + 1]
                        pos = content.find(f"\n# {next_category}\n")
                        if pos != -1:
                            next_category_pos = pos

                # Insert before next category or at EOF
                insert_pos = next_category_pos if next_category_pos != float('inf') else len(content)
                content = content[:insert_pos] + section + "\n\n" + content[insert_pos:]

                # Write back to file
                with open(self.output_file, 'w') as f:
                    f.write(content)

                processing_time = time.time() - start_time
                logger.info(f"[{idx}/{len(articles)}] ✅ Generated section for {article.get('url')} in {processing_time:.2f}s")
            except Exception as e:
                logger.error(f"❌ Error processing article {article.get('url')}: {str(e)}", exc_info=True)

    def parse_links_md(self, force_reload: bool = False) -> Dict[str, List[str]]:
        """
        Parse links.md to get categories and their URLs

        Args:
            force_reload (bool): Force reload from file even if cached

        Returns:
            Dict[str, List[str]]: Map of categories to their URLs
        """
        # Return cached data if available
        if self._category_data is not None and not force_reload:
            return self._category_data

        logger.info(f"📖 Reading {self.links_file}")
        categories = {}
        current_category = None

        try:
            with open(self.links_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('## '):
                        current_category = line[3:].strip()
                        categories[current_category] = []
                    elif line.startswith('- [') and current_category:
                        try:
                            url = line.split('](')[1].split(')')[0].strip()
                            if url:  # Only add non-empty URLs
                                categories[current_category].append(url)
                        except IndexError:
                            continue

            # Cache the categories
            self._category_data = categories

            logger.info(f"📊 Found {len(categories)} categories")
            for category, urls in categories.items():
                logger.info(f"  - {category}: {len(urls)} URLs")
            return self._category_data

        except FileNotFoundError:
            logger.error("❌ links.md not found")
            raise FileNotFoundError("links.md not found")

    def create_newsletter(self, output_file: str = "newsletter.md") -> str:
        """
        Create complete newsletter by reading categories and URLs from links.md

        Args:
            output_file (str): Path to save the newsletter

        Returns:
            str: Path to generated newsletter file
        """
        # Parse links.md to get categorized URLs
        categorized_urls = self.parse_links_md()
        total_urls = sum(len(urls) for urls in categorized_urls.values())
        logger.info(f"📰 Starting newsletter creation with {total_urls} URLs")
        start_time = time.time()

        self.output_file = output_file

        # Initialize newsletter file with header
        logger.info(f"📝 Initializing newsletter at {output_file}")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Generate title and intro by looking at all articles first
        logger.info("🎨 Generating newsletter intro")

        # Collect all articles from all categories
        all_urls = []
        for category_urls in categorized_urls.values():
            all_urls.extend(category_urls)

        all_articles = self.collect_batch_articles(all_urls)
        intro_content = self.generate_newsletter_intro(all_articles)

        # Write initial content
        with open(output_file, 'w') as f:
            f.write(intro_content)

        # Process each category in order
        categories = list(categorized_urls.keys())
        total_categories = len(categories)

        # Write category headers using order from links.md
        self.write_category_headers(categories)

        # Process each category's content
        for idx, category in enumerate(categories, 1):
            urls = categorized_urls[category]
            if urls:  # Skip if no URLs in category
                logger.info(f"[{idx}/{total_categories}] 🔄 Processing category: {category}")
                batch_start = time.time()
                self.process_batch(category, urls)
                batch_time = time.time() - batch_start
                logger.info(f"[{idx}/{total_categories}] ✅ Completed category in {batch_time:.2f}s")
            else:
                logger.warning(f"[{idx}/{total_categories}] ⚠️ Skipping empty category: {category}")

        total_time = time.time() - start_time
        logger.info(f"🎉 Newsletter creation completed in {total_time:.2f}s")
        return output_file
