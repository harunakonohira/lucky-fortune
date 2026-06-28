import sqlite3
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# DBの準備：fortunes テーブルがなければ作る
def init_db():
    conn = sqlite3.connect("fortune.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fortunes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            result TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# アプリ起動時に、DBの準備を1回やる
init_db()


class Fortune(BaseModel):
    result: str
    message: str


@app.get("/fortune", response_model=Fortune)
def get_fortune():
    result = "大吉"
    message = "今日はいい日になりそう！"

    # 占い結果を DB に保存する
    conn = sqlite3.connect("fortune.db")
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO fortunes (result, message, created_at) VALUES (?, ?, ?)",
        (result, message, now)
    )
    conn.commit()
    conn.close()

    return {"result": result, "message": message}

class FortuneHistory(BaseModel):
    id: int
    result: str
    message: str
    created_at: str


@app.get("/history", response_model=list[FortuneHistory])
def get_history():
    conn = sqlite3.connect("fortune.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, result, message, created_at FROM fortunes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    # 取り出したデータを、扱いやすい形に整える
    history = []
    for row in rows:
        history.append({
            "id": row[0],
            "result": row[1],
            "message": row[2],
            "created_at": row[3],
        })
    return history