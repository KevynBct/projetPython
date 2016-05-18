import sqlite3, csv

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute("""SELECT * FROM installation""")
test = cursor.fetchone()
print(test)



conn.close()