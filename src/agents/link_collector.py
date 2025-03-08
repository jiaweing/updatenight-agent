from crewai import Agent
from typing import List
import markdown
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
        for link in soup.find_all('a'):
            # Get the containing list item for context
            list_item = link.find_parent('li')
            if list_item:
                # Extract URL, title, and surrounding text
                url = link.get('href', '')
                title = link.get_text()
                # Get text after the link in the list item
                context = list_item.get_text().split(title)[-1].strip('- ')
                
                links.append({
                    'url': url,
                    'title': title,
                    'context': context
                })
        
        return links
