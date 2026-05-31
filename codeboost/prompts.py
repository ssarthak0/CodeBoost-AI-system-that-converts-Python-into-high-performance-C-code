from codeboost.config import OUTPUT_FILE, get_compile_command, get_system_info

SYSTEM_PROMPT = """
Your task is to convert Python code into high performance C++ code.
Respond only with C++ code. Do not provide any explanation other than occasional comments.
The C++ response needs to produce an identical output in the fastest possible time.
""".strip()


def user_prompt_for(python: str) -> str:
    return f"""
Port this Python code to C++ with the fastest possible implementation that produces identical output in the least time.
The system information is:
{get_system_info()}
Your response will be written to a file called {OUTPUT_FILE} and then compiled and executed; the compilation command is:
{get_compile_command()}
Respond only with C++ code.
Python code to port:

```python
{python}
```
""".strip()


def messages_for(python: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt_for(python)},
    ]
