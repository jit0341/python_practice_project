# SQL Lesson 2: DISTINCT, COUNT, LIMIT, MIN, MAX

**Platform:** W3Schools Try SQL  
**Table Used:** Customers  

This lesson focuses on filtering result sets and extracting summary information commonly used in reporting and analysis.

---

## DISTINCT
Returns unique country values from the table.

```sql
SELECT DISTINCT Country
FROM Customers;


---

COUNT (All Rows)

Counts the total number of records in the table.

SELECT COUNT(*) AS Total_Records
FROM Customers;


---

COUNT with DISTINCT

Counts the number of unique countries served.

SELECT COUNT(DISTINCT Country) AS Unique_Countries
FROM Customers;


---

MIN / MAX

Finds the minimum and maximum CustomerID values.

SELECT 
    MIN(CustomerID) AS Min_CustomerID,
    MAX(CustomerID) AS Max_CustomerID
FROM Customers;


---

TOP (SQL Server)

Returns a limited number of rows.

> Note:
W3Schools uses Microsoft SQL Server
TOP → SQL Server
LIMIT → MySQL / PostgreSQL



SELECT TOP 5 *
FROM Customers;


---

Result Preview

Representative outputs shown (queries executed individually in W3Schools).

![Combined Query Result](/screenshots/combined.png)


---

Business Value

Helps analyze data distribution

Useful for reporting and summaries

Supports decision-making with clean metrics



---

Deliverables

Clean query outputs

Client-readable results

Ready for CSV / Excel / PDF reporting


---
