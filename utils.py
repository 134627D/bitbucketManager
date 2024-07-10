import os
from datetime import datetime
import logging

def setup_logging(log_directory='./logs'):
    # Ensure the logs directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Set up logging with a timestamp in the file name
    log_filename = os.path.join(log_directory, f'inactive_branches_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

    return log_filename
