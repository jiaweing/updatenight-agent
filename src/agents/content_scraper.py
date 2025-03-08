from crewai import Agent
from typing import List, Dict
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig
import os
import base64
from PIL import Image
from src.utils.logging_config import setup_logging, get_logger
from config import Config

# Setup logging
setup_logging()
logger = get_logger('ContentScraper')

class ContentScraperAgent:
    def __init__(self):
        self.agent = Agent(
            role='Content Scraper',
            goal='Scrape content and take screenshots of provided URLs',
            backstory="""You are a specialized agent that extracts content from web pages
            using crawl4ai. You can handle different types of web pages and ensure
            important content is captured along with screenshots."""
        )
        
        browser_config = BrowserConfig(
            headless=Config.HEADLESS,
            viewport_width=1920,
            viewport_height=1080,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            extra_args=[
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
                '--allow-running-insecure-content',
                '--disable-site-isolation-trials'
            ],
            headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'DNT': '1'
            }
        )
        self.crawler = AsyncWebCrawler(
            config=browser_config, 
            timeout=30,
            use_stealth_js=True
        )
        self.content_dir = "content"
        os.makedirs(self.content_dir, exist_ok=True)
        
    async def scrape_content(self, links: List[Dict]) -> List[Dict]:
        """
        Scrape content and take screenshots for each link
        
        Args:
            links (List[Dict]): List of dictionaries containing link data
            
        Returns:
            List[Dict]: Original link data enriched with content and screenshot paths
        """

        logger.info(f"🔎 Starting content scraping for {len(links)} links")
        results = []
        async with self.crawler as crawler:
            for link in links:
                try:
                    logger.info(f"📥 Scraping URL: {link['url']}")
                    
                    # Create config with headers and CORS handling
                    config = CrawlerRunConfig(
                        screenshot=True,
                        screenshot_wait_for=3.0,  # Time for magic features to execute
                        magic=True,
                        simulate_user=True,
                        override_navigator=True,
                        cache_mode=CacheMode.BYPASS,
                        page_timeout=30000,
                        delay_before_return_html=1.0,  # Reduced since we handle delays in JS
                        js_code="""
                            new Promise(resolve => {
                                setTimeout(() => {
                                    window.scrollTo(0, 0);
                                    setTimeout(resolve, 500);
                                }, 2000);
                            })
                        """
                    )
                    
                    # Scrape the page with headers passed separately
                    result = await crawler.arun(
                        url=link['url'],
                        config=config,
                    )
                
                    # Create content files
                    os.makedirs(self.content_dir, exist_ok=True)
                    link_hash = str(hash(link['url']))
                    content_path = os.path.join(self.content_dir, f"{link_hash}_content.txt")
                    logger.debug(f"📝 Saving content to {content_path}")
                    with open(content_path, 'w', encoding='utf-8') as f:
                        f.write(f"URL: {link['url']}\n")
                        f.write(f"Title: {link.get('title', 'No title')}\n")
                        f.write("-" * 50 + "\n\n")
                        f.write(result.markdown.raw_markdown)

                    # Process and save screenshot
                    screenshot = result.screenshot if hasattr(result, 'screenshot') else None
                    if screenshot:
                        screenshot_path = os.path.join(self.content_dir, f"{link_hash}.png")
                        logger.debug(f"📸 Processing screenshot for {link['url']}")
                        
                        # Convert to bytes if needed
                        screenshot_bytes = (
                            base64.b64decode(screenshot) if isinstance(screenshot, str)
                            else screenshot
                        )
                        
                        # Save original screenshot temporarily
                        temp_path = os.path.join(self.content_dir, f"{link_hash}_temp.png")
                        with open(temp_path, 'wb') as f:
                            f.write(screenshot_bytes)
                        
                        # Process with PIL
                        logger.debug("✂️ Cropping screenshot to 16:9 ratio")
                        with Image.open(temp_path) as img:
                            # Calculate dimensions for 16:9 aspect ratio
                            target_width = 1920
                            target_height = 1080  # 16:9 ratio
                            
                            # Get current dimensions
                            orig_width, orig_height = img.size
                            
                            # Calculate resize ratio to match target width
                            ratio = target_width / orig_width
                            new_height = int(orig_height * ratio)
                            
                            # Resize to target width
                            img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
                            
                            # Crop top portion to target height
                            if new_height > target_height:
                                img = img.crop((0, 0, target_width, target_height))
                            
                            # Save final version
                            img.save(screenshot_path, 'PNG', optimize=True)
                        
                        # Clean up temp file
                        os.remove(temp_path)
                        logger.debug(f"📸 Screenshot saved as {target_width}x{target_height} PNG")
                    else:
                        logger.warning("⚠️ No screenshot available for this URL")
                        screenshot_path = None
                    
                    logger.debug(f"🔄 Updating link info with scraped data")
                    # Add scraped data to link info
                    link.update({
                        'content': result.markdown.raw_markdown,
                        'screenshot_path': screenshot_path,
                        'title': link.get('title', '')
                    })
                    results.append(link)

                    # Save metadata file
                    metadata_path = os.path.join(self.content_dir, f"{link_hash}_info.txt")
                    logger.debug(f"📋 Saving metadata to {metadata_path}")
                    with open(metadata_path, 'w', encoding='utf-8') as f:
                        f.write("Scraping Result Info:\n")
                        f.write(f"URL: {link['url']}\n")
                        f.write(f"Title: {link['title']}\n")
                        f.write(f"Title from link: {link.get('title', 'No title')}\n")
                        f.write(f"Screenshot Path: {screenshot_path}\n")
                        f.write(f"Content Path: {content_path}\n")
                        f.write(f"Success: True\n")
                    
                except Exception as e:
                    error_msg = f"Error scraping {link['url']}: {str(e)}"
                    logger.error(f"❌ {error_msg}", exc_info=True)
                    
                    # Save error info
                    os.makedirs(self.content_dir, exist_ok=True)
                    link_hash = str(hash(link['url']))
                    error_path = os.path.join(self.content_dir, f"{link_hash}_error.txt")
                    logger.debug(f"⚠️ Saving error info to {error_path}")
                    with open(error_path, 'w', encoding='utf-8') as f:
                        f.write("Scraping Error Info:\n")
                        f.write(f"URL: {link['url']}\n")
                        f.write(f"Title: {link.get('title', 'No title')}\n")
                        f.write(f"Error: {str(e)}\n")
                        f.write(f"Success: False\n")
                    continue
                
        logger.info(f"✅ Completed content scraping. Successfully processed {len(results)} out of {len(links)} links")
        return results
