from fastapi import FastAPI, HTTPException
from models import Prompt, Game
from generate import generate_trivia_game

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the TrivMe Backend API"}

@app.post("/generate", response_model=Game)
def create_game(prompt: Prompt):
    """
    Endpoint to receive a prompt and generate a trivia game.
    """
    try:
        game = generate_trivia_game(prompt.text)
        return game
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
