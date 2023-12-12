import sqlite3

con = sqlite3.connect('database.db')

with open('schema.sql') as f:
    con.executescript(f.read())
    
cur = con.cursor()

cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",
            ('Flowers', 'Flowers are very beautiful'))

cur.execute("INSERT INTO posts(title, content) VALUES (?,?)",
            ('Dogs', 'Dogs are cute and loyal'))

con.commit()
con.close()