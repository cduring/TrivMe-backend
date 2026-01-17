
# TrivMe Backend

This is the FastAPI backend for the TrivMe application. It generates trivia games using Google's Gemini API.

## Prerequisites

- Python 3.14.2+
- A Google Cloud Project with the Gemini API enabled and an API Key.

## Setup

1.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install dependencies:**

    ```bash
    pip install .
    # Or manually:
    # pip install "google-genai>=1.59.0" "fastapi>=0.128.0" "uvicorn>=0.40.0" "pydantic>=2.12.5"
    ```

3.  **Configuration:**

    Duplicate `.env.example` to `.env` (if it exists) or create a `.env` file with your Gemini API key:

    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Running the Server

Start the FastAPI development server:

```bash
fastapi dev main.py
```

The server will start at `http://127.0.0.1:8000`.

## API Endpoints

### `POST /generate`

Generates a trivia game based on a prompt.

**Request Body:**

```json
{
  "text": "Science fiction movies from the 80s"
}
```

**Response:**

Returns a JSON object conforming to the `Game` schema, containing a topic and a list of questions.

## Testing

You can test the endpoint using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"text": "History of the Internet"}'
```
