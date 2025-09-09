import sqlite3

#Task 1 and 2
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY(subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY(magazine_id) REFERENCES magazines(magazine_id)
        )
        """)

        print("Tables created successfully.")

except sqlite3.Error as e:
    print(f"File failed: {e}")    

#Task 3
def addPublisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print("Publisher exists: ", name)

def addMagazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print("Magazine exists: ", name)

def addSubscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.IntegrityError:
        print("Subscriber exists: ", name)

def addSubscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError as e:
        print("Publisher exists: ", e)

addPublisher(cursor, "Pearson")
addPublisher(cursor, "Oxford University Press")
addPublisher(cursor, "Macmillan")
addMagazine(cursor, "People", 1)
addMagazine(cursor, "Time", 2)
addMagazine(cursor, "Vanity Fair", 3)
addSubscriber(cursor, "John Smith", "123 Main St")
addSubscriber(cursor, "Bob Brown", "456 Pine St")
addSubscriber(cursor, "Adam Jones", "789 Willow St")
addSubscription(cursor, 1, 1, "2025-01-01")
addSubscription(cursor, 2, 2, "2025-05-11")
addSubscription(cursor, 3, 3, "2025-07-20")
conn.commit()


#Task 4
print("\nAll Subscribers:")
cursor.execute("SELECT * FROM subscribers")

for row in cursor.fetchall():
    print(row)

print("\nAll Magazines:")
cursor.execute("SELECT * FROM magazines")

for row in cursor.fetchall():
    print(row)

print("Magazines published by Oxford University Press:")
cursor.execute("""SELECT m.name FROM magazines m 
               JOIN publishers p ON m.publisher_id = p.publisher_id 
               WHERE p.name = 'Oxford University Press'""")

for row in cursor.fetchall():
    print(row)
