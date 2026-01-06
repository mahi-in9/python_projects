import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = (
    "You are Jarvis, a concise conversational voice assistant. "
    "Reply naturally and briefly."
)

def ask_ai(query: str, context: str = "") -> str:
    try:
        contents = SYSTEM_PROMPT
        if context:
            contents += "\n\nConversation so far:\n" + context

        contents += "\nUser: " + query

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=contents,
            config={"temperature": 0.3, "max_output_tokens": 70},
        )

        return response.text.strip()

    except Exception:
        return "I am having trouble responding."
