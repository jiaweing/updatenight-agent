# Update Night Newsletter Agent

An automated system for generating the Update Night newsletter using AI agents. This project uses crewAI to orchestrate multiple agents that collect links, scrape content, and generate newsletter content in the Update Night style.

## Features

- Automated link collection from markdown files
- Web scraping with screenshots using crawl4ai
- AI-powered content summarization with writing style matching
- Markdown output with properly formatted sections and images

## Setup

1. Install dependencies (with Python 3.11+):

```bash
# Using pip
pip install -r requirements.txt

# Or using poetry
poetry install
```

2. Configure environment variables:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key.

3. Create required directories:

```bash
mkdir -p output samples
```

## Usage

1. Create a `links.md` file with your links in the following format:

```markdown
## Section Name

- [Title](url) - Brief description
- [Another Title](url) - Another description
```

2. (Optional) Add sample newsletter issues to the `samples` directory to help the AI match your writing style.

3. Run the newsletter generation:

```bash
python src/main.py
```

The generated newsletter will be saved to `output/newsletter.md` along with screenshots of the referenced web pages.

## Project Structure

```
.
├── src/
│   ├── agents/
│   │   ├── link_collector.py    # Processes links.md
│   │   ├── content_scraper.py   # Web scraping and screenshots
│   │   └── content_writer.py    # Newsletter generation
│   └── main.py                  # Main orchestrator
├── samples/                     # Writing style examples
├── output/                      # Generated content
├── links.md                     # Input links
├── requirements.txt             # Python dependencies
└── .env                        # Configuration
```

## Agent Workflow

1. **Link Collector Agent**

   - Reads links.md
   - Extracts URLs, titles, and context
   - Validates link accessibility

2. **Content Scraper Agent**

   - Scrapes content from each URL
   - Takes screenshots of pages
   - Stores assets in the output directory

3. **Content Writer Agent**
   - Analyzes scraped content
   - Matches Update Night writing style
   - Generates concise, informative summaries
   - Creates properly formatted markdown

## Contributing

Feel free to submit issues and enhancement requests!
