import os
import logging

from bitbucket import find_inactive_branches
from emailer import send_email
from utils import setup_logging

def main(event, context):
    log_filename = setup_logging()

    try:
        inactive_branches = find_inactive_branches()
        if inactive_branches:
            logging.info("Inactive branches:")
            log_content = ""
            for branch in inactive_branches:
                log_entry = f"Branch: {branch['name']}, Last Commit Date: {branch['last_commit_date']}, Creator: {branch['creator']}"
                logging.info(log_entry)
                log_content += log_entry + "\n"
        else:
            log_content = "No inactive branches found."
            logging.info(log_content)
    except Exception as e:
        log_content = f"Error occurred: {e}"
        logging.error(log_content)

    send_email(log_content)

    return {
        "statusCode": 200,
        "body": log_content
    }
