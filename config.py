import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BITBUCKET_USERNAME = os.getenv('BITBUCKET_USERNAME')
BITBUCKET_APP_PASSWORD = os.getenv('BITBUCKET_APP_PASSWORD')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_SLUG = os.getenv('REPO_SLUG')
DAYS_INACTIVE = int(os.getenv('DAYS_INACTIVE'))
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT')
