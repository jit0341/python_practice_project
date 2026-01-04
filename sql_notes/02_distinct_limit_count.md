# SQL Lesson 2: DISTINCT, COUNT, LIMIT, MIN, MAX

Platform: W3Schools Try SQL  
Table Used: Customers

This lesson focuses on filtering result sets
and extracting summary information from data.
## COUNT()

```sql
SELECT COUNT(*) FROM Customers;
---

## 🧪 STEP 3 — COUNT with DISTINCT (countries count)

Run:

```sql
SELECT COUNT(DISTINCT Country)
FROM Customers;
