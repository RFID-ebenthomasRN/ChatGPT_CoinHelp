import sqlite3

conn = sqlite3.connect('coinflip.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

c.execute("SELECT * FROM flips")
print(c.fetchall())
