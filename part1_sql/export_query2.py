import sqlite3
import csv

conn = sqlite3.connect("data/meesho_reseller.db")
cur = conn.cursor()

sql = """
SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY revenue DESC;
"""

cur.execute(sql)
rows = cur.fetchall()

with open(
    "part1_sql/output/region_totals.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["region", "revenue", "n_orders"])
    writer.writerows(rows)

conn.close()

print("CSV created successfully.")