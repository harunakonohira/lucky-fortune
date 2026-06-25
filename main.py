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


class Fortune(BaseModel):
    result: str
    message: str


@app.get("/fortune", response_model=Fortune)
def get_fortune():
    return {"result": "大吉", "message": "今日はいい日になりそう！"}