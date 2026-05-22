import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

with open("brouillon.sql", "r") as file:
    cursor.executescript(file.read())

conn.commit()
conn.close()
