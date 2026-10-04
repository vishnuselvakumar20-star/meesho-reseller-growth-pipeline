import sqlite3
import csv

conn = sqlite3.connect("data/meesho_reseller.db")
cur = conn.cursor()

sql = """
SELECT
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY
    CASE month
        WHEN 'April' THEN 1
        WHEN 'May' THEN 2
        WHEN 'June' THEN 3
    END,
    category;
"""

cur.execute(sql)
rows = cur.fetchall()

with open(
    "part1_sql/output/monthly_category_revenue.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["month", "category", "revenue", "n_orders"])
    writer.writerows(rows)

conn.close()

print("CSV created successfully.")