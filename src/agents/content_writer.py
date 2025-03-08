import hashlib
from crewai import Agent
from typing import List, Dict
import os
import time
from datetime import datetime
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
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
        
        llm = ChatOpenAI(model_name="gpt-4o-mini")
        prompt = PromptTemplate(
            input_variables=["articles", "style_examples"],
            template="""Write three sections about these topics:

{articles}

First section: Create a viral, eye-catching title (2-5 words) that:
- Focuses on the most shocking/surprising aspect
- Makes readers think "Wait, what? How is that possible?"
- Is true to the content (not clickbait)
- Avoids quotes and special formatting
Examples:
- Write PHP in React (about React's new PHP support)
- You can now play DOOM in a PDF (about PDF gaming capabilities)
- AI Writes Better Tests (about AI-powered testing)

Second section: Key topics intro
Format: "Let's talk X, Y, Z, and some really cool hidden projects"
where X, Y, Z are the most interesting topics from the articles

Third section: Brief welcome message (2-3 sentences) that:
- Uses a conversational tone
- Includes personal commentary or opinion
- Engages readers with rhetorical questions
- Maintains a balance between technical depth and accessibility
Example:
Time flies in tech! Welcome back to Update Night, we've got some amazing developments to share that will blow your mind. Are you ready for what's coming next? Let me know what you think!

Important:
- Make title surprising but true to the content
- Avoid quotes and special formatting
- Use plain text only"""
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
        
        # Split the response into sections
        sections = result.strip().split("\n\n")
        if len(sections) < 3:
            logger.warning("⚠️ Generated intro is incomplete, using fallback")
            title = "Tech Updates"
            subheadline = "Let's talk about the latest in tech and some really cool hidden projects"
            intro_text = ["Another exciting week in tech! Welcome back to Update Night, we've got some amazing things to cover that will blow your mind."]
        else:
            title = sections[0].strip()
            subheadline = sections[1].strip()
            # Take the welcome message as is
            intro_text = [sections[2].strip()]
        
        # Remove quotes, asterisks and clean special characters
        clean_title = title.strip('*#"').strip().replace('"', '')
        clean_subheadline = subheadline.strip('*#').strip()
        clean_text = [t.strip('*#').strip() for t in intro_text]

        # Format the complete intro section with minimal formatting
        intro_section = f"""# {clean_title}

### {clean_subheadline}

{datetime.now().strftime('%b %d, %Y')}

{"\n\n".join(clean_text)}

---

Wanna listen to the podcast instead and follow along?

[link]()

---

"""
        return self._clean_text(intro_section)
        
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
            input_variables=["content", "style_examples"],
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

2. Write a technical yet conversational summary (2-3 paragraphs) that:
- Starts with the most impressive metrics/capabilities
- Includes specific benchmarks and improvements
- Explains how it works/why it matters
- Adds personal commentary or opinion where appropriate
- Uses rhetorical questions to engage readers
- Maintains a balance between technical depth and accessibility
- Concludes with a thought-provoking question or insight

Return the title on first line, then blank line, then summary."""
        )
        
        logger.debug("🤔 Generating title and summary using OpenAI")
        # Use OpenAI to generate title and summary
        llm = ChatOpenAI(model_name="gpt-4o-mini")
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
        
        # Get content and link
        clean_summary = summary.strip('*').strip('#')
        content_block = f"\n{clean_summary}\n"
        if 'youtube.com' in url or 'youtu.be' in url:
            link_block = f"\n{url}\n"
        else:
            link_block = f"\n[Read more]({url})\n"
        
        # Randomly place screenshot at start or end
        if screenshot_block:
            import random
            if random.choice([True, False]):
                section_parts.extend([screenshot_block, content_block, link_block])
            else:
                section_parts.extend([content_block, link_block, screenshot_block])
        else:
            section_parts.extend([content_block, link_block])
        
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

    def categorize_articles(self, articles: List[Dict]) -> Dict[str, List[Dict]]:
        """Group articles into categories"""
        llm = ChatOpenAI(model_name="gpt-4o-mini")
        prompt = PromptTemplate(
            input_variables=["articles"],
            template="""Categorize these articles into Update Night sections:
{articles}

Use these categories:
- The Big Picture (major tech announcements and developments)
- Under the Radar (interesting but less mainstream developments)
- TrAIn of Thought (AI developments and insights)
- The Grid (UI/UX and design updates)
- The Spotlight (cool projects and tools)

Return in format:
CATEGORY: [category name]
ARTICLES: [comma-separated list of article numbers, e.g. 1,3,5]
(repeat for each category)"""
        )
        
        # Format articles with numbers
        article_list = []
        for i, article in enumerate(articles, 1):
            article_list.append(f"{i}. {article.get('title', '')}")
            
        result = llm.invoke(
            prompt.format(articles="\n".join(article_list))
        ).content.strip()
        
        # Parse categories
        categories = {}
        current_category = ""
        for line in result.split("\n"):
            if line.startswith("CATEGORY:"):
                current_category = line.replace("CATEGORY:", "").strip()
            elif line.startswith("ARTICLES:"):
                article_nums = line.replace("ARTICLES:", "").strip()
                if article_nums and article_nums.lower() != "none":
                    try:
                        indices = [int(i.strip()) - 1 for i in article_nums.split(",")]
                        categories[current_category] = [articles[i] for i in indices if i < len(articles)]
                    except ValueError:
                        logger.warning(f"Invalid article numbers for category {current_category}: {article_nums}")
                        categories[current_category] = []
                else:
                    logger.warning(f"No articles assigned to category {current_category}")
                    categories[current_category] = []
        
        # Ensure ordered categories
        ordered_categories = {}
        priority_order = [
            "The Big Picture",
            "Under the Radar",
            "TrAIn of Thought",
            "The Grid",
            "The Spotlight",
        ]
        
        # Sort by priority order
        for category in priority_order:
            if category in categories:
                ordered_categories[category] = categories[category]
        
        # Add any remaining categories not in priority list
        for category in categories:
            if category not in ordered_categories:
                ordered_categories[category] = categories[category]
                
        return ordered_categories

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
    
    def write_category_headers(self):
        """Write all category headers once at the start"""
        categories = [
            "The Big Picture",
            "Under the Radar", 
            "TrAIn of Thought",
            "The Grid",
            "The Spotlight",
        ]
        with open(self.output_file, 'a') as f:
            for category in categories:
                f.write(f"\n# {category}\n\n")

    def process_batch(self, urls: List[str]):
        """
        Process a batch of articles and create newsletter sections
        
        Args:
            urls (List[str]): List of article URLs to process
        """
        logger.info(f"🔄 Processing batch of {len(urls)} URLs")
        articles = self.collect_batch_articles(urls)
        logger.info(f"📊 Found content for {len(articles)} out of {len(urls)} URLs")
        
        # Categorize articles
        logger.info("🏷️ Categorizing articles")
        categorized = self.categorize_articles(articles)
        
        # Process articles by category
        for category, category_articles in categorized.items():
            # Process articles in this category
            for current_idx, article in enumerate(category_articles, 1):
                try:
                    start_time = time.time()
                    section = self.create_section(article)
                    # Find where to insert this section
                    with open(self.output_file, 'r') as f:
                        content = f.read()
                    
                    # Find the category header position
                    category_pos = content.find(f"\n# {category}\n")
                    if category_pos != -1:
                        # Find the next category header or EOF
                        next_category_pos = float('inf')
                        for next_category in ["The Big Picture", "Under the Radar", "TrAIn of Thought", "The Grid", "The Spotlight"]:
                            pos = content.find(f"\n# {next_category}\n", category_pos + len(category) + 2)
                            if pos != -1 and pos < next_category_pos:
                                next_category_pos = pos
                        
                        # Insert before next category or at end
                        insert_pos = next_category_pos if next_category_pos != float('inf') else len(content)
                        content = content[:insert_pos] + section + "\n\n" + content[insert_pos:]
                        
                        # Write back to file
                        with open(self.output_file, 'w') as f:
                            f.write(content)
                            
                    processing_time = time.time() - start_time
                    logger.info(f"[{current_idx}/{len(category_articles)}] ✅ Generated section for {article.get('url')} in {processing_time:.2f}s")
                except Exception as e:
                    logger.error(f"❌ Error processing article {article.get('url')}: {str(e)}", exc_info=True)

    def create_newsletter(self, urls: List[str], output_file: str, batch_size: int = 5) -> str:
        """
        Create complete newsletter by processing URLs in batches
        
        Args:
            urls (List[str]): List of article URLs to process
            output_file (str): Path to save the newsletter
            batch_size (int): Number of articles to process in each batch
            
        Returns:
            str: Path to generated newsletter file
        """
        logger.info(f"📰 Starting newsletter creation for {len(urls)} URLs")
        start_time = time.time()
        
        self.output_file = output_file
        
        # Initialize newsletter file with header
        logger.info(f"📝 Initializing newsletter at {output_file}")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Generate title and intro by looking at all articles first
        logger.info("🎨 Generating newsletter intro")
        all_articles = self.collect_batch_articles(urls)
        intro_content = self.generate_newsletter_intro(all_articles)
        
        # Write intro and category headers
        with open(output_file, 'w') as f:
            f.write(intro_content)
        
        # Write category headers once
        self.write_category_headers()
            
        # Process articles in batches
        for i in range(0, len(urls), batch_size):
            batch_num = i//batch_size + 1
            total_batches = (len(urls) + batch_size - 1) // batch_size
            logger.info(f"[{batch_num}/{total_batches}] 🔄 Processing batch")
            
            batch_start = time.time()
            batch_urls = urls[i:i + batch_size]
            self.process_batch(batch_urls)
            batch_time = time.time() - batch_start
            logger.info(f"[{batch_num}/{total_batches}] ✅ Completed batch in {batch_time:.2f}s")
        
        total_time = time.time() - start_time
        logger.info(f"🎉 Newsletter creation completed in {total_time:.2f}s")
        return output_file
