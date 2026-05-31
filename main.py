"""Entry point: uv run python main.py"""

from codeboost.config import get_compile_command, get_run_command
from codeboost.ui import launch_app


def main() -> None:
    print("Compile:", " ".join(get_compile_command()))
    print("Run:", " ".join(get_run_command()))
    launch_app()


if __name__ == "__main__":
    main()
