# Update Night Newsletter Agent

An automated system for generating the Update Night newsletter using AI agents. This project uses crewAI to orchestrate multiple agents that collect links from Discord, scrape content, and generate newsletter content in the Update Night style.

## 🚀 Features

- Automated Discord link collection with categorization
- Web scraping with screenshots using crawl4ai
- AI-powered content summarization with writing style matching
- Markdown output with properly formatted sections and images
- Configurable crawler settings for headless mode and timeouts
- OpenAI GPT integration for intelligent content processing

## 📁 Project Structure

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

## 🛠️ Setup

### Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Discord bot token and permissions

### Installation

1. Install dependencies:

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

Edit `.env` and configure:

```ini
# Required
DISCORD_TOKEN=your_discord_bot_token
DISCORD_GUILD_ID=your_server_id
OPENAI_API_KEY=your_openai_api_key

# Optional
COLLECT_SINCE_DATE=2025-02-06  # Default: current date
OUTPUT_DIR=output             # Default: output
HEADLESS=true                # Default: true (run browser in headless mode)
TIMEOUT=30                   # Default: 30 (seconds for page load timeout)
```

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
5. Add the bot token and server ID to your `.env` file

## 🚗 Usage

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
   - Generate the final newsletter using OpenAI's GPT models

2. Run the newsletter generation:

```bash
python src/main.py
```

The generated newsletter will be saved to `output/newsletter.md` along with screenshots of the referenced web pages.

## 🎯 Link Categorization

Links are automatically categorized based on context and keywords:

- **The Big Picture**: Major announcements, launches, breaking news
- **Under the Radar**: Experimental features, insights, analyses
- **TrAIn of Thought**: AI/ML developments, models, research
- **The Grid**: Design systems, UI/UX, component libraries
- **The Spotlight**: Open source projects, tools, resources

You can customize categorization by modifying the keywords in `discord_collector.py`.

## 🔧 Configuration

### Crawler Settings

- `HEADLESS`: Controls whether to run the browser in headless mode (default: true)
- `TIMEOUT`: Maximum time in seconds to wait for a page to load (default: 30)

### OpenAI Integration

The agent uses OpenAI's GPT models to:

- Analyze and categorize content
- Generate summaries in the Update Night style
- Ensure consistent tone and formatting
- Extract key insights from articles

Make sure to set your `OPENAI_API_KEY` in the `.env` file.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

To contribute:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

Please make sure to update tests as appropriate.
