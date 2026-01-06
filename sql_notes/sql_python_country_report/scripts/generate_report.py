import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("data/customers.db")

# ===============================
# QUERY 1: All countries
# ===============================
"""
SELECT 
    Country,
    COUNT(*) AS Total_Customers
FROM Customers
GROUP BY Country
ORDER BY Total_Customers DESC;
"""

# ===============================
# QUERY 2: Countries with > 5 customers (ACTIVE)
# ===============================
query = """
SELECT 
    Country,
    COUNT(*) AS Total_Customers
FROM Customers
GROUP BY Country
HAVING COUNT(*) > 5
ORDER BY Total_Customers DESC;
"""

# Execute query and load into DataFrame
df = pd.read_sql_query(query, conn)

# Save report
df.to_csv("reports/country_customer_report.csv", index=False)

conn.close()

print("✅ Country-wise customer report generated successfully")
