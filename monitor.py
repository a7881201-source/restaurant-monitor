import requests
import os
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

EMAIL = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

url = "https://tw.eztable.com/restaurant/17768"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(response.text, "html.parser")

result = []

result.append("TITLE:")
result.append(soup.title.text if soup.title else "No Title")

result.append("\nLINKS:")

for link in soup.find_all("a")[:50]:
    href = link.get("href")
    if href:
        result.append(href)

mail_text = "\n".join(result)

msg = MIMEText(mail_text)

msg["Subject"] = "EZTABLE Links Test"
msg["From"] = EMAIL
msg["To"] = EMAIL

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("Mail Sent")
