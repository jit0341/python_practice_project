# 📊 Report 01 — Country-wise Customer Count

## Client Question
How many customers are there in each country?

---

## SQL Query

```sql
SELECT 
    Country,
    COUNT(*) AS Total_Customers
FROM Customers
GROUP BY Country;

![SQL REPORTING — STRUCTURED SHOWCASE](screenshots/country_count_report.png)
