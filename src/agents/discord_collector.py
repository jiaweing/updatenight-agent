from crewai import Agent
from typing import List, Dict
import discord
from datetime import datetime
import re
from collections import defaultdict
from src.utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('DiscordCollector')

class DiscordCollectorAgent:
    # Channels to exclude from collection
    EXCLUDED_CHANNELS = [
        'rules',
        'moderator-only',
        'welcome',
        'announcements',
        'featured',
        'jobs',
        'conferences',
        'hackathons'
    ]
    
    def __init__(self):
        logger.info("🤖 Initializing DiscordCollectorAgent")
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guild_messages = True
        
        self.agent = Agent(
            role='Discord Link Collector',
            goal='Collect and categorize links from Discord messages',
            backstory="You are a specialized agent that collects links from Discord "
                     "channels, categorizes them based on content, and formats them "
                     "for the Update Night newsletter."
        )
        self.client = discord.Client(intents=intents)
        self.categories = [
            "The Big Picture",
            "Under the Radar",
            "TrAIn of Thought",
            "The Grid",
            "The Spotlight"
        ]
        self.category_keywords = self._load_category_keywords()
        
    def _load_category_keywords(self) -> Dict[str, List[str]]:
        """Load category keywords for classification"""
        return {
            "The Big Picture": [
                "announcement", "launch", "release", "major", "breaking",
                "headline", "news", "unveiled", "introduces", "acquisition"
            ],
            "Under the Radar": [
                "experimental", "preview", "beta", "upcoming", "insight",
                "analysis", "deep dive", "behind the scenes", "investigation"
            ],
            "TrAIn of Thought": [
                "ai", "ml", "machine learning", "gpt", "llm", "neural",
                "model", "artificial intelligence", "transformer", "openai"
            ],
            "The Grid": [
                "design", "ui", "ux", "component", "library", "framework",
                "css", "style", "theme", "layout", "tailwind"
            ],
            "The Spotlight": [
                "opensource", "github", "project", "tool", "library",
                "framework", "resource", "utility", "package"
            ]
        }
        
    def _should_process_channel(self, channel) -> bool:
        """Check if we should process this channel"""
        channel_name = channel.name.lower()
        return not any(excluded in channel_name 
                      for excluded in self.EXCLUDED_CHANNELS)
    
    async def collect_links(self, token: str, guild_id: str,
                          since_date: datetime) -> None:
        """
        Collect links from specified Discord channels after a given date
        
        Args:
            token: Discord bot token
            channel_ids: List of channel IDs to collect from
            since_date: Collect messages after this date
        """
        links = defaultdict(list)
        
        @self.client.event
        async def on_ready():
            try:
                logger.info(f"🔰 Connected to Discord as {self.client.user}")
                # Get all channels in the guild
                guild = self.client.get_guild(int(guild_id))
                if not guild:
                    logger.error(f"❌ Could not find guild with ID {guild_id}")
                    raise ValueError(f"Could not find guild with ID {guild_id}")
                logger.info(f"🏠 Found guild: {guild.name}")
                
                # Process each text channel that isn't excluded
                for channel in guild.text_channels:
                    logger.info(f"👀 Checking channel: {channel.name}")
                    if not self._should_process_channel(channel):
                        logger.debug(f"⏩ Skipping excluded channel: {channel.name}")
                        continue
                        
                    logger.info(f"📢 Processing channel: {channel.name}")
                    async for message in channel.history(after=since_date, limit=None):
                        # Extract links from message
                        found_links = re.findall(r'https?://\S+', message.content)
                        
                        for link in found_links:
                            logger.debug(f"🔗 Found link in message: {link[:50]}...")
                            # Get message context (some words before/after the link)
                            context = message.content
                            
                            # Categorize the link based on context
                            category = self._categorize_link(context)
                            logger.debug(f"📑 Categorized link as: {category}")
                            
                            links[category].append({
                                'url': link,
                                'context': context,
                                'timestamp': message.created_at,
                                'author': str(message.author)
                            })
                            
                # Log statistics about collected links
                total_links = sum(len(links[cat]) for cat in links)
                logger.info(f"\n📊 Collection complete. Found {total_links} total links:")
                # Print collected links by category
                for category in self.categories:
                    if category in links:
                        logger.info(f"\n📎 {category} ({len(links[category])} links):")
                        for link_data in sorted(links[category], key=lambda x: x['timestamp'], reverse=True):
                            # Clean context for display
                            clean_context = re.sub(r'https?://\S+', '', link_data['context']).strip()
                            if len(clean_context) > 100:
                                clean_context = clean_context[:97] + "..."
                            logger.info(f"  • {link_data['url']}")
                            logger.debug(f"    Context: {clean_context}")

                # Generate links.md
                logger.info("\n📝 Generating links.md file")
                self._generate_links_file(links)
                logger.info("✅ Links file generated successfully")
                
            except Exception as e:
                logger.error("❌ Error during link collection", exc_info=True)
                raise
            finally:
                logger.info("👋 Closing Discord client connection")
                await self.client.close()
                
        await self.client.start(token)
        
    def _categorize_link(self, context: str) -> str:
        """Categorize a link based on its context using keywords"""
        scores = {category: 0 for category in self.categories}
        
        # Normalize context
        context = context.lower()
        
        # Score each category based on keyword matches
        for category, keywords in self.category_keywords.items():
            for keyword in keywords:
                if keyword in context:
                    scores[category] += 1
                    
        # Default to "Under the Radar" if no clear category
        max_score = max(scores.values())
        if max_score == 0:
            return "Under the Radar"
            
        # Return category with highest score
        return max(scores.items(), key=lambda x: x[1])[0]
        
    def _generate_links_file(self, categorized_links: Dict[str, List[Dict]]):
        """Generate links.md file with categorized links"""
        content = ["# Links for Update Night Newsletter\n"]
        
        for category in self.categories:
            if category in categorized_links and categorized_links[category]:
                content.append(f"\n## {category}\n")
                
                # Sort links by timestamp
                sorted_links = sorted(
                    categorized_links[category],
                    key=lambda x: x['timestamp'],
                    reverse=True
                )
                
                for link in sorted_links:
                    # Clean and format the context
                    clean_context = re.sub(
                        r'https?://\S+',
                        '',
                        link['context']
                    ).strip()
                    if len(clean_context) > 100:
                        clean_context = clean_context[:97] + "..."
                        
                    # Extract title from URL (basic version)
                    title = link['url'].split('/')[-1].replace('-', ' ').title()
                    if len(title) > 50:
                        title = title[:47] + "..."
                        
                    content.append(
                        f"- [{title}]({link['url']}) - {clean_context}\n"
                    )
                    
        # Write to file
        logger.info("💾 Writing links to links.md")
        with open('links.md', 'w', encoding='utf-8') as f:
            f.write(''.join(content))
        logger.info("✨ Successfully wrote links.md")
