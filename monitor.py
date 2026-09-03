import os
import smtplib
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

msg = MIMEText("測試通知成功")
msg["Subject"] = "島語監控測試"
msg["From"] = EMAIL
msg["To"] = EMAIL

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("Mail sent successfully")
