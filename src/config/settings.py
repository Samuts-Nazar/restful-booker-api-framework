from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    auth_url: str = Field(alias="AUTH_URL")
    booking_url: str = Field(alias="BOOKING_URL")
    room_url: str = Field(alias="ROOM_URL")
    branding_url: str = Field(alias="BRANDING_URL")
    message_url: str = Field(alias="MESSAGE_URL")
    report_url: str = Field(alias="REPORT_URL")
    assets_url: str = Field(alias="ASSETS_URL")

    default_timeout: int = 10

    username: str = Field(alias="API_USERNAME")
    password: str = Field(alias="API_PASSWORD")

    db_url: str = Field(alias="DB_URL")
    db_username: str = Field(alias="DB_USERNAME")
    db_password: str = Field(alias="DB_PASSWORD")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
default_timeout: int = 10