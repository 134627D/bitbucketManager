import os
import requests
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import logging

# Ensure the logs directory exists
log_directory = './logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up logging with a timestamp in the file name
log_filename = os.path.join(log_directory, f'inactive_branches_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Load environment variables from .env file
load_dotenv()

# Replace with your Bitbucket credentials and repository details
BITBUCKET_USERNAME = os.getenv('BITBUCKET_USERNAME')
BITBUCKET_APP_PASSWORD = os.getenv('BITBUCKET_APP_PASSWORD')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_SLUG = os.getenv('REPO_SLUG')
DAYS_INACTIVE = int(os.getenv('DAYS_INACTIVE'))

# Calculate the cutoff date for inactivity
cutoff_date = datetime.now(timezone.utc) - timedelta(days=DAYS_INACTIVE)

def get_branches():
    url = f'https://api.bitbucket.org/2.0/repositories/{REPO_OWNER}/{REPO_SLUG}/refs/branches'
    response = requests.get(url, auth=(BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD))
    response.raise_for_status()
    return response.json()

def get_commit_date_and_author(commit_hash):
    url = f'https://api.bitbucket.org/2.0/repositories/{REPO_OWNER}/{REPO_SLUG}/commit/{commit_hash}'
    response = requests.get(url, auth=(BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD))
    response.raise_for_status()
    commit_data = response.json()
    commit_date = commit_data['date']
    author = commit_data['author']
    
    # Check if author has 'user' field
    if 'user' in author:
        author_name = author['user']['display_name']
    else:
        author_name = author['raw']  # Use the raw author name if 'user' is not available
    
    return commit_date, author_name

def find_inactive_branches():
    branches = get_branches()
    inactive_branches = []
    
    for branch in branches['values']:
        commit_date, author = get_commit_date_and_author(branch['target']['hash'])
        commit_datetime = datetime.fromisoformat(commit_date.replace('Z', '+00:00'))
        
        if commit_datetime < cutoff_date:
            inactive_branches.append({
                'name': branch['name'],
                'last_commit_date': commit_datetime,
                'updated_by': author
            })
    
    return inactive_branches

if __name__ == "__main__":
    try:
        inactive_branches = find_inactive_branches()
        if inactive_branches:
            logging.info("Inactive branches:")
            for branch in inactive_branches:
                logging.info(f"Branch: {branch['name']}, Last Commit Date: {branch['last_commit_date']}, Updated By: {branch['updated_by']}")
        else:
            logging.info("No inactive branches found.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
