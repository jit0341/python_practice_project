# SQL Lesson 2: DISTINCT, COUNT, LIMIT, MIN, MAX

**Platform:** W3Schools Try SQL  
**Table Used:** Customers  

This lesson focuses on filtering result sets and extracting summary information.

---

## DISTINCT

```sql
SELECT DISTINCT Country FROM Customers;
Returns unique country values.
COUNT (All Rows)

Sql
SELECT COUNT(*) FROM Customers;
Counts total number of records.
COUNT with DISTINCT

Sql
SELECT COUNT(DISTINCT Country) FROM Customers;
Counts unique countries served.
MIN / MAX

Sql
SELECT MIN(CustomerID), MAX(CustomerID) FROM Customers;
Finds boundary values in a column.
LIMIT vs TOP (Important Note)
W3Schools uses Microsoft SQL Server.
LIMIT → MySQL / PostgreSQL
TOP → SQL Server
Example:

Sql
SELECT TOP 5 * FROM Customers;

