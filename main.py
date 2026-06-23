from fastapi import FastAPI

app = FastAPI()


@app.get("/fortune")
def get_fortune():
    return {"result": "大吉", "message": "今日はいい日になりそう！"}