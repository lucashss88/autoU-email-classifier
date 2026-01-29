import os
import json
import logging
from dotenv import load_dotenv
from google import genai

load_dotenv()
logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def analyze_with_gemini(text: str) -> dict:
    prompt = f"""
    You are an email triage assistant for the company AutoU.
    Analyze the following email and classify it.

    Email:
    "{text}"

    Rules:
    - Category "Produtivo": Requests, support, questions, complaints.
    - Category "Improdutivo": Thanks, spam, congratulations, "ok", "thanks".

    Reply EXACTLY with this JSON format:
    {{
        "category": "Produtivo" or "Improdutivo",
        "suggested_response": "Write a short and polite response here."
    }}
    """

    try:
        if client is None:
            raise RuntimeError('GEMINI_API_KEY is not configured')

        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt,
            config={'response_mime_type': 'application/json'}
        )

        return json.loads(response.text)

    except json.JSONDecodeError:
        logger.error('Gemini response is not valid JSON')
        return {
            "category": "AI Error",
            "suggested_response": "Não foi possível conectar ao Google Gemini. Resposta inválida do modelo."
        }
    except Exception as e:
        logger.error(f"GEMINI ERROR: {e}")
        return {
            "category": "AI Error",
            "suggested_response": "Não foi possível conectar ao Google Gemini. Verifique sua chave de API."
        }
