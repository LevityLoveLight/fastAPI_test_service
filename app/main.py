from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()


class Question(BaseModel):
    question_id: int
    question: str
    answer: str


class Quest(BaseModel):
    questions_num: int


@app.post("/question/")
async def question(quest: Quest):
    response = httpx.get(f"https://jservice.io/api/random?count={quest.questions_num}")
    for quest in response.json():
        question_id = quest.get("id")
        question = quest.get()
        answer = quest.get()
    return response.json
