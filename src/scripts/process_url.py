#!/usr/bin/env python3
import asyncio
import argparse
import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

from src.agents.content_scraper import ContentScraperAgent
from src.agents.content_writer import ContentWriterAgent
from src.utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('ProcessURL')

async def main():
    parser = argparse.ArgumentParser(description='Process a single URL and generate a report')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('--output', '-o', default='report.md', help='Output markdown file path (default: report.md)')
    args = parser.parse_args()
    
    try:
        # Initialize agents
        logger.info("🤖 Initializing agents...")
        scraper = ContentScraperAgent()
        writer = ContentWriterAgent()
        
        # Scrape content
        logger.info(f"🔎 Scraping content from: {args.url}")
        scraped_data = await scraper.scrape_content([{'url': args.url}])
        
        if not scraped_data:
            logger.error("❌ Failed to scrape content")
            return 1
            
        # Generate report using ContentWriter
        logger.info("✍️ Generating report...")
        article_data = scraped_data[0]
        # Set output file path before creating section
        writer.output_file = args.output
        section = writer.create_section(article_data)
        
        # Write report to file
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(section)
            
        logger.info(f"✅ Report generated: {args.output}")
        return 0
        
    except Exception as e:
        logger.error(f"❌ Error processing URL: {str(e)}", exc_info=True)
        return 1

if __name__ == '__main__':
    exit_code = asyncio.run(main())
    exit(exit_code)
