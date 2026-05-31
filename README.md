# CodeBoost

**AI-assisted Python to C++ conversion for performance-critical workloads.**

CodeBoost is a local web application that uses Google Gemini (via the OpenAI-compatible API) to translate Python into optimized C++. Run the original script, generate C++, compile, and compare output side by side—all from a single Gradio interface.

---

## Features

- **Gemini-powered translation** — Ports Python to idiomatic, performance-oriented C++ with system-aware prompts.
- **Interactive workflow** — Edit Python, run reference output, convert, then compile and execute generated C++.
- **Environment-aware** — Feeds OS, CPU, and toolchain details into the model for better flag and API choices.
- **Modular codebase** — Clear separation of config, client, prompts, conversion, execution, and UI.
- **Fast setup** — Dependency management with [uv](https://docs.astral.sh/uv/); minimal runtime dependencies.

---

## How it works

```text
Python source  →  Gemini (prompt + system info)  →  C++ source
                                                      ↓
                                            g++ compile & run
                                                      ↓
                                            Compare with Python output
```

1. You provide Python in the UI.
2. CodeBoost builds a prompt that includes your machine’s compiler and OS context.
3. Gemini returns C++ only (fences stripped automatically).
4. Optional: `g++` compiles `main.cpp` and runs the binary so you can verify behavior.

---

## Requirements

| Requirement | Notes |
|-------------|--------|
| **Python** | 3.11 or newer |
| **uv** | [Install uv](https://docs.astral.sh/uv/getting-started/installation/) |
| **Google AI API key** | [Create a key](https://aistudio.google.com/apikey) |
| **C++ compiler** (optional) | `g++` on PATH for **Run C++** — e.g. [MinGW-w64](https://www.mingw-w64.org/) on Windows |

Without a compiler, conversion and **Run Python** still work; **Run C++** will report a compile error.

---

## Installation

Clone the repository and install dependencies:

```powershell
git clone <your-repo-url>
cd CodeBoost-AI-system-that-converts-Python-into-high-performance-C-code
```

Configure secrets:

```powershell
copy .env.example .env
```

Edit `.env` and set your API key:

```env
GOOGLE_API_KEY=your_key_here
```

Install packages:

```powershell
uv sync
```

---

## Usage

Start the application:

```powershell
uv run python main.py
```

The Gradio UI opens in your browser (default: `http://127.0.0.1:7860`).

| Step | Action |
|------|--------|
| 1 | Paste or edit Python in the left editor. |
| 2 | **Run Python** — Execute the script and capture stdout (reference). |
| 3 | **Port to C++** — Send code to Gemini and fill the C++ editor. |
| 4 | **Run C++** — Write `main.cpp`, compile with `g++`, and show program output. |

Compare the **Python result** and **C++ result** panels to validate correctness.

---

## Configuration

Environment variables (`.env`):

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GOOGLE_API_KEY` | Yes | — | Google AI Studio API key |
| `CODEBOOST_MODEL` | No | `gemini-2.5-pro` | Gemini model id for chat completions |

Compile and link commands are defined in `codeboost/config.py` (`get_compile_command`, `get_run_command`). Adjust flags there if you use Clang, MSVC, or custom optimization settings.

---

## Project structure

```text
.
├── codeboost/
│   ├── config.py       # Environment, model, compile/run commands
│   ├── client.py       # Gemini OpenAI-compatible client
│   ├── prompts.py      # System and user prompts
│   ├── converter.py    # Python → C++ via LLM
│   ├── runner.py       # Execute Python; compile and run C++
│   ├── ui.py           # Gradio application
│   ├── samples.py      # Default example snippet
│   ├── system_info.py  # Host OS, CPU, toolchain detection
│   └── styles.py       # UI stylesheet
├── main.py             # Application entry point
├── pyproject.toml      # Project metadata and dependencies
├── .env.example        # Environment template
└── LICENSE             # MIT License
```

---

## Development

Run from the project root so imports resolve correctly:

```powershell
uv run python main.py
```

Generated artifacts (`main.cpp`, `main.exe`, `main`) are gitignored. Re-sync after dependency changes:

```powershell
uv sync
```

---

## Limitations

- Generated C++ quality depends on the model and prompt; always review output before production use.
- **Run C++** assumes `g++` and default flags; exotic platforms may need config changes.
- Executing arbitrary Python via `exec()` in the UI is intended for local development only—do not expose this app untrusted on a network without hardening.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [Google Gemini](https://ai.google.dev/) for code generation
- [Gradio](https://gradio.app/) for the web UI
- [uv](https://docs.astral.sh/uv/) for Python package management
