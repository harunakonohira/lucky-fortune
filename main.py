from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Fortune(BaseModel):
    result: str
    message: str



@app.get("/fortune", response_model=Fortune)
def get_fortune():
    return {"result": "大吉", "message": "今日はいい日になりそう！"}