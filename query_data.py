import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Sales")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute(
"""
SELECT SUM(Quantity * Price)
FROM Sales
"""
)

print("\nTotal Revenue =", cursor.fetchone()[0])

conn.close()