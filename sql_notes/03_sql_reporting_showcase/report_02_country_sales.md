
---

# 📊 Report 02 — Country-wise Total Sales

## 🎯 Business Question
Which countries generate the highest total sales revenue?

This report helps businesses understand:
- Revenue contribution by country
- Strong vs weak markets
- Where to focus sales & marketing efforts

---

## 🗂️ Dataset Assumed

**Table:** `customers`

| Column Name     | Description                     |
|-----------------|---------------------------------|
| customer_id     | Unique customer identifier      |
| customer_name   | Customer name                   |
| country         | Customer country                |
| amount          | Purchase / order amount         |

---

## 🧠 SQL Logic Used

- `SUM(amount)` → calculates total sales
- `GROUP BY country` → aggregates country-wise
- Clean, aggregated output (no raw rows)

---

## 🧾 SQL Query

'''sql
SELECT 
    country,
    SUM(amount) AS total_sales
FROM customers
GROUP BY country;


---

📈 Result Snapshot (Example Output)

Country	Total_Sales

Germany	21000
Mexico	23000
Sweden	11000
UK	6000


> 📸 See attached execution screenshot for actual query output




---

💼 Business Value

Identifies top revenue-generating countries

Helps prioritize regional sales strategy

Supports management-level decision making



---

🧑‍💻 Freelance / Real-World Use Cases

Sales performance reports

CRM / customer analytics

Monthly or quarterly business reviews

Executive dashboards



---

📦 Possible Client Deliverables

✔ CSV export (raw aggregated data)

✔ Excel report (formatted + charts)

✔ PDF report (branded, client-ready)



---

✅ Key Takeaway

> Businesses don’t need individual transactions —
they need country-level revenue insights.



This report converts raw customer data into decision-ready sales intelligence.

---

