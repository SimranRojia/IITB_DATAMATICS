import smtplib
from email.mime.text import MIMEText
import json

def send_notification(subject, body):
    with open('config/email_config.json') as f:
        config = json.load(f)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["email"]
    msg["To"] = "support-team@example.com"

    with smtplib.SMTP(config["smtp_server"], 587) as server:
        server.starttls()
        server.login(config["email"], config["password"])
        server.sendmail(config["email"], "support-team@example.com", msg.as_string())
