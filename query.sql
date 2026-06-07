SELECT * FROM Sales;

SELECT name
FROM sqlite_master
WHERE type='table';
CREATE TABLE Sales (
    OrderID INTEGER,
    Category TEXT,
    Product TEXT,
    Quantity INTEGER,
    Price INTEGER
);

INSERT INTO Sales VALUES
(1001,'Electronics','Laptop',2,50000),
(1002,'Fashion','T-Shirt',5,800),
(1003,'Electronics','Mobile',3,20000),
(1004,'Home','Chair',4,3000),
(1005,'Fashion','Jeans',2,1500),
(1006,'Electronics','Headphones',6,2000),
(1007,'Home','Table',1,7000),
(1008,'Fashion','Shoes',3,2500);
SELECT * FROM Sales;