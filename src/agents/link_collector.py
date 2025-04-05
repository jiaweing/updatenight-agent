from crewai import Agent
from typing import List
import markdown
import os
from bs4 import BeautifulSoup
from src.utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('LinkCollector')

class LinkCollectorAgent:
    def __init__(self):
        self.agent = Agent(
            role='Link Collector',
            goal='Collect and validate links from links.md file',
            backstory="""You are a specialized agent that reads from a markdown file containing links
            and ensures they are valid and accessible. You understand markdown formatting and can
            extract URLs while preserving their context."""
        )

    def collect_links(self, file_path: str) -> List[dict]:
        """
        Read links from markdown file and return structured data.
        
        Args:
            file_path (str): Path to links.md file
            
        Returns:
            List[dict]: List of dictionaries containing link data
            [{'url': 'https://...', 'title': 'Title if available', 'context': 'Surrounding text'}]
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Links file not found: {file_path}")
            
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Parse markdown to HTML
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        
        links = []
        seen_urls = {}  # Use dict to store normalized URLs and their original form

        # Process all links in the order they appear
        for link in soup.find_all('a'):
            url = link.get('href', '')
            if not url:
                logger.debug(f"⏩ Skipping empty URL")
                continue
                
            # Normalize URL for comparison (convert to lowercase)
            normalized_url = url.lower()
            
            # Skip duplicates based on normalized URL only
            if normalized_url in seen_urls:
                logger.debug(f"⏩ Skipping duplicate URL: {url}")
                continue

            # Store normalized URL after checking for duplicates
            seen_urls[normalized_url] = True
            
            # Extract title and context if link is in a list item
            title = link.get_text().strip()
            context = ""
            list_item = link.find_parent('li')
            if list_item:
                if title:
                    list_text = list_item.get_text()
                    try:
                        context = list_text.split(title)[-1].strip('- ')
                    except:
                        context = list_text.strip('- ')
                else:
                    context = list_text.strip('- ')
                    
                link_data = {
                    'url': url,
                    'title': title,
                    'context': context
                }
                links.append(link_data)
        
        # Log extracted links
        total_found = len(seen_urls)
        skipped = len(soup.find_all('a')) - total_found
        logger.info(f"\n🔍 Extracted {total_found} unique links from {file_path} ({skipped} duplicates filtered)")
        for idx, link in enumerate(links, 1):
            logger.info(f"\n📌 Link #{idx}")
            logger.info(f"  • URL: {link['url']}")
            logger.debug(f"  • Title: {link['title']}")
            logger.debug(f"  • Context: {link['context']}")
                
        return links
