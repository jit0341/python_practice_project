# 📊 Country-wise Customer Analytics Report (SQL + Python)

This project demonstrates a complete, client-ready data reporting workflow
using **SQL, Python, and SQLite**.

The goal is not just to write queries,
but to convert raw database data into **usable business reports**.

---

## 🎯 Client Question

> How many customers are there in each country, and how is the market distributed?

---

## 🧠 Solution Overview

This automation performs:

- SQL aggregation (GROUP BY + COUNT)
- Clean tabular terminal output
- CSV export (Excel / Google Sheets ready)
- Visual analytics (Bar chart + Pie chart)
- Timestamped execution for audit clarity

---

## 🛠️ Tech Stack

- SQLite (Database)
- SQL (Aggregation & reporting)
- Python
  - pandas
  - matplotlib
  - tabulate

---

## 📁 Project Structure
sql_python_country_report/ ├── data/ │   └── customers.db ├── reports/ │   ├── country_customer_report.csv │   ├── customer_distribution.png │   └── customer_multiple_charts.png ├── scripts/ │   ├── generate_report.py │   └── generate_country_report.py └── README.md

---

## ▶️ How to Run

```bash
cd scripts
python generate_country_report.py
```
🖥️ Terminal Output Preview
![Terminal Output](screenshots/terminal_output.png)

📄 CSV Report Preview
![CSV Report](screenshots/csv_preview.png)

📊 Charts Preview
![Double Charts](screenshots/charts_preview.png)

📦 Deliverables
```md
📸 Execution & Output Proof  
👉 [View Screenshots](screenshots.md)

✅ Terminal summary
✅ CSV report
✅ Bar chart (comparison)
✅ Pie chart (market share)

💼 Freelance Use Case

This type of report is commonly used for:
CRM analysis
Sales distribution reports
Country-wise business insights
Client-ready Excel & presentation data

## ✅ Verification Steps (Client Proof)

After running the report script, outputs can be independently verified
using standard CLI commands:

```bash
# List generated reports with size and timestamp
ls -lh reports/

# Verify file metadata (creation & modification time)
stat reports/*.png
stat reports/*.csv

# Confirm file types
file reports/*

# Validate CSV content
wc -l reports/country_customer_report.csv
head reports/country_customer_report.csv

# Optional integrity check
sha256sum reports/country_customer_report.csv

These steps ensure:
Reports are auto-generated (no manual editing)
Files are reproducible and auditable
Output integrity is verifiable by any technical reviewer
