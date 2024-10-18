import imaplib
import email
import json

def fetch_emails():
    with open('config/email_config.json') as f:
        config = json.load(f)

    mail = imaplib.IMAP4_SSL(config["imap_server"])
    mail.login(config["email"], config["password"])
    mail.select('inbox')

    _, data = mail.search(None, 'ALL')
    mail_ids = data[0].split()

    for mail_id in mail_ids:
        _, msg_data = mail.fetch(mail_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        return msg.get_payload(decode=True).decode()
