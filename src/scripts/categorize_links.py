"""
Script to categorize links in links.md using AI.
"""
import asyncio
import argparse
import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.link_categorizer import categorize_and_update_links
from src.utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('CategorizeLinks')

async def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='Categorize links in links.md using AI')
    parser.add_argument('--file', type=str, default='links.md',
                        help='Path to the links.md file (default: links.md)')
    args = parser.parse_args()

    try:
        logger.info(f"🚀 Starting AI categorization of links in {args.file}")
        await categorize_and_update_links(args.file)
        logger.info("✅ Categorization complete")
        return 0
    except Exception as e:
        logger.error(f"❌ Error during categorization: {str(e)}", exc_info=True)
        return 1

if __name__ == "__main__":
    asyncio.run(main())
