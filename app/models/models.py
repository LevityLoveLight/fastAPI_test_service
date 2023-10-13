from pydantic import BaseModel


class Question(BaseModel):
    question_id: int
    question: str
    answer: str
