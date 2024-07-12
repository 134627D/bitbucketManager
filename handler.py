import os
import boto3
import logging

from bitbucket import find_inactive_branches
from config import SNS_TOPIC_ARN
from utils import setup_logging

sns_client = boto3.client('sns')

def main(event, context):
    log_filename = setup_logging()

    log_content = ""
    try:
        inactive_branches = find_inactive_branches()
        if inactive_branches:
            logging.info("Inactive branches:")
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
        
    sns_topic_arn = SNS_TOPIC_ARN
    message = log_content
    subject = "Inactive Branches Notification"

    try:
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject=subject
        )
        print(f"Message sent to SNS topic {sns_topic_arn}")
    except Exception as e:
        print(f"Error sending message to SNS: {e}")

    return {
        "statusCode": 200,
        "body": "Notification sent"
    }
