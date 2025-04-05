import asyncio
from datetime import datetime
from agents.discord_collector import DiscordCollectorAgent
from agents.link_collector import LinkCollectorAgent
from agents.content_scraper import ContentScraperAgent
from agents.content_writer import ContentWriterAgent
from crewai import Crew, Process
from config import Config

class UpdateNightCrew:
    def __init__(self):
        # Initialize agents
        self.discord_collector = DiscordCollectorAgent()
        self.link_collector = LinkCollectorAgent()
        self.content_scraper = ContentScraperAgent()
        self.content_writer = ContentWriterAgent()
        
        # Setup crew
        self.crew = Crew(
            agents=[
                self.link_collector.agent,
                self.content_scraper.agent,
                self.content_writer.agent
            ],
            process=Process.sequential
        )
        
    async def collect_discord_links(self):
        """Collect links from Discord channels"""
        since_date = datetime.strptime(Config.COLLECT_SINCE_DATE, '%Y-%m-%d')
        await self.discord_collector.collect_links(
            Config.DISCORD_TOKEN,
            Config.DISCORD_GUILD_ID,
            since_date
        )

    async def generate_newsletter(self, links_file: str = 'links.md', 
                                output_file: str = Config.NEWSLETTER_FILE):
        """
        Generate newsletter by orchestrating the agent workflow
        
        Args:
            links_file (str): Path to markdown file containing links
            output_file (str): Path to save the final newsletter
        """
        try:
            # Step 1: Collect links
            print("📚 Collecting links...")
            links = self.link_collector.collect_links(links_file)
            
            # Pause for user confirmation
            print("\n🔍 links.md has been generated. Please review and reorder categories if needed.")
            print("Press 'Y' to continue when ready...")
            user_input = input().strip().upper()
            if user_input != 'Y':
                print("❌ Process cancelled by user")
                return
            
            # Step 2: Scrape content
            print("🌐 Scraping content and taking screenshots...")
            articles = await self.content_scraper.scrape_content(links)
            
            # Step 3: Generate newsletter
            print("✍️ Writing newsletter...")
            # Generate newsletter
            newsletter_path = self.content_writer.create_newsletter(output_file)
            
            print(f"✨ Newsletter generated successfully: {newsletter_path}")
            
        except Exception as e:
            print(f"Error generating newsletter: {str(e)}")
            raise

async def main():
    try:
        # Validate configuration
        Config.validate()
        
        # Initialize crew
        crew = UpdateNightCrew()
        
        # Step 1: Collect links from Discord
        print("🤖 Collecting links from Discord...")
        await crew.collect_discord_links()
        
        # Step 2: Generate newsletter
        print("✨ Generating newsletter...")
        await crew.generate_newsletter()
        
        print(f"Newsletter generated successfully at: {Config.NEWSLETTER_FILE}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
