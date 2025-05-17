#!/usr/bin/env python3
import asyncio
import argparse
import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

from src.agents.content_writer import ContentWriterAgent
from src.utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('ProcessText')

async def main():
    parser = argparse.ArgumentParser(description='Process text from a file and generate a report')
    parser.add_argument('url', help='The URL to associate with the text (for reference)')
    parser.add_argument('--input', '-i', default='text.md', help='Input text file path (default: text.md)')
    parser.add_argument('--output', '-o', default='report.md', help='Output markdown file path (default: report.md)')
    args = parser.parse_args()
    
    try:
        # Initialize agent
        logger.info("🤖 Initializing content writer agent...")
        writer = ContentWriterAgent()
        
        # Read text from file
        logger.info(f"📄 Reading text from: {args.input}")
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text_content = f.read()
        except FileNotFoundError:
            logger.error(f"❌ Input file not found: {args.input}")
            return 1
        except Exception as e:
            logger.error(f"❌ Error reading input file: {str(e)}")
            return 1
            
        if not text_content:
            logger.error("❌ Input file is empty")
            return 1
            
        # Prepare article data
        article_data = {
            'url': args.url,
            'content': text_content,
            'title': os.path.basename(args.url)  # Use the URL basename as a fallback title
        }
            
        # Generate report using ContentWriter
        logger.info("✍️ Generating report...")
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
        logger.error(f"❌ Error processing text: {str(e)}", exc_info=True)
        return 1

if __name__ == '__main__':
    exit_code = asyncio.run(main())
    exit(exit_code)
