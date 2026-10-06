from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Gemma LLM Service"
    API_V1_STR: str = "/api/v1"
    GEMINI_API_KEY: str
    DEFAULT_GEMMA_MODEL: str = "gemma-4-26b-a4b-it"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()