import sqlite3

# Task 1

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT
    o.order_id, 
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()

# Task 2

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query2 = """
SELECT 
    c.customer_name, 
    AVG(subquery.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b, 
        SUM(l.quantity * p.price) AS total_price
    FROM orders AS o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id, o.customer_id
) AS subquery
ON c.customer_id = subquery.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

for row in results2:
    print(row)

conn.close()

#Task 3
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
customer_id = cursor.fetchone()[0]

cursor.execute("SELECT employee_id FROM employees WHERE first_name='Miranda' AND last_name='Harris'")
employee_id = cursor.fetchone()[0]

cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
products = cursor.fetchall()

cursor.execute(f"""
    INSERT INTO orders (customer_id, employee_id, date)
    VALUES ({customer_id}, {employee_id}, DATE('now'))
    RETURNING order_id
""")
order_id = cursor.fetchone()[0]

for p in products:
    cursor.execute(f"""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES ({order_id}, {p[0]}, 10)
    """)

conn.commit()

cursor.execute(f"""
    SELECT l.line_item_id, 
        l.quantity, 
        p.product_name
    FROM line_items l
    JOIN products p ON l.product_id = p.product_id
    WHERE l.order_id = {order_id}
""")
results3 = cursor.fetchall()

for row in results3:
    print(row)

conn.close()

# Task 4

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query3 = """
SELECT e.employee_id,
    e.first_name,
    e.last_name,
    COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC;
"""

cursor.execute(query3)
results4 = cursor.fetchall()

for row in results4:
    print(row)