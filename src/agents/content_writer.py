from crewai import Agent
from typing import List, Dict
import os
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
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
        title = article_data.get('title', '')
        url = article_data.get('url', '')
        content = article_data.get('content', '')
        screenshot_path = article_data.get('screenshot_path', '')
        
        # Create relative path for screenshot
        if screenshot_path:
            rel_path = os.path.relpath(
                screenshot_path, 
                os.path.dirname(self.output_file)
            )
            logger.debug(f"🖼️ Using screenshot at relative path: {rel_path}")
        
        # Format markdown section
        section = f"""
## {title}

![Screenshot]({rel_path})

{self._write_summary(content)}

[Read more]({url})
"""
        return section
        
    def _write_summary(self, content: str) -> str:
        """Generate summary with key insights based on content"""
        start_time = time.time()
        logger.debug("🎯 Starting summary generation")
        
        # Split content into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(content)
        logger.debug(f"📦 Split content into {len(chunks)} chunks")
        
        # Create summary prompt template
        prompt = PromptTemplate(
            input_variables=["content", "style_examples"],
            template="""
            You are writing a section for the Update Night newsletter. Using the following content:
            
            {content}
            
            Write a concise summary that highlights:
            1. Key points and announcements
            2. Why it matters for developers/tech industry
            3. Important technical details or impacts
            
            Match the writing style from these examples:
            {style_examples}
            
            Focus on being informative yet engaging, technical yet accessible.
            Keep the summary brief but impactful.
            """
        )
        
        logger.debug("🤔 Generating summary using OpenAI")
        # Use OpenAI to generate summary
        llm = OpenAI(model="gpt-4o-mini")
        summary = llm.predict(
            prompt.format(
                content="\n".join(chunks),
                style_examples="\n---\n".join(self.style_examples[:2])  # Use first 2 examples
            )
        )
        
        processing_time = time.time() - start_time
        logger.info(f"✨ Generated summary in {processing_time:.2f}s")
        return summary.strip()
        
    def _load_article_content(self, url: str) -> Dict:
        """
        Load article content and metadata from content directory
        
        Args:
            url (str): Article URL to load content for
            
        Returns:
            Dict: Article data including content and metadata
        """
        logger.debug(f"📥 Loading content for URL: {url}")
        link_hash = str(hash(url))
        article_data = {'url': url}
        
        # Load content file
        content_path = os.path.join(self.content_dir, f"{link_hash}_content.txt")
        if os.path.exists(content_path):
            logger.debug(f"📄 Found content file: {content_path}")
            with open(content_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Skip metadata lines and separator
                content_start = 4  # Skip URL, title, and separator lines
                article_data['content'] = ''.join(lines[content_start:])
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

    def process_batch(self, urls: List[str]) -> str:
        """
        Process a batch of articles and create newsletter section
        
        Args:
            urls (List[str]): List of article URLs to process
            
        Returns:
            str: Generated newsletter section content
        """
        logger.info(f"🔄 Processing batch of {len(urls)} URLs")
        articles = []
        for url in urls:
            article_data = self._load_article_content(url)
            if article_data.get('content'):
                articles.append(article_data)
            else:
                logger.warning(f"⚠️ No content found for URL: {url}")
        
        logger.info(f"📊 Found content for {len(articles)} out of {len(urls)} URLs")
        
        # Process articles in this batch
        sections = []
        for article in articles:
            try:
                start_time = time.time()
                section = self.create_section(article)
                sections.append(section)
                processing_time = time.time() - start_time
                logger.info(f"✅ Generated section for {article.get('url')} in {processing_time:.2f}s")
            except Exception as e:
                logger.error(f"❌ Error processing article {article.get('url')}: {str(e)}", exc_info=True)
                continue
                
        return "\n\n".join(sections)

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
        
        # Process URLs in batches
        all_sections = []
        for i in range(0, len(urls), batch_size):
            batch_num = i//batch_size + 1
            total_batches = (len(urls) + batch_size - 1) // batch_size
            logger.info(f"🔄 Processing batch {batch_num}/{total_batches}")
            
            batch_start = time.time()
            batch_urls = urls[i:i + batch_size]
            batch_content = self.process_batch(batch_urls)
            if batch_content:
                all_sections.append(batch_content)
            batch_time = time.time() - batch_start
            logger.info(f"✅ Completed batch {batch_num} in {batch_time:.2f}s")
            
        content = "\n\n".join(all_sections)
        
        # Add header
        newsletter = f"""# Update Night

_Your weekly dose of tech updates_

{content}
"""
        
        # Save newsletter
        logger.info(f"💾 Saving newsletter to {output_file}")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(newsletter)
        
        total_time = time.time() - start_time    
        logger.info(f"🎉 Newsletter creation completed in {total_time:.2f}s")
        return output_file
