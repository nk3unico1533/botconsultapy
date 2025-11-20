import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOG_LEVEL = "INFO"
