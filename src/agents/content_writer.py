from crewai import Agent
from typing import List, Dict
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import markdown

class ContentWriterAgent:
    def __init__(self, samples_dir: str = "samples"):
        self.agent = Agent(
            role='Content Writer',
            goal='Write informative newsletter content in Update Night style',
            backstory="""You are a specialized agent that analyzes content and writes
            engaging summaries in the style of Update Night newsletter. You understand
            technical concepts and can highlight key insights while maintaining a
            consistent tone and format."""
        )
        self.samples_dir = samples_dir
        self.style_examples = self.load_style_examples()
        
    def load_style_examples(self) -> List[str]:
        """Load and parse writing style examples from samples directory"""
        examples = []
        if not os.path.exists(self.samples_dir):
            return examples
            
        for file in os.listdir(self.samples_dir):
            if file.endswith('.md'):
                with open(os.path.join(self.samples_dir, file), 'r') as f:
                    examples.append(f.read())
        return examples
        
    def create_section(self, article_data: Dict) -> str:
        """
        Create a newsletter section for a single article
        
        Args:
            article_data (Dict): Dictionary containing article content and metadata
            
        Returns:
            str: Formatted markdown section
        """
        # Extract key information
        title = article_data.get('title', '')
        url = article_data.get('url', '')
        content = article_data.get('content', '')
        screenshot_path = article_data.get('screenshot_path', '')
        
        # Create relative path for screenshot
        if screenshot_path:
            rel_path = os.path.relpath(
                screenshot_path, 
                os.path.dirname(self.output_file)
            )
        
        # Format markdown section
        section = f"""
## {title}

![Screenshot]({rel_path})

{self._write_summary(content)}

[Read more]({url})
"""
        return section
        
    def _write_summary(self, content: str) -> str:
        """Generate summary with key insights based on content"""
        # Split content into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(content)
        
        # Create summary prompt template
        prompt = PromptTemplate(
            input_variables=["content", "style_examples"],
            template="""
            You are writing a section for the Update Night newsletter. Using the following content:
            
            {content}
            
            Write a concise summary that highlights:
            1. Key points and announcements
            2. Why it matters for developers/tech industry
            3. Important technical details or impacts
            
            Match the writing style from these examples:
            {style_examples}
            
            Focus on being informative yet engaging, technical yet accessible.
            Keep the summary brief but impactful.
            """
        )
        
        # Use OpenAI to generate summary
        llm = OpenAI()
        summary = llm.predict(
            prompt.format(
                content="\n".join(chunks),
                style_examples="\n---\n".join(self.style_examples[:2])  # Use first 2 examples
            )
        )
        
        return summary.strip()
        
    def create_newsletter(self, articles: List[Dict], output_file: str) -> str:
        """
        Create complete newsletter with all articles
        
        Args:
            articles (List[Dict]): List of article data
            output_file (str): Path to save the newsletter
            
        Returns:
            str: Path to generated newsletter file
        """
        self.output_file = output_file
        
        # Create newsletter content
        sections = [self.create_section(article) for article in articles]
        content = "\n\n".join(sections)
        
        # Add header
        newsletter = f"""# Update Night

_Your weekly dose of tech updates_

{content}
"""
        
        # Save newsletter
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(newsletter)
            
        return output_file
