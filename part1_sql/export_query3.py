import sqlite3
import csv

conn = sqlite3.connect("data/meesho_reseller.db")
cur = conn.cursor()

sql = """
SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY r.reseller_id, r.reseller_name
HAVING total_spend > 50000
ORDER BY total_spend DESC
LIMIT 5;
"""

cur.execute(sql)
rows = cur.fetchall()

with open(
    "part1_sql/output/top_spenders.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["reseller_id", "reseller_name", "total_spend"])
    writer.writerows(rows)

conn.close()

print("CSV created successfully.")