"""
AI-based categorization for articles using Google's Gemini model.
"""
from utils.logging_config import setup_logging, get_logger
from utils.model_provider import ModelProvider

# Setup logging
setup_logging()
logger = get_logger('AICategorizer')

class AICategorizer:
    """
    Categorizes articles using Google's Gemini model.
    """

    # Standard categories used in the newsletter
    CATEGORIES = [
        "The Big Picture",
        "Under the Radar",
        "TrAIn of Thought",
        "The Grid",
        "The Spotlight"
    ]

    # Category descriptions for better AI understanding
    CATEGORY_DESCRIPTIONS = {
        "The Big Picture": "Major announcements, launches, breaking news, significant updates in tech",
        "Under the Radar": "Experimental features, insights, analyses, lesser-known but interesting developments",
        "TrAIn of Thought": "AI/ML developments, models, research, generative AI, LLMs, neural networks",
        "The Grid": "Design systems, UI/UX, component libraries, CSS frameworks, visual tools, frontend",
        "The Spotlight": "Open source projects, tools, resources, libraries, frameworks, utilities"
    }

    def __init__(self, model_name: str = None):
        """
        Initialize the AI categorizer.

        Args:
            model_name: The Gemini model to use for categorization (default: None, uses ModelProvider default)
        """
        self.model_name = model_name
        self._setup_model()

    def _setup_model(self):
        """Set up the Gemini model using ModelProvider."""
        try:
            # Use the existing ModelProvider to get a Gemini model
            self.model = ModelProvider.get_model(self.model_name)
            logger.info(f"✅ Successfully initialized Gemini model: {self.model_name}")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Gemini model: {str(e)}")
            raise

    def categorize(self, content: str) -> str:
        """
        Categorize an article based on its content.

        Args:
            content: The article content to categorize

        Returns:
            The category name (one of the standard categories)
        """
        try:
            # Create a prompt that explains the task and categories
            prompt = self._create_categorization_prompt(content)

            # Generate response from Gemini using Langchain
            response = self.model.invoke(prompt)

            # Extract the category from the response
            category = self._extract_category(response.content)
            logger.info(f"🏷️ AI categorized content as: {category}")

            return category
        except Exception as e:
            logger.error(f"❌ Error during AI categorization: {str(e)}")
            # Default to "Under the Radar" if categorization fails
            return "Under the Radar"

    def _create_categorization_prompt(self, content: str) -> str:
        """
        Create a prompt for the Gemini model to categorize the content.

        Args:
            content: The article content to categorize

        Returns:
            A formatted prompt string
        """
        # Truncate content if it's too long (Gemini has token limits)
        max_content_length = 10000
        if len(content) > max_content_length:
            content = content[:max_content_length] + "..."

        # Build the category descriptions part of the prompt
        category_descriptions = "\n".join([
            f"- {category}: {description}"
            for category, description in self.CATEGORY_DESCRIPTIONS.items()
        ])

        # Create the full prompt
        prompt = f"""
        You are an expert content categorizer for a tech newsletter called "Update Night".

        Your task is to categorize the following article into exactly one of these categories:
        {category_descriptions}

        Here is the article content:
        ---
        {content}
        ---

        Analyze the content and determine which single category it fits best.
        Consider the topic, focus, and technical domain of the article.

        Return ONLY the category name, nothing else. For example: "The Grid"
        """

        return prompt

    def _extract_category(self, response_text: str) -> str:
        """
        Extract the category from the model's response.

        Args:
            response_text: The raw text response from the model

        Returns:
            The extracted category, or "Under the Radar" if no valid category is found
        """
        # Clean up the response text
        clean_response = response_text.strip().strip('"').strip("'")

        # Check if the response exactly matches one of our categories
        for category in self.CATEGORIES:
            if category.lower() == clean_response.lower():
                return category

        # If no exact match, look for partial matches
        for category in self.CATEGORIES:
            if category.lower() in clean_response.lower():
                return category

        # Default to "Under the Radar" if no match is found
        logger.warning(f"⚠️ Could not extract valid category from response: '{response_text}'")
        return "Under the Radar"
