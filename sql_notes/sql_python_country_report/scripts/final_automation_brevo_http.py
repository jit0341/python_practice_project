import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587
SMTP_USER = "9f859b001@smtp-brevo.com"
SMTP_PASS = os.getenv("BREVO_SMTP_KEY")

FROM_EMAIL = "jitendrablog6@gmail.com"   # any name
TO_EMAIL = "jitendrblog7@gmail.com"

csv_file = "reports/country_customer_report.csv"

msg = MIMEMultipart()
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = "📊 Automated Customer Report"

msg.attach(MIMEText(
    "Please find the attached customer report generated automatically.",
    "plain"
))

with open(csv_file, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f'attachment; filename="{csv_file}"'
    )
    msg.attach(part)

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
    print("✅ Email sent successfully via Brevo!")
except Exception as e:
    print("❌ Email failed:", e)
