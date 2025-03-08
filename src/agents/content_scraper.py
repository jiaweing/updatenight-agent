from crewai import Agent
from typing import List, Dict
from crawl4ai import CrawlerConfig, Crawler
from PIL import Image
import os

class ContentScraperAgent:
    def __init__(self):
        self.agent = Agent(
            role='Content Scraper',
            goal='Scrape content and take screenshots of provided URLs',
            backstory="""You are a specialized agent that extracts content from web pages
            using crawl4ai. You can handle different types of web pages and ensure
            important content is captured along with screenshots."""
        )
        
        self.crawler = None
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def setup_crawler(self):
        """Initialize crawl4ai crawler with configuration"""
        config = CrawlerConfig(
            # Configure crawl4ai options
            screenshot=True,
            headless=True,
            timeout=30
        )
        self.crawler = Crawler(config)
        
    def scrape_content(self, links: List[Dict]) -> List[Dict]:
        """
        Scrape content and take screenshots for each link
        
        Args:
            links (List[Dict]): List of dictionaries containing link data
            
        Returns:
            List[Dict]: Original link data enriched with content and screenshot paths
        """
        if not self.crawler:
            self.setup_crawler()
            
        results = []
        for link in links:
            try:
                # Scrape the page
                result = self.crawler.scrape(link['url'])
                
                # Save screenshot
                screenshot_path = os.path.join(
                    self.output_dir, 
                    f"{hash(link['url'])}.png"
                )
                result.screenshot.save(screenshot_path)
                
                # Add scraped data to link info
                link.update({
                    'content': result.content,
                    'screenshot_path': screenshot_path,
                    'title': result.title or link.get('title', '')
                })
                results.append(link)
                
            except Exception as e:
                print(f"Error scraping {link['url']}: {str(e)}")
                continue
                
        return results
