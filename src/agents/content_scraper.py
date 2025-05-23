from crewai import Agent
from typing import List, Dict
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig
import os
import hashlib
import base64
from PIL import Image
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from src.utils.logging_config import setup_logging, get_logger
from src.config import Config

# Setup logging
setup_logging()
logger = get_logger('ContentScraper')

class ContentScraperAgent:
    def _load_article_content(self, url: str) -> Dict:
        """
        Load previously scraped article content from disk

        Args:
            url (str): URL of the article to load

        Returns:
            Dict: Article data including content and metadata
        """
        link_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()[:16]
        content_path = os.path.join(self.content_dir, f"{link_hash}_content.txt")
        metadata_path = os.path.join(self.content_dir, f"{link_hash}_info.txt")
        screenshot_path = os.path.join(self.content_dir, f"{link_hash}.png")

        article_data = {'url': url}

        # Load content
        if os.path.exists(content_path):
            with open(content_path, 'r', encoding='utf-8') as f:
                content = f.read().split('-' * 50 + '\n\n')
                if len(content) > 1:
                    article_data['content'] = content[1]

        # Load metadata
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('Title: '):
                        article_data['title'] = line.replace('Title: ', '').strip()
                        break

        # Add screenshot path if it exists
        if os.path.exists(screenshot_path):
            article_data['screenshot_path'] = screenshot_path

        return article_data

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
                    current_idx = links.index(link) + 1
                    link_hash = hashlib.sha256(link['url'].encode('utf-8')).hexdigest()[:16]
                    content_path = os.path.join(self.content_dir, f"{link_hash}_content.txt")
                    metadata_path = os.path.join(self.content_dir, f"{link_hash}_info.txt")
                    error_path = os.path.join(self.content_dir, f"{link_hash}_error.txt")

                    # Check if content already exists and was successful (no error file)
                    content_exists = os.path.exists(content_path)
                    metadata_exists = os.path.exists(metadata_path)
                    error_exists = os.path.exists(error_path)

                    logger.debug(f"[{current_idx}/{len(links)}] Content exists: {content_exists}, Metadata exists: {metadata_exists}, Error exists: {error_exists}")

                    if content_exists and metadata_exists and not error_exists:
                        # Verify content file is not empty
                        with open(content_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if len(content.strip()) > 0:
                                logger.info(f"[{current_idx}/{len(links)}] ⏩ Skipping URL (already scraped): {link['url']}")
                                # Load existing data
                                article_data = self._load_article_content(link['url'])
                                if article_data.get('content'):
                                    results.append(article_data)
                                continue
                            else:
                                logger.info(f"[{current_idx}/{len(links)}] 🔄 Re-scraping URL (empty content file): {link['url']}")
                    elif error_exists:
                        logger.info(f"[{current_idx}/{len(links)}] 🔄 Retrying previously failed URL: {link['url']}")

                    logger.info(f"[{current_idx}/{len(links)}] 📥 Scraping URL: {link['url']}")

                    # Setup default config
                    config = CrawlerRunConfig(
                        screenshot=True,
                        screenshot_wait_for=10.0,  # Increased to allow for multiple scrolls
                        magic=True,
                        simulate_user=True,
                        override_navigator=True,
                        cache_mode=CacheMode.BYPASS,
                        page_timeout=45000,  # Increased timeout for longer scrolling
                        delay_before_return_html=2.0,  # Increased delay to ensure content is loaded
                        js_code="""
                            new Promise(resolve => {
                                // Function to scroll to bottom of page
                                const scrollToBottom = () => {
                                    window.scrollTo(0, document.body.scrollHeight);
                                };

                                // Scroll to bottom 3 times with delays
                                setTimeout(() => {
                                    console.log("First scroll to bottom");
                                    scrollToBottom();

                                    setTimeout(() => {
                                        console.log("Second scroll to bottom");
                                        scrollToBottom();

                                        setTimeout(() => {
                                            console.log("Third scroll to bottom");
                                            scrollToBottom();

                                            // Finally scroll back to top for screenshot
                                            setTimeout(() => {
                                                console.log("Final scroll to top");
                                                window.scrollTo(0, 0);
                                                setTimeout(resolve, 500);
                                            }, 2000);
                                        }, 2000);
                                    }, 2000);
                                }, 1000);
                            })
                        """
                    )

                    # Special handling for GitHub repository URLs
                    if 'github.com' in link['url']:
                        logger.info(f"[{current_idx}/{len(links)}] 🌐 Handling GitHub URL with redirect blocking")
                        config = CrawlerRunConfig(
                            screenshot=True,
                            screenshot_wait_for=15.0,  # Increased wait time for GitHub with multiple scrolls
                            # magic=True,
                            # simulate_user=True,
                            override_navigator=True,
                            cache_mode=CacheMode.BYPASS,
                            page_timeout=60000,  # Increased timeout for GitHub with multiple scrolls
                            delay_before_return_html=3.0,  # Increased delay for GitHub
                            js_code="""
                                new Promise(resolve => {
                                    // Function to scroll to bottom of page
                                    const scrollToBottom = () => {
                                        window.scrollTo(0, document.body.scrollHeight);
                                    };

                                    // Wait for repository content to load
                                    const checkContent = () => {
                                        const repoContent = document.querySelector('.repository-content, .markdown-body');
                                        if (repoContent) {
                                            // Scroll to bottom 3 times with delays
                                            console.log("First scroll to bottom");
                                            scrollToBottom();

                                            setTimeout(() => {
                                                console.log("Second scroll to bottom");
                                                scrollToBottom();

                                                setTimeout(() => {
                                                    console.log("Third scroll to bottom");
                                                    scrollToBottom();

                                                    // Finally scroll back to top for screenshot
                                                    setTimeout(() => {
                                                        console.log("Final scroll to top");
                                                        window.scrollTo(0, 0);
                                                        setTimeout(resolve, 1000);
                                                    }, 2000);
                                                }, 2000);
                                            }, 2000);
                                        } else {
                                            setTimeout(checkContent, 500);
                                        }
                                    };
                                    setTimeout(checkContent, 3000);
                                })
                            """
                        )
                        result = await crawler.arun(url=link['url'], config=config)
                    # Handle YouTube URLs
                    elif 'youtube.com' in link['url'] or 'youtu.be' in link['url']:
                        # Extract video ID
                        if 'youtube.com' in link['url']:
                            parsed_url = urlparse(link['url'])
                            video_id = parse_qs(parsed_url.query).get('v', [None])[0]
                        else:  # youtu.be
                            video_id = urlparse(link['url']).path[1:]

                        if not video_id:
                            raise ValueError("Could not extract YouTube video ID")

                        # Get transcript
                        try:
                            logger.info(f"[{current_idx}/{len(links)}] 🎬 Getting transcript for video ID: {video_id}")
                            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                            logger.info(f"[{current_idx}/{len(links)}] ✅ Got transcript with {len(transcript_list)} entries")

                            # Combine transcript parts into markdown
                            transcript_text = "\n\n# Video Transcript\n\n"
                            for entry in transcript_list:
                                timestamp = int(entry['start'])
                                minutes = timestamp // 60
                                seconds = timestamp % 60
                                transcript_text += f"[{minutes:02d}:{seconds:02d}] {entry['text']}\n"

                            # Get page content first
                            logger.info(f"[{current_idx}/{len(links)}] 🌐 Getting page content")
                            page_result = await crawler.arun(url=link['url'], config=config)

                            # Add transcript to the page content
                            if hasattr(page_result, 'markdown'):
                                logger.info(f"[{current_idx}/{len(links)}] 📝 Combining page content with transcript")
                                page_content = page_result.markdown.raw_markdown if hasattr(page_result.markdown, 'raw_markdown') else str(page_result.markdown)

                                # Create a new result object
                                result = type('obj', (), {})
                                result.screenshot = page_result.screenshot if hasattr(page_result, 'screenshot') else None
                                result.markdown = type('obj', (), {})
                                result.markdown.raw_markdown = f"{page_content}\n\n{transcript_text}"

                                logger.debug(f"[{current_idx}/{len(links)}] Combined content length: {len(result.markdown.raw_markdown)}")
                                logger.info(f"[{current_idx}/{len(links)}] ✨ Successfully combined content")

                        except Exception as e:
                            logger.warning(f"Failed to get YouTube transcript: {str(e)}")
                            # Fallback to normal page scraping
                            result = await crawler.arun(url=link['url'], config=config)
                    else:
                        # For regular URLs, use default configuration
                        result = await crawler.arun(url=link['url'], config=config)

                    if not result or not hasattr(result, 'markdown'):
                        raise RuntimeError("Failed to get content from URL")

                    # Create content files
                    os.makedirs(self.content_dir, exist_ok=True)
                    logger.debug(f"[{current_idx}/{len(links)}] 📝 Saving content to {content_path}")
                    with open(content_path, 'w', encoding='utf-8') as f:
                        f.write(f"URL: {link['url']}\n")
                        f.write(f"Title: {link.get('title', 'No title')}\n")
                        f.write("-" * 50 + "\n\n")
                        f.write(result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown))

                    # Process and save screenshot
                    screenshot = result.screenshot if hasattr(result, 'screenshot') else None
                    if screenshot:
                        screenshot_path = os.path.join(self.content_dir, f"{link_hash}.png")
                        logger.debug(f"[{current_idx}/{len(links)}] 📸 Processing screenshot for {link['url']}")

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
                        logger.debug(f"[{current_idx}/{len(links)}] ✂️ Cropping screenshot to 16:9 ratio")
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
                        logger.debug(f"[{current_idx}/{len(links)}] 📸 Screenshot saved as {target_width}x{target_height} PNG")
                    else:
                        logger.warning(f"[{current_idx}/{len(links)}] ⚠️ No screenshot available for this URL")
                        screenshot_path = None

                    logger.debug(f"[{current_idx}/{len(links)}] 🔄 Updating link info with scraped data")
                    # Add scraped data to link info
                    link.update({
                        'content': result.markdown.raw_markdown,
                        'screenshot_path': screenshot_path,
                        'title': link.get('title', '')
                    })
                    results.append(link)

                    # Remove any previous error file if it exists
                    if os.path.exists(error_path):
                        os.remove(error_path)

                    # Save metadata file
                    metadata_path = os.path.join(self.content_dir, f"{link_hash}_info.txt")
                    logger.debug(f"[{current_idx}/{len(links)}] 📋 Saving metadata to {metadata_path}")
                    with open(metadata_path, 'w', encoding='utf-8') as f:
                        f.write("Scraping Result Info:\n")
                        f.write(f"URL: {link['url']}\n")
                        f.write(f"Title: {link['title']}\n")
                        f.write(f"Title from link: {link.get('title', 'No title')}\n")
                        screenshot_file = os.path.join(self.content_dir, f"{link_hash}.png")
                        f.write(f"Screenshot Path: {screenshot_file if os.path.exists(screenshot_file) else 'None'}\n")
                        f.write(f"Content Path: {content_path}\n")
                        f.write(f"Success: True\n")

                except Exception as e:
                    current_idx = links.index(link) + 1
                    error_msg = f"Error scraping {link['url']}: {str(e)}"
                    logger.error(f"[{current_idx}/{len(links)}] ❌ {error_msg}", exc_info=True)

                    # Save error info
                    os.makedirs(self.content_dir, exist_ok=True)
                    link_hash = hashlib.sha256(link['url'].encode('utf-8')).hexdigest()[:16]
                    error_path = os.path.join(self.content_dir, f"{link_hash}_error.txt")
                    logger.debug(f"[{current_idx}/{len(links)}] ⚠️ Saving error info to {error_path}")

                    # Clean up any files from failed attempt
                    screenshot_path = os.path.join(self.content_dir, f"{link_hash}.png")
                    for file_path in [content_path, metadata_path, screenshot_path]:
                        if os.path.exists(file_path):
                            os.remove(file_path)

                    with open(error_path, 'w', encoding='utf-8') as f:
                        f.write("Scraping Error Info:\n")
                        f.write(f"URL: {link['url']}\n")
                        f.write(f"Title: {link.get('title', 'No title')}\n")
                        f.write(f"Error: {str(e)}\n")
                        f.write(f"Success: False\n")
                    continue

        skipped = sum(1 for link in links
                     if os.path.exists(os.path.join(self.content_dir, f"{hashlib.sha256(link['url'].encode('utf-8')).hexdigest()[:16]}_content.txt"))
                     and os.path.exists(os.path.join(self.content_dir, f"{hashlib.sha256(link['url'].encode('utf-8')).hexdigest()[:16]}_info.txt"))
                     and not os.path.exists(os.path.join(self.content_dir, f"{hashlib.sha256(link['url'].encode('utf-8')).hexdigest()[:16]}_error.txt")))
        logger.info(f"✅ Completed content scraping. Successfully processed {len(results)} out of {len(links)} links ({skipped} skipped)")
        return results
