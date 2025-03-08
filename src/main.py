import os
from agents.link_collector import LinkCollectorAgent
from agents.content_scraper import ContentScraperAgent
from agents.content_writer import ContentWriterAgent
from crewai import Crew, Process
from dotenv import load_dotenv

load_dotenv()

class UpdateNightCrew:
    def __init__(self):
        # Initialize agents
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
        
    def generate_newsletter(self, links_file: str, output_file: str):
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
            
            # Step 2: Scrape content
            print("🌐 Scraping content and taking screenshots...")
            articles = self.content_scraper.scrape_content(links)
            
            # Step 3: Generate newsletter
            print("✍️ Writing newsletter...")
            newsletter_path = self.content_writer.create_newsletter(
                articles,
                output_file
            )
            
            print(f"✨ Newsletter generated successfully: {newsletter_path}")
            
        except Exception as e:
            print(f"Error generating newsletter: {str(e)}")
            raise

if __name__ == "__main__":
    # Example usage
    crew = UpdateNightCrew()
    crew.generate_newsletter(
        "links.md",
        "output/newsletter.md"
    )
