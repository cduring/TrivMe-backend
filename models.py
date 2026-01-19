from pydantic import BaseModel, Field
from typing import List

class Prompt(BaseModel):
    text: str

class Question(BaseModel):
    text: str = Field(description="The question text.")
    options: List[str] = Field(description="A list of 4 multiple choice options.")
    answer: int = Field(description="The index of the correct answer from the options [0, 1, 2 or 3].")

class Game(BaseModel):
    title: str = Field(description="The title of the trivia game. Should be exciting.")
    description: str = Field(description="A description of the game's topic.")
    questions: List[Question] = Field(description="A list of 5 to 10 trivia questions.")
