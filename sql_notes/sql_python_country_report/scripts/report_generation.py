import sqlite3
from tabulate import tabulate
import pandas as pd

conn = sqlite3.connect("data/customers.db")
cursor = conn.cursor()

query ="""
SELECT
 Country,
 COUNT(*) AS Total_Customers 
 FROM Customers
 GROUP BY Country
 ORDER BY Total_customers DESC;
 """
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

headers = ["Country", "Total_Customers"]
df = pd.DataFrame(rows, columns=headers)

# ======Step 3: Define color======================== function(before  use) =============

def green(text):
    return f"\033[92m{text}\033[0m"

# ======Display========

display_rows = []
for country, total in rows:
    display_rows.append([country, green(total)])
display_rows = [[c, green(t)] for c, t in rows]
# ===Step 5: Client-readable table =====================================

print(
    tabulate(
        display_rows,
        headers=["Country", "Total_Customers"],
        tablefmt="grid",
        colalign=("center", "center")   # 👈 Country left, Total_Customers center
    )
)

# ==========Step 6: Export clean CSV========================================

df_csv = pd.DataFrame(rows, columns=headers)
df_csv.to_csv("reports/country_customer_report.csv", index=False)






