import sqlite3
import pandas as pd

conn = sqlite3.connect("practice.db")

query = """
SELECT country, AVG(age) AS avg_age
FROM customers
GROUP BY country
"""

df = pd.read_sql(query, conn)
