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

![SQL Output — Country-wise Customer Count](screenshots/report_01_country_count.png)
