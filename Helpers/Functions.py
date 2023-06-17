from simplegmail import Gmail
from Credentials.credentials import GMAIL

class Functions:
    def write_email(recipient, subject, body):
        gmail = Gmail() # will open a browser window to ask you to log in and authenticate

        params = {
        "to": recipient,
        "sender": GMAIL,
        "subject": subject,
        "msg_html": body,
        "msg_plain": body,
        "signature": True  # use my account signature
        }
        message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)
        print('Email sent!')
            