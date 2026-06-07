import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    OrderID INTEGER,
    Category TEXT,
    Product TEXT,
    Quantity INTEGER,
    Price INTEGER
)
""")

conn.commit()
conn.close()

print("Sales Table Created Successfully")