from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from the .env file.
    """

    APP_NAME: str = "Ambient Clinical Scribe"
    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    DATABASE_URL: str

    GEMINI_API_KEY: str

    UPLOAD_DIRECTORY: str = "uploads"
    MAX_AUDIO_SIZE_MB: int = 100

    LOG_LEVEL: str = "INFO"

    WHISPER_MODEL: str = "whisper-1"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """
    return Settings()


settings = get_settings()