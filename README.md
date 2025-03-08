# Update Night Newsletter Agent

An automated system for generating the Update Night newsletter using AI agents. This project uses crewAI to orchestrate multiple agents that collect links from Discord, scrape content, and generate newsletter content in the Update Night style.

## Features

- Automated Discord link collection with categorization
- Web scraping with screenshots using crawl4ai
- AI-powered content summarization with writing style matching
- Markdown output with properly formatted sections and images

## Project Structure

```
.
├── src/
│   ├── agents/
│   │   ├── discord_collector.py  # Collects links from Discord
│   │   ├── link_collector.py     # Processes links.md
│   │   ├── content_scraper.py    # Web scraping and screenshots
│   │   └── content_writer.py     # Newsletter generation
│   ├── config.py                 # Configuration management
│   └── main.py                   # Main orchestrator
├── samples/                      # Writing style examples
├── output/                      # Generated content
├── requirements.txt             # Python dependencies
└── .env                        # Configuration
```

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

Edit `.env` and add:

- Your Discord bot token
- Discord server (guild) ID - Right click server icon -> Copy Server ID
- Starting date for link collection (default: 2025-02-06)
- OpenAI API key

### Discord Bot Setup

1. Create a new Discord application at https://discord.com/developers/applications
2. Create a bot and get the token
3. Enable required intents:
   - Server Members Intent
   - Message Content Intent (required to read message content)
   - Guild Messages Intent (required to read server messages)
4. Invite the bot to your server with these permissions:
   - Read Messages/View Channels
   - Read Message History
5. Add the bot token and channel IDs to your `.env` file

## Usage

1. The agent will automatically:

   - Collect links from all Discord channels except:
     - rules
     - moderator-only
     - welcome
     - announcements
     - featured
     - jobs
     - conferences
     - hackathons
   - Categorize the collected links into sections:
     - The Big Picture (major headlines)
     - Under the Radar (undercovered stories)
     - TrAIn of Thought (AI/ML news)
     - The Grid (design/component libraries)
     - The Spotlight (open source highlights)
   - Generate links.md with categorized links
   - Scrape content and take screenshots
   - Generate the final newsletter

2. Run the newsletter generation:

```bash
python src/main.py
```

The generated newsletter will be saved to `output/newsletter.md` along with screenshots of the referenced web pages.

## Link Categorization

Links are automatically categorized based on context and keywords:

- **The Big Picture**: Major announcements, launches, breaking news
- **Under the Radar**: Experimental features, insights, analyses
- **TrAIn of Thought**: AI/ML developments, models, research
- **The Grid**: Design systems, UI/UX, component libraries
- **The Spotlight**: Open source projects, tools, resources

You can customize categorization by modifying the keywords in `discord_collector.py`.

## Contributing

Feel free to submit issues and enhancement requests!
