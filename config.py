import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BITBUCKET_USERNAME = os.getenv('BITBUCKET_USERNAME')
BITBUCKET_APP_PASSWORD = os.getenv('BITBUCKET_APP_PASSWORD')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_SLUG = os.getenv('REPO_SLUG')
DAYS_INACTIVE = int(os.getenv('DAYS_INACTIVE'))
SNS_TOPIC_ARN = os.getenv('SNS_TOPIC_ARN')
