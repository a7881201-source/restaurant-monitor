from playwright.sync_api import sync_playwright
import os
import smtplib
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://tw.eztable.com/restaurant/17768",
        wait_until="networkidle"
    )

    title = page.title()

    content = page.content()[:5000]

    browser.close()

msg = MIMEText(content)

msg["Subject"] = f"Playwright Test - {title}"
msg["From"] = EMAIL
msg["To"] = EMAIL

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("sent")
