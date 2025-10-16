"""
File I/O Mini — Context Managers and Path Objects

Fill in and use these helpers in your lab work and future projects.
"""

from __future__ import annotations
from pathlib import Path
from typing import Any
import json


def read_json(file_path: Path) -> dict[str, Any] | None:
    """Read a JSON file into a dict. Return None on error and print a message."""
    try:
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in {file_path}: {e}")
    except PermissionError:
        print(f"Error: no permission to read {file_path}")
    return None


def write_json(file_path: Path, data: dict[str, Any]) -> bool:
    """Write a dict to JSON file. Returns True on success, False on error."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    except PermissionError:
        print(f"Error: no permission to write {file_path}")
        return False


def read_lines(file_path: Path) -> list[str] | None:
    """Return lines from a text file, or None on error."""
    try:
        return file_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return None


def append_line(file_path: Path, line: str) -> bool:
    """Append a line to a text file. Creates parent dirs if needed."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
        return True
    except PermissionError:
        print(f"Error: no permission to write {file_path}")
        return False


def _demo() -> None:
    # Keep demo artifacts inside the lab06 folder
    base = Path(__file__).resolve().parent / "tmp"
    data_file = base / "sample.json"
    text_file = base / "log.txt"

    print("Write JSON:", write_json(data_file, {"ok": True, "items": [1, 2, 3]}))
    print("Read JSON:", read_json(data_file))

    print("Append line:", append_line(text_file, "hello"))
    print("Append line:", append_line(text_file, "world"))
    print("Read lines:", read_lines(text_file))

    print("List folder contents:")
    for p in base.iterdir():
        print("  ", ("FILE" if p.is_file() else "DIR "), p.name)


if __name__ == "__main__":
    _demo()
