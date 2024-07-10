import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import DAYS_INACTIVE, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_RECIPIENT, EMAIL_SUBJECT, REPO_OWNER, REPO_SLUG

def send_email(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            log_content = file.read()

        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = f'{EMAIL_SUBJECT}: {REPO_OWNER}/{REPO_SLUG} in {DAYS_INACTIVE} Days'

        msg.attach(MIMEText(log_content, 'plain'))

        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_HOST_USER, EMAIL_RECIPIENT, text)
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
