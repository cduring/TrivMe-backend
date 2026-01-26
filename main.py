from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import Prompt, Game
from .generate import generate_trivia_game

app = FastAPI(
    title="TrivMe backend",
    description="Backend for TrivMe",
    version="0.0.1",
    contact={"email": "chimdi.during@gmail.com"},
)

origins = ["https://triv-me.vercel.app", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

if __name__ == "__main__":
    main()
