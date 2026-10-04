import sqlite3
import csv

conn = sqlite3.connect("data/meesho_reseller.db")
cur = conn.cursor()

sql = """
SELECT
    r.reseller_id,
    r.reseller_name,
    r.region
FROM resellers r
LEFT JOIN orders o
    ON r.reseller_id = o.reseller_id
GROUP BY r.reseller_id, r.reseller_name, r.region
HAVING COUNT(o.order_id) = 0;
"""

cur.execute(sql)
rows = cur.fetchall()

with open(
    "part1_sql/output/zero_order_resellers.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["reseller_id", "reseller_name", "region"])
    writer.writerows(rows)

conn.close()

print("CSV created successfully.")