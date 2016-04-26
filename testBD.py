import sqlite3, csv

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute("""SELECT * FROM equipements""")
test = cursor.fetchone()
print(test)



conn.close()