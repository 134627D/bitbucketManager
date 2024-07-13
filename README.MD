# Inactive Branches Detector

This project is to watch inactive branches on Bitbucket of the NGPH project. It involves `Python`, `AWS Lambda`, `CloudWatch` and `Simple Notification Service`. The ideas under the hood is to call Bitbucket APIs to detect if there is a branch turning inactive for more than 5 days. AWS CloudWatch will run a scheduled task (5 days interval) to trigger the Lambda function mentioned before and the results will be sent through the Simple Notification Service to the target emails. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone the project from [here](https://github.com/134627D/bitbucketManager). Before running the project locally, make sure Node.js is installed and AWS credentials are setup correctly.

- First, ensure you have Node.js installed. Then, install the Serverless Framework globally.
- Install the Serverless Framework: `npm install -g serverless`
- Run `npm install` to add all serverless dependencies
- Install Python Dependencies: `pip install -r requirements.txt`


## Usage

- First, activate the virtual environment: `Source venv/Scripts/activate`
- Run it locally: `Python hander.py` or 
- Check it out on AWS dev: `Lambda > Functions > bitbucket-inactive-branches-dev-main > Test`