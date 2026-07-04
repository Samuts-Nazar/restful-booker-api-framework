from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    base_url: str = Field(alias="BASE_URL")

    username: str = Field(alias="USERNAME")
    password: str = Field(alias="PASSWORD")

    db_url: str = Field(alias="DB_URL")
    db_username: str = Field(alias="DB_USERNAME")
    db_password: str = Field(alias="DB_PASSWORD")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()