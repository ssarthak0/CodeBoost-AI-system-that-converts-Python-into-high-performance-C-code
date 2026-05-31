from openai import OpenAI

from codeboost.config import GEMINI_BASE_URL, GOOGLE_API_KEY

_client: OpenAI | None = None


def get_gemini_client() -> OpenAI:
    global _client
    if _client is None:
        if not GOOGLE_API_KEY:
            raise ValueError("Set GOOGLE_API_KEY in .env (see .env.example)")
        _client = OpenAI(api_key=GOOGLE_API_KEY, base_url=GEMINI_BASE_URL)
    return _client
