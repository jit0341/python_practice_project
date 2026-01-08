📊 Automated Customer Country Report (SQL + Python)

📌 Project Overview

This project automatically generates a customer distribution report by country from a relational database using SQL + Python, exports the results as a CSV, displays a formatted table in the terminal, and optionally sends the report via email.

This repository is designed as a learning + portfolio project, demonstrating real-world data automation workflows rather than production-scale email infrastructure.


---

🧠 Problem Statement

Clients often need periodic summary reports (daily/weekly/monthly) from their databases, such as:

Customer distribution by country

Sales count by region

User analytics summaries


Manual extraction is error-prone and time-consuming. This project solves that by automating the full pipeline.


---

🏗 Architecture Overview

SQLite / PostgreSQL
        ↓ (SQL Query)
     Python Script
        ↓
Formatted Terminal Table (tabulate)
        ↓
   CSV Report Export
        ↓
 Optional Email Delivery (SMTP)


---

🧩 Features

✅ SQL aggregation using GROUP BY

✅ Clean terminal report with colored output

✅ CSV export for Excel / Google Sheets

✅ Email automation with attachment (optional)

✅ Environment-variable–based secret handling



---

🛠 Tech Stack

Database: SQLite (current) / PostgreSQL (planned)

Language: Python 3

Libraries:

sqlite3

pandas

tabulate

smtplib

email.message




---

📂 Project Structure

sql_python_country_report/
│
├── data/
│   └── customers.db
│
├── reports/
│   └── country_customer_report.csv
│
├── scripts/
│   └── final_automation_brevo_smtp.py
│
└── README.md


---

▶️ How It Works

Step 1: SQL Query

The script runs the following query:

SELECT
    Country,
    COUNT(*) AS Total_Customers
FROM Customers
GROUP BY Country
ORDER BY Total_Customers DESC;


---

Step 2: Terminal Display

Results are displayed in a clean grid format using tabulate, with color highlighting for readability.


---

Step 3: CSV Export

The result set is exported as:

reports/country_customer_report.csv

This file can be directly opened in Excel or Google Sheets.


---

Step 4: Email Automation (Optional)

If SMTP credentials are configured via environment variables, the CSV report is emailed automatically as an attachment.

export BREVO_SMTP_KEY="<your_smtp_key>"
python scripts/final_automation_brevo_smtp.py


---

⚠️ Important Notes (Client Transparency)

This project uses freemail domains (Gmail/Outlook) for demonstration.

Freemail domains often fail DMARC / SPF checks in production email systems.

Email delivery may be inconsistent without a custom domain.


> 📌 This is expected behavior and not a code defect.




---

✅ What This Project Demonstrates

Real-world SQL reporting logic

Python automation skills

Clean separation of logic (query → report → delivery)

Secure handling of secrets via environment variables

Awareness of production constraints



---

🚀 Future Enhancements

PostgreSQL support (planned)

Scheduler integration (cron / Airflow)

Email ON/OFF config flag

HTML email templates

Cloud deployment



---

👤 Author

Jitendra Bharti
Python | SQL | Automation Enthusiast


---

📄 License

This project is open for learning and portfolio demonstration purposes.

