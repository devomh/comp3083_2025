# Introduction to Programming and CS I - Lab 03

## Overview

This lab bridges the gap between fundamental programming concepts and professional software development practices. Students will transition from interactive notebooks to a fully-featured local development environment using Visual Studio Code. The core of this lab is a hands-on project to build a real-world application that integrates with a live web API, reinforcing concepts of project organization, virtual environments, and robust coding.

## Learning Objectives

By the end of this lab, students will be able to:

- Set up and configure a professional Python development environment using VS Code.
- Understand, create, and manage virtual environments to ensure project reproducibility.
- Implement a standard, professional project structure for Python applications.
- Understand the fundamentals of APIs and make HTTP requests to fetch live data.
- Build a complete, functional application that integrates with a third-party API.
- Read and parse JSON data within a Python application.
- Apply debugging techniques within an IDE to identify and resolve errors.
- Apply security best practices for API key management using environment variables.
- Document a project with a `README.md` and manage dependencies with `requirements.txt`.

## Lab Structure

### Core Content Modules

1.  **[Introduction and Environment Setup](content/01_Introduction.md)**
    -   Installing and configuring all required tools: Git, Miniconda, and VS Code.
    -   Connecting this lab to concepts from Labs 01 and 02.

2.  **[Mastering Your Professional IDE](content/02_IDE.md)**
    -   A deep dive into VS Code features for Python development.
    -   Setting up virtual environments and managing packages with `pip`.
    -   Best practices for organizing a Python project.

3.  **[APIs & Real-World Data Integration](content/03_API.md)**
    -   Understanding how to work with web APIs to fetch live data.
    -   Step-by-step guide to building a command-line weather checker application.
    -   Techniques for error handling and data parsing.

### Example Code

-   **[Function Definition Practice](content/examples/math_functions.py)**: A script for practicing function definitions and library imports.
-   **[Complete Weather App](content/examples/weather_checker.py)**: The final, working code for the weather application project.
-   **[Debugging Challenge](content/examples/weather_with_errors.py)**: An intentionally broken version of the app to practice debugging.

## Prerequisites

-   Completion of Lab 02 (Programming Fundamentals).
-   A solid understanding of the input-compute-output paradigm.
-   Familiarity with basic Python syntax, variables, and data types.

## Assessment and Deliverables

To complete this lab, you will need to submit the following:

-   **A functional weather checker application** that successfully fetches and displays data from the OpenWeatherMap API.
-   **A well-organized project structure** following the template provided in the lab materials.
-   **A `requirements.txt` file** listing all project dependencies.
-   **A complete project uploaded to a new repository on your personal GitHub account**, including a descriptive `README.md`.

### Assessment Criteria

-   **Technical Implementation (40%)**: The application works as expected, integrates with the API, handles basic errors, and uses secure environment variables for API keys.
-   **Code Organization (25%)**: The project follows the specified file and folder structure.
-   **Documentation (20%)**: The repository includes a clear `README.md`, and the code uses meaningful variable names and comments.
-   **Problem Solving (15%)**: Demonstrated ability to debug issues and apply concepts to solve problems.

## Troubleshooting Common Issues

-   **`conda` command not found**: This usually means Conda was not added to your system's PATH. Close and reopen your terminal. On Windows, use the "Anaconda Prompt" if available.
-   **`ModuleNotFoundError`**: This is a classic error. It almost always means one of two things: (1) you forgot to install the package (`pip install <package-name>`) or (2) your VS Code terminal is not using your activated `conda` environment. Make sure `(lab03)` is visible in your terminal prompt.
-   **Environment Variable Not Set**: If you get "API key not found" error, ensure you've set the `WEATHER_API_KEY` environment variable using the platform-specific commands in the lab materials.
-   **API Key Issues (401 Error)**: Double-check email verification completion and API key format (32 characters). Never commit API keys to Git repositories.
-   **City Not Found (404 Error)**: The API could not find the city you entered. Check for spelling mistakes.

## Course Progression

This lab provides the foundational skills for nearly all modern software development. The ability to set up a local environment, organize a project, and interact with APIs is essential for the more advanced topics we will cover next, including:

-   Advanced Data Structures and Algorithms
-   Object-Oriented Programming
-   Building Web Applications and Services
