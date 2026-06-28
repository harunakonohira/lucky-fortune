import sqlite3

conn = sqlite3.connect("join_practice.db")
cursor = conn.cursor()

# JOINで2つのテーブルをつなげて取り出す
cursor.execute("""
    SELECT fortunes.result, users.name
    FROM fortunes
    JOIN users ON fortunes.user_id = users.id
""")

rows = cursor.fetchall()

print("=== 誰が何を引いたか ===")
for row in rows:
    print(row)

conn.close()