import sqlite3
import pandas as pd
import os
from tabulate import tabulate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- Step 1: Data Extraction (Your Original Code) ---
conn = sqlite3.connect("data/customers.db")
query = """
SELECT country, COUNT(*) AS Total_Customers 
FROM Customers 
GROUP BY country 
ORDER BY Total_Customers DESC;
"""
df = pd.read_sql_query(query, conn)
conn.close()

# --- Step 2: Professional Formatting ---
def green(text):
    return f"\033[92m{text}\033[0m"

display_rows = [[row['country'], green(row['Total_Customers'])] for index, row in df.iterrows()]
table_output = tabulate(display_rows, headers=["country", "Total_Customers"], tablefmt="grid", colalign=("center", "center"))

print("\n📊 Generated Report:")
print(table_output)

# CSV Export
csv_file = "reports/country_customer_report.csv"
df.to_csv(csv_file, index=False)

# --- Step 3: Email Automation Function ---
def send_email():
    sender = "jitendrablog6@gmail.com"      # अपना ईमेल यहाँ लिखें
    receiver = "jitendrablog7@gmail.com"  # क्लाइंट का ईमेल यहाँ लिखें


    app_password = os.getenv("EMAIL_APP_PASSWORD") # 16-digit Google App Password

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "📊 Automated Customer Report (SQL + Python)"

    body = "Please find the attached customer distribution report generated from the database."
    msg.attach(MIMEText(body, 'plain'))

    # Attachment logic
    with open(csv_file, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {csv_file}")
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.send_message(msg)
        print("\n✅ Email sent successfully to the client!")
    except Exception as e:
        print(f"\n❌ Email failed: {e}")

# ईमेल भेजने के लिए इस लाइन को अन-कमेंट करें
send_email() 

