import requests
import os
import smtplib
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

url = "https://tw.eztable.com/restaurant/17768"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

html = response.text[:2000]

msg = MIMEText(html)

msg["Subject"] = "EZTABLE測試"
msg["From"] = EMAIL
msg["To"] = EMAIL

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("Mail Sent")
`
