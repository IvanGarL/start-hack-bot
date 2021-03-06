"""Bot config."""
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, '.env'))


class Config:
    """configuration variables."""

    # General Config
    SLACK_OAUTH_ACCESS_TOKEN = environ.get('SLACK_OAUTH_ACCESS_TOKEN')
    SIGNING_SECRET = environ.get('SIGNING_SECRET')