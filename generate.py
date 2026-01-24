import os
from google import genai
from dotenv import load_dotenv
from .models import Game

MODEL_NAME="gemini-2.5-flash-lite"

def generate_trivia_game(prompt_text: str) -> Game:
    """
    Generates a TriviaGame based on a prompt using the Gemini API.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Generate a trivia game based on the following topic or request:
    "{prompt_text}"

    Ensure the questions are engaging and cover different aspects of the topic.
    The game should have the specified number of questions. Do 5 if not specified.
    Each question must have 4 options and one correct answer.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Game,
        },
    )

    game = response.parsed
    return game
