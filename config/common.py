import logging
import os


class Config:
    LOG_LEVEL = logging.DEBUG
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    GOOGLE_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
    CSE_KEY = os.getenv('SEARCH_ENGINE_ID')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME')
