from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import ClassVar

from context import Context

class Config(BaseSettings):
    app_name: str = "fastAPIContext"

    model_config = SettingsConfigDict(env_file="config.env")
    context: ClassVar[Context] = Context(**{"APP_NAME": app_name})

@lru_cache 
def get_config():
    return Config()