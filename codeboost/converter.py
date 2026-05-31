from codeboost.client import get_gemini_client
from codeboost.config import MODEL
from codeboost.prompts import messages_for

_FENCE_MARKERS = ("```cpp", "```c++", "```")


def port(python: str) -> str:
    """Convert Python source to optimized C++ using Gemini."""
    client = get_gemini_client()
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages_for(python),
    )
    reply = response.choices[0].message.content or ""
    for fence in _FENCE_MARKERS:
        reply = reply.replace(fence, "")
    return reply.strip()
