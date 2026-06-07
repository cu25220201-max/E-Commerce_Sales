import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

data = [
(1001,'Electronics','Laptop',2,50000),
(1002,'Fashion','T-Shirt',5,800),
(1003,'Electronics','Mobile',3,20000),
(1004,'Home','Chair',4,3000),
(1005,'Fashion','Jeans',2,1500)
]

cursor.executemany(
"INSERT INTO Sales VALUES (?, ?, ?, ?, ?)",
data
)

conn.commit()
conn.close()

print("Data Inserted Successfully")