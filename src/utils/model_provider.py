"""
Model provider utility for handling different AI model providers.
Supports OpenAI and Gemini models.
"""
from typing import Optional, Dict, Any
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from config import Config
from utils.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger('ModelProvider')

class ModelProvider:
    """Factory class for creating language models based on configuration."""

    @staticmethod
    def get_model(model_name: Optional[str] = None, **kwargs) -> Any:
        """
        Get a language model based on the configured provider.

        Args:
            model_name: Optional model name to use. If not provided, uses default for provider.
            **kwargs: Additional arguments to pass to the model constructor.

        Returns:
            A language model instance (ChatOpenAI or ChatGoogleGenerativeAI)

        Raises:
            ValueError: If the configured provider is invalid
        """
        provider = Config.AI_PROVIDER

        if provider == 'openai':
            return ModelProvider._get_openai_model(model_name, **kwargs)
        elif provider == 'gemini':
            return ModelProvider._get_gemini_model(model_name, **kwargs)
        else:
            raise ValueError(f"Invalid AI provider: {provider}")

    @staticmethod
    def _get_openai_model(model_name: Optional[str] = None, **kwargs) -> ChatOpenAI:
        """
        Get an OpenAI model.

        Args:
            model_name: Optional model name to use. Defaults to 'gpt-4o-mini'.
            **kwargs: Additional arguments to pass to ChatOpenAI constructor.

        Returns:
            ChatOpenAI instance
        """
        if model_name is None:
            model_name = "gpt-4o-mini"

        logger.debug(f"Creating OpenAI model: {model_name}")
        return ChatOpenAI(
            model_name=model_name,
            api_key=Config.OPENAI_API_KEY,
            **kwargs
        )

    @staticmethod
    def _get_gemini_model(model_name: Optional[str] = None, **kwargs) -> ChatGoogleGenerativeAI:
        """
        Get a Gemini model.

        Args:
            model_name: Optional model name to use. Defaults to 'gemini-2.5-flash-preview-04-17'.
            **kwargs: Additional arguments to pass to ChatGoogleGenerativeAI constructor.

        Returns:
            ChatGoogleGenerativeAI instance
        """
        if model_name is None:
            model_name = "gemini-2.5-flash-preview-04-17"

        logger.debug(f"Creating Gemini model: {model_name}")
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=Config.GEMINI_API_KEY,
            **kwargs
        )

    @staticmethod
    def invoke_with_prompt(
        prompt_template: str,
        input_variables: Dict[str, Any],
        model_name: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Invoke a model with a prompt template and input variables.

        Args:
            prompt_template: The prompt template string
            input_variables: Dictionary of variables to format the prompt with
            model_name: Optional model name to use
            **kwargs: Additional arguments to pass to the model constructor

        Returns:
            The model's response content as a string
        """
        prompt = PromptTemplate(
            input_variables=list(input_variables.keys()),
            template=prompt_template
        )

        model = ModelProvider.get_model(model_name, **kwargs)
        result = model.invoke(prompt.format(**input_variables))

        return result.content
