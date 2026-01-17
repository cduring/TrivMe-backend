from models import Game
from google import genai

MODEL_NAME="gemini-2.5-flash-lite"

def generate_trivia_game(prompt_text: str) -> Game:
    """
    Generates a TriviaGame based on a prompt using the Gemini API.
    """

    client = genai.Client()

    prompt = f"""
    Generate a trivia game based on the following topic or request:
    "{prompt_text}"

    Ensure the questions are engaging and cover different aspects of the topic.
    The game should have between 5 and 10 questions.
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
