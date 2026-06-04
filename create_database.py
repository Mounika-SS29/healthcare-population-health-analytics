import pandas as pd
import sqlite3

df = pd.read_csv("diabetes_state_burden.csv")

conn = sqlite3.connect("healthcare.db")

df.to_sql(
    "diabetes_data",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully")

conn.close()