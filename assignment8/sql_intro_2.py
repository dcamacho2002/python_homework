#Task 5
import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("../db/lesson.db")

    statement = """
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products
    ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(statement, conn)
    print(df.head())

    df['total'] = df['quantity'] * df['price']
    print(df.head())

    group = df.groupby("product_id").agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }).reset_index()
    print(group.head())

    group = group.sort_values("product_name")

    group.to_csv("order_summary.csv", index = False)

except Exception as e:
    print("Error:", e)
