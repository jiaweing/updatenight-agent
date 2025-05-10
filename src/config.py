from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Discord configuration
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    DISCORD_GUILD_ID = os.getenv('DISCORD_GUILD_ID')

    # Date configuration
    COLLECT_SINCE_DATE = os.getenv(
        'COLLECT_SINCE_DATE',
        datetime.now(timezone.utc).strftime('%Y-%m-%d')
    )

    # AI Model configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'openai').lower()  # 'openai' or 'gemini'

    # Output configuration
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'output')
    NEWSLETTER_FILE = os.path.join(OUTPUT_DIR, 'newsletter.md')

    # Crawler configuration
    HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
    TIMEOUT = int(os.getenv('TIMEOUT', '30'))

    @classmethod
    def validate(cls) -> bool:
        """Validate required configuration"""
        required_vars = [
            ('DISCORD_TOKEN', cls.DISCORD_TOKEN),
            ('DISCORD_GUILD_ID', cls.DISCORD_GUILD_ID),
        ]

        # Add the appropriate API key requirement based on the selected provider
        if cls.AI_PROVIDER == 'openai':
            required_vars.append(('OPENAI_API_KEY', cls.OPENAI_API_KEY))
        elif cls.AI_PROVIDER == 'gemini':
            required_vars.append(('GEMINI_API_KEY', cls.GEMINI_API_KEY))
        else:
            raise ValueError(
                f"Invalid AI_PROVIDER: {cls.AI_PROVIDER}. Must be 'openai' or 'gemini'"
            )

        missing = [var[0] for var in required_vars if not var[1]]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

        try:
            datetime.strptime(cls.COLLECT_SINCE_DATE, '%Y-%m-%d')
        except ValueError:
            raise ValueError(
                "Invalid COLLECT_SINCE_DATE format. Use YYYY-MM-DD"
            )

        return True
