"""
Link categorization utility that uses AI to categorize links in links.md.
"""
from typing import Dict, List, Optional
import os
import re
import asyncio
from collections import defaultdict
import markdown
from bs4 import BeautifulSoup
from agents.content_scraper import ContentScraperAgent
from utils.ai_categorizer import AICategorizer
from utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('LinkCategorizer')

class LinkCategorizer:
    """
    Categorizes links in links.md using AI.
    """

    def __init__(self, links_file: str = "links.md"):
        """
        Initialize the link categorizer.

        Args:
            links_file: Path to the links.md file
        """
        self.links_file = links_file
        self.ai_categorizer = AICategorizer()
        self.content_scraper = ContentScraperAgent()

    async def categorize_links(self) -> Dict[str, List[Dict]]:
        """
        Categorize all links in the links.md file using AI.

        Returns:
            A dictionary mapping categories to lists of link data
        """
        # Parse the links.md file to get all links
        all_links = self._parse_links_file()
        logger.info(f"📊 Found {len(all_links)} links in {self.links_file}")

        # Scrape content for all links
        scraped_data = await self.content_scraper.scrape_content(all_links)
        logger.info(f"🔍 Successfully scraped {len(scraped_data)} out of {len(all_links)} links")

        # Categorize each link using AI
        categorized_links = defaultdict(list)
        for article in scraped_data:
            if 'content' in article:
                # Use AI to categorize the article
                category = self.ai_categorizer.categorize(article['content'])
                categorized_links[category].append(article)
            else:
                # If no content was scraped, use "Under the Radar" as default
                logger.warning(f"⚠️ No content found for {article['url']}, using default category")
                categorized_links["Under the Radar"].append(article)

        return categorized_links

    def _parse_links_file(self) -> List[Dict]:
        """
        Parse the links.md file to extract all links.

        Returns:
            A list of dictionaries containing link data
        """
        if not os.path.exists(self.links_file):
            logger.error(f"❌ Links file not found: {self.links_file}")
            raise FileNotFoundError(f"Links file not found: {self.links_file}")

        with open(self.links_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse markdown to HTML
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')

        links = []
        seen_urls = {}  # Track seen URLs to avoid duplicates

        # Process all links in the order they appear
        for link in soup.find_all('a'):
            url = link.get('href', '')
            if not url:
                continue

            # Normalize URL for comparison
            normalized_url = url.lower()

            # Skip duplicates
            if normalized_url in seen_urls:
                continue

            # Mark as seen
            seen_urls[normalized_url] = True

            # Extract title and context
            title = link.get_text().strip()
            context = ""
            list_item = link.find_parent('li')
            if list_item:
                list_text = list_item.get_text()
                if title:
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

        return links

    def generate_links_file(self, categorized_links: Dict[str, List[Dict]]) -> None:
        """
        Generate a new links.md file with AI-categorized links.

        Args:
            categorized_links: Dictionary mapping categories to lists of link data
        """
        content = ["# Links for Update Night Newsletter\n"]

        # Get all categories from AICategorizer to maintain consistent order
        categories = self.ai_categorizer.CATEGORIES

        for category in categories:
            if category in categorized_links and categorized_links[category]:
                content.append(f"\n## {category}\n")

                # Sort links by title for now (could be changed to other criteria)
                sorted_links = sorted(
                    categorized_links[category],
                    key=lambda x: x.get('title', '').lower()
                )

                for link in sorted_links:
                    # Clean and format the context
                    clean_context = re.sub(
                        r'https?://\S+',
                        '',
                        link.get('context', '')
                    ).strip()
                    if len(clean_context) > 100:
                        clean_context = clean_context[:97] + "..."

                    # Use the title from the link or extract from URL
                    title = link.get('title', '')
                    if not title:
                        title = link['url'].split('/')[-1].replace('-', ' ').title()
                    if len(title) > 50:
                        title = title[:47] + "..."

                    content.append(
                        f"- [{title}]({link['url']}) - {clean_context}\n"
                    )

        # Write to file
        logger.info(f"💾 Writing AI-categorized links to {self.links_file}")
        with open(self.links_file, 'w', encoding='utf-8') as f:
            f.write(''.join(content))
        logger.info(f"✨ Successfully wrote {self.links_file}")

async def categorize_and_update_links(links_file: str = "links.md") -> None:
    """
    Categorize links in links.md using AI and update the file.

    Args:
        links_file: Path to the links.md file
    """
    categorizer = LinkCategorizer(links_file)
    categorized_links = await categorizer.categorize_links()
    categorizer.generate_links_file(categorized_links)
    logger.info("✅ Links have been categorized and links.md has been updated")
