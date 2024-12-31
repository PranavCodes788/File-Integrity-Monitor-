import logging
import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, from_email, to_email, smtp_server, smtp_port):

        # Sends alert email using SMPT server settings
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # If your SMTP server requires login, you'd do:
            # server.login('username', 'password')
            server.sendmail(from_email, [to_email], msg.as_string())
        logging.info(f"Alert email sent to {to_email} with subject: {subject}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")
