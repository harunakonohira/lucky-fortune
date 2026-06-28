import sqlite3

conn = sqlite3.connect("fortune.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM fortunes")
rows = cursor.fetchall()

print("=== 占い履歴 ===")
for row in rows:
    print(row)

conn.close()