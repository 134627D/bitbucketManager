import logging
from bitbucket import find_inactive_branches
from emailer import send_email
from utils import setup_logging

if __name__ == "__main__":
    log_filename = setup_logging()

    try:
        inactive_branches = find_inactive_branches()
        if inactive_branches:
            logging.info("Inactive branches:")
            for branch in inactive_branches:
                logging.info(f"Branch: {branch['name']}, Last Commit Date: {branch['last_commit_date']}, Creator: {branch['creator']}")
        else:
            logging.info("No inactive branches found.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")

    # Send the log file via email
    send_email(log_filename)
