import sqlite3
import pandas as pd

conn = sqlite3.connect("healthcare.db")

query = """
SELECT Location,
AVG(CAST("Data Value" AS REAL)) AS Avg_Diabetes
FROM diabetes_data
WHERE "Short Indicator Text" = 'Diabetes Prevalence'
AND "Data Type" = 'Age-adjusted Rate (per 100)'
GROUP BY Location
ORDER BY Avg_Diabetes DESC
LIMIT 10
"""

result = pd.read_sql_query(query, conn)

print(result)

conn.close()