import os
import platform
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv(override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL = os.getenv("CODEBOOST_MODEL", "gemini-2.5-pro")

EXTENSION = "cpp"
OUTPUT_FILE = f"main.{EXTENSION}"


@lru_cache
def get_compile_command() -> list[str]:
    if platform.system() == "Windows":
        return ["g++", OUTPUT_FILE, "-O3", "-std=c++17", "-o", "main.exe"]
    return ["g++", OUTPUT_FILE, "-O3", "-std=c++17", "-march=native", "-o", "main"]


@lru_cache
def get_run_command() -> list[str]:
    if platform.system() == "Windows":
        return ["main.exe"]
    return ["./main"]


@lru_cache
def get_system_info() -> dict:
    from codeboost.system_info import retrieve_system_info

    return retrieve_system_info()
