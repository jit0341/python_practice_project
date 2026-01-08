## Understand final_automation_brevo_smtp.py
> This document explains the internal working of the automation script.
> Intended for learning, debugging, and client explanation.

## OVERALL FLOW (पहले दिमाग में map बना लें)

यह script 5 काम करता है:

1. SQLite database से data निकालता है


2. Terminal में readable table दिखाता है


3. CSV file बनाता है


4. Brevo SMTP से email भेजता है


5. सब कुछ automation के रूप में करता है



अब line-by-line चलते हैं 👇


---

🔹 IMPORTS (क्यों ज़रूरी हैं)

import sqlite3

👉 SQLite database से connect करने के लिए
(आपका DB = customers.db)


---

import os

👉

folders बनाने के लिए

environment variable (BREVO_SMTP_KEY) पढ़ने के लिए



---

import smtplib

👉 Python का SMTP client
Email भेजने का low-level protocol


---

from email.message import EmailMessage

👉 Email का structure बनाने के लिए
(subject, from, to, body, attachment)


---

from tabulate import tabulate

👉 Terminal में pretty table दिखाने के लिए


---

import pandas as pd

👉

SQL result को DataFrame में बदलने

CSV export करने के लिए



---

🔹 STEP 1: DATABASE + QUERY

conn = sqlite3.connect("data/customers.db")

👉 SQLite database file से connection बनता है
(अगर path गलत होगा → error आएगा)


---

cursor = conn.cursor()

👉 Cursor = SQL commands चलाने का tool


---

query = """
SELECT
    Country,
    COUNT(*) AS Total_Customers
FROM Customers
GROUP BY Country
ORDER BY Total_Customers DESC;
"""

👉 SQL logic:

COUNT(*) → हर country के कितने customers

GROUP BY Country → country wise grouping

ORDER BY DESC → सबसे ज़्यादा वाले ऊपर



---

cursor.execute(query)
rows = cursor.fetchall()

👉

SQL run हुआ

Result Python list of tuples में आया


Example:

[('Mexico', 2), ('Germany', 2), ('UK', 1)]


---

conn.close()

👉 Database connection cleanly बंद
(important habit)


---

🔹 STEP 2: TERMINAL DISPLAY

def green(text):
    return f"\033[92m{text}\033[0m"

👉 ANSI escape code
Terminal में text को green color देता है
(Logic clear है — UI sugar)


---

display_rows = [[c, green(t)] for c, t in rows]

👉 List comprehension:

Country normal

Count green color में



---

print("\n📊 Generated Report:\n")

👉 Output को readable बनाने के लिए


---

print(
    tabulate(
        display_rows,
        headers=["Country", "Total_Customers"],
        tablefmt="grid",
        colalign=("center", "center")
    )
)

👉 Tabulate:

Data → table

grid → box style

colalign → professional look



---

🔹 STEP 3: CSV EXPORT

os.makedirs("reports", exist_ok=True)

👉

reports/ folder बनाता है

पहले से हो तो error नहीं देता



---

csv_path = "reports/country_customer_report.csv"

👉 File path variable
(reuse के लिए — smart)


---

df = pd.DataFrame(rows, columns=["Country", "Total_Customers"])

👉 SQL result → pandas DataFrame


---

df.to_csv(csv_path, index=False)

👉 Clean CSV export
(no index = client-friendly)


---

🔹 STEP 4: EMAIL VIA BREVO SMTP

def send_email(csv_file):

👉 Function बनाया ताकि:

reusable हो

automation clean रहे



---

smtp_key = os.getenv("BREVO_SMTP_KEY")

👉 Environment variable से secret key पढ़ता है
(secure practice)


---

if not smtp_key:
    raise ValueError("BREVO_SMTP_KEY not set")

👉 Defensive programming
Key नहीं है → fail fast


---

msg = EmailMessage()

👉 Email object create


---

msg["Subject"] = "📊 Automated Customer Report (SQL + Python)"
msg["From"] = "jitendrablog6@gmail.com"
msg["To"] = "jitendrablog7@gmail.com"

👉 Email headers
(From वही होना चाहिए जो Brevo में verified है)


---

msg.set_content("Please find the attached customer distribution report.")

👉 Email body (plain text)


---

with open(csv_file, "rb") as f:

👉 CSV binary mode में खोलते हैं
(attachments के लिए जरूरी)


---

msg.add_attachment(
    f.read(),
    maintype="application",
    subtype="octet-stream",
    filename="country_customer_report.csv"
)

👉 Attachment:

raw bytes

generic file type

clean filename



---

with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:

👉 Brevo SMTP server
Port 587 = TLS


---

server.starttls()

👉 Encryption start
(Security mandatory)


---

server.login("9f859b001@smtp-brevo.com", smtp_key)

🔥 MOST IMPORTANT LINE

👉 Brevo rule:

username = something@smtp-brevo.com

password = SMTP key


यह Gmail नहीं है, इसलिए normal email ID नहीं चलेगी


---

server.send_message(msg)

👉 Actual email send


---

print("\n✅ Email sent successfully via Brevo SMTP")

👉 Confirmation


---

🔹 STEP 5: FUNCTION CALL

send_email(csv_path)

👉 Pipeline complete: DB → Report → CSV → Email


---

🧠 अब PostgreSQL कहाँ fit होगा?

Future में सिर्फ यह बदलेगा:

import psycopg2

और यह:

sqlite3.connect(...)

बाकी 80% code SAME रहेगा
👉 यही industry reality है


---

## 🎯 आपने क्या सीख लिया (सबसे ज़रूरी)

✔ SQL aggregation
✔ Python DB automation
✔ CSV generation
✔ SMTP authentication logic
✔ Real-world debugging
✔ Client-explainable workflow

यह portfolio-grade learning है
