# 2. Mastering Your Professional IDE: Visual Studio Code

Welcome to the core of your new development workflow. In Lab 02, you used Google Colab, an excellent tool for interactive notebooks. Now, we transition to a professional-grade local Integrated Development Environment (IDE): Visual Studio Code (VS Code).

An IDE is much more than a text editor. It integrates a suite of tools—a code editor, a terminal, a debugger, and support for extensions—into a single application, streamlining your entire development process.

---

## 2.1. VS Code Interface and Configuration (15 minutes)

First, let's get familiar with the VS Code user interface.

### Hands-on Exploration

Open VS Code and take a moment to identify these key areas:

1.  **Explorer Panel (Left Sidebar)**: This is your file and folder navigator. You can open, create, and manage your project files here.
2.  **Integrated Terminal**: Open it by pressing `` ` `` (backtick) or by going to `Terminal > New Terminal`. This is where you'll run commands, just like in a standalone terminal.
3.  **Extensions Marketplace (Left Sidebar)**: Look for the icon with four squares. This is where you can find and install thousands of extensions to enhance VS Code's functionality.
4.  **Command Palette**: Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac). This powerful tool gives you quick, searchable access to all of VS Code's commands and features.

### Essential Configuration

A little setup now will save you a lot of time later.

-   **Set the Python Interpreter**:
    1.  Open the Command Palette (`Ctrl+Shift+P`).
    2.  Type `Python: Select Interpreter`.
    3.  You should see a list of Python interpreters found on your system. We will connect this to our `conda` environment in a later step.

-   **Productivity Settings**:
    -   **Auto-Save**: Go to `File > Auto Save` and check it. This prevents you from losing work.
    -   **Themes & Shortcuts**: Explore `File > Preferences > Color Theme` and `File > Preferences > Keyboard Shortcuts` to customize VS Code to your liking.

---

## 2.2. Essential Python Extensions (10 minutes)

Extensions are the superpowers of VS Code. Let's install the most critical ones for Python development.

### Required Extensions

Navigate to the **Extensions Marketplace** and install the following:

1.  **Python (from Microsoft)**: This is the official extension. It provides core support for Python, including syntax highlighting, code completion (IntelliSense), and linting (analyzing code for potential errors).
2.  **Pylance (from Microsoft)**: Works alongside the Python extension to provide high-performance type checking and intelligent error detection. It helps you catch bugs before you even run your code.
3.  **Jupyter (from Microsoft)**: Allows you to work with Jupyter notebooks (`.ipynb` files) directly within VS Code, giving you the best of both worlds: the interactivity of notebooks and the power of an IDE.

### Recommended Extensions

Consider these optional but highly recommended extensions for a professional workflow:

-   **GitLens**: Supercharges the Git integration, allowing you to see who wrote each line of code, view version history, and more.
-   **Black Formatter**: Automatically formats your Python code to be clean and consistent every time you save.

---

## 2.3. Virtual Environments & Package Management (20 minutes)

In Lab 02, we discussed reproducibility. Virtual environments are the key to achieving it in a local environment.

**Why use them?** They isolate the packages (external libraries) required for a specific project. This prevents conflicts where one project needs `pandas version 1.5` and another needs `pandas version 2.0`.

### Practical Implementation with Conda

Let's create and manage a virtual environment for this lab using `conda`.

1.  **Create the Environment**: Open your integrated terminal in VS Code and run:
    ```bash
    conda create -n lab03 python=3.11
    ```
    This command creates a new, isolated environment named `lab03` with Python version 3.11.

2.  **Activate the Environment**:
    ```bash
    conda activate lab03
    ```
    You'll see `(lab03)` appear at the beginning of your terminal prompt, indicating the environment is active.

3.  **Connect VS Code to the Environment**:
    -   Open the Command Palette (`Ctrl+Shift+P`).
    -   Run `Python: Select Interpreter`.
    -   Select the Python interpreter associated with your `lab03` conda environment. It should be clearly labeled.

4.  **Install Packages**: With the environment active, let's install the `requests` library we'll need for our API project.
    ```bash
    pip install requests
    ```

5.  **Document the Environment**: To ensure anyone can reproduce your environment, create a `requirements.txt` file.
    ```bash
    pip freeze > requirements.txt
    ```
    This command lists all packages in your active environment and saves them to a file. It's a standard practice for all Python projects.

---

## 2.4. Python Project Organization (15 minutes)

Organizing your files professionally is crucial for projects of any size. Let's create a standard project structure.

### Basic Project Structure Template

Create the following folders and files inside your `lab03` directory. You can do this from the VS Code Explorer or the terminal (`mkdir` command).

```
weather_app/
├── src/
│   └── weather_checker.py
├── data/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

-   `src/`: For your main source code.
-   `data/`: For data files (e.g., CSVs, JSON files).
-   `tests/`: For your test files (we'll cover this in a future lab).
-   `requirements.txt`: The file you generated in the previous step.
-   `README.md`: A file to describe your project.
-   `.gitignore`: A special file that tells Git which files or folders to ignore (e.g., environment files, secret keys).

### Creating Your `.gitignore`

Before you commit your code to Git, create the `.gitignore` file inside your `weather_app` directory and add the following lines. This tells Git to ignore files and folders that don't belong in version control.

```
# Python virtual environment
venv/
.venv/

# Python cache
__pycache__/

# IDE-specific files
.vscode/
.idea/
```

**Activity**: Take a few minutes to create this structure for a new project called `weather_app`. Initialize a Git repository in the `weather_app` directory (`git init`) and write a brief description in your `README.md`.

---

## 2.5. Libraries and Function Definitions (10 minutes)

Before we build our weather app, let's review how to use libraries and define reusable functions—a concept we build upon from Lab 02.

### Library Imports

An `import` statement brings code from an external library into your program.

```python
# Import the entire math library
import math

# Import a specific class (datetime) from a library
from datetime import datetime

# Import a library and give it an alias (we'll see this later)
import random
```

### Function Definition Practice

Functions are blocks of reusable code that perform a specific task. Good functions have a clear name, receive inputs (parameters), and `return` an output. The text inside triple quotes `"""Docstring"""` is a **docstring**, which explains what the function does.

Copy the code below into a new Python file (e.g., `functions_practice.py`) and run it to see the output.

```python
import math
from datetime import datetime
import random

def calculate_circle_area(radius):
    """Calculate the area of a circle using math.pi"""
    return math.pi * radius ** 2

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit temperature"""
    return (celsius * 9/5) + 32

def generate_random_number(min_val, max_val):
    """Generate a random number between min and max values"""
    return random.randint(min_val, max_val)

def get_current_timestamp():
    """Get current date and time as a formatted string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Test the functions ---
# The code below will only run when this script is executed directly
if __name__ == "__main__":
    print(f"Circle area (radius=5): {calculate_circle_area(5):.2f}")
    print(f"25°C in Fahrenheit: {convert_celsius_to_fahrenheit(25)}")
    print(f"Random number (1-100): {generate_random_number(1, 100)}")
    print(f"Current time: {get_current_timestamp()}")
```

This practice prepares you for the next section, where we will define our own functions to interact with a live API.
