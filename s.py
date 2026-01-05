import pandas as pd

df = pd.read_csv("customer_report.csv")
df.to_excel("customer_report.xlsx", index=False)
