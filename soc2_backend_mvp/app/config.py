from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    ENV: str = "dev"
    API_NAME: str = "SOC2 Policy Pack API"
    API_VERSION: str = "0.1.0"

    MONGO_URI: str = Field(default="mongodb://localhost:27017")
    MONGO_DB: str = Field(default="soc2_saas")

    JWT_SECRET: str = Field(default="CHANGE_ME")
    JWT_ALGORITHM: str = Field(default="HS256")
    JWT_EXPIRES_MINUTES: int = Field(default=60 * 24 * 3)  # 3 days

    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.5-flash"
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"

    CORS_ORIGINS: str = "http://localhost:4200"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
