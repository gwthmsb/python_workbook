from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import ClassVar
from loguru import logger
from sys import stdout

from context import Context

class Config(BaseSettings):
    app_name: str = "fastAPIContext"

    model_config = SettingsConfigDict(env_file="config.env")
    context: ClassVar[Context] = Context(**{"APP_NAME": app_name})

    def config_to_add_logs(self):
        return {
            "request_id": self.context.get_request_id(),
        }

@lru_cache 
def get_config():
    return Config()


def configure_logger():
    logger.remove(0)

    # You can change the 'extra' to print only what you want
    # Eg: format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {extra[request_id]} | {message}"
    # This will print only request_id instead of all the configurations
    logger.add(sink=stdout, level="INFO", 
               format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {extra} | {message}", 
               serialize=False, 
               backtrace=True)
