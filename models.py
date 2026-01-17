from pydantic import BaseModel, Field
from typing import List

class Prompt(BaseModel):
    text: str

class Question(BaseModel):
    text: str = Field(description="The question text.")
    options: List[str] = Field(description="A list of 4 multiple choice options.")
    correct_answer: str = Field(description="The correct answer from the options.")

class Game(BaseModel):
    topic: str = Field(description="The specific topic of the trivia game.")
    questions: List[Question] = Field(description="A list of 5 to 10 trivia questions.")
