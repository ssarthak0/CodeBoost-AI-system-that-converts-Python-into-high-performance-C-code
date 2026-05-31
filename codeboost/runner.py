import io
import subprocess
import sys

from codeboost.config import OUTPUT_FILE, get_compile_command, get_run_command


def write_output(code: str) -> None:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(code)


def run_python(code: str) -> str:
    globals_dict = {"__builtins__": __builtins__}
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        exec(code, globals_dict)
        output = buffer.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout
    return output


def compile_and_run(code: str) -> str:
    write_output(code)
    compile_command = get_compile_command()
    run_command = get_run_command()
    try:
        subprocess.run(compile_command, check=True, text=True, capture_output=True)
        run_result = subprocess.run(run_command, check=True, text=True, capture_output=True)
        return run_result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred:\n{e.stderr}"
