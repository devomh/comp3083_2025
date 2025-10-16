File I/O Mini — Context Managers and Path Objects

Goal
- Use `with` statements to manage files safely and `pathlib.Path` for readable file paths.

Key Patterns
- `with open(path) as f:` automatically closes files.
- `Path.read_text()` / `Path.write_text()` for simple cases.
- Catch specific exceptions: `FileNotFoundError`, `PermissionError`, `json.JSONDecodeError`.

Exercises (20–30 minutes)
1) JSON read/write helpers with validation and friendly errors.
2) Append a line to a text file and read it back.
3) List files in a folder and print a short report.

How to Work
- Complete the helpers in `05_File_Handling_Patterns.py` and run the demo.

