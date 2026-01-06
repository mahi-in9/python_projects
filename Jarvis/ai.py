# ai.py
import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = (
    "You are Jarvis, a concise voice assistant. "
    "Give short, spoken-friendly answers. "
    "Avoid emojis, markdown, or long explanations."
)

def ask_ai(query: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[
                {"role": "system", "parts": [{"text": SYSTEM_PROMPT}]},
                {"role": "user", "parts": [{"text": query}]},
            ],
            config={
                "temperature": 0.5,
                "max_output_tokens": 100,
            },
        )

        return response.text.strip()

    except Exception as e:
        return "Sorry, I am having trouble responding right now."
