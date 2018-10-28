import sqlite3

connection = sqlite3.connect('holi.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES ('test', 5.00)")
connection.commit()

connection.close()
