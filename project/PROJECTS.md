# COMP3083 Final Lab Project Options

This document defines a **set of uniform final project options** for the course.  
All options share the same technical requirements and grading criteria so that
different projects can be evaluated fairly.

---

## 1. Common Requirements (All Projects)

- **Technology**
  - Implement the UI using **either**:
    - `ipywidgets` in Jupyter/Colab **or**
    - `PySide6` (Qt Designer–based desktop app).
  - You may reuse patterns and examples from Lab 07.

- **Data & JSON**
  - Each project must load and save its data from **at least one JSON file**.
  - Define a clear JSON schema (list of objects with consistent keys).
  - All CRUD operations must update the in‑memory data and keep the JSON file
    in sync (save changes to disk).

- **Core Features**
  - **CRUD**
    - Create new records using the UI.
    - Read/View/list existing records in a list.
    - Update/edit existing records.
    - Delete records with confirmation.
  - **Search**
    - Text search on one or more main fields (e.g., name, title, city).
  - **Filter**
    - At least one filter by category or range (e.g., status, date range,
      grade range, activity type).
  - **Analytics**
    - At least **two** analytics operations from:
      - count, sum, mean, min, max
    - Present results clearly in the UI (labels or message area).

- **Error Handling & Validation**
  - Validate user input (e.g., numeric ranges, required fields).
  - Handle missing/invalid JSON gracefully (show a friendly error message and
    avoid crashing).

- **Code Organization**
  - Separate data logic from UI logic as much as possible.
  - Use functions to avoid duplicated code.
  - Follow naming conventions that make the code readable.

- **Deliverables**
  - Source code (Python + UI files if using Qt Designer).
  - Sample JSON data file(s) with realistic records.
  - If you are using ipywidgets in Colab or Jupyter notebooks, include the following in the notebook as properly formatted text cells:
    - Problem formulation.
    - JSON schema description.
    - Additional considerations.
    - How your interface should be used and its limitations.
  - If you are using PySide6, include a README.md file alongside your UI and Python files that explains:
    - Problem formulation.
    - JSON schema description.
    - Additional considerations.
    - How your interface should be used and its limitations.
    - How to run the project.

---

## 2. Grading Criteria (Applies to All Projects)

Total: **100 points**

- **(15 pts) Data Model & JSON Handling**
  - Clear JSON structure with appropriate fields and types.
  - Correct loading, in‑memory representation, and saving of data.

- **(20 pts) CRUD Operations**
  - All four operations (create, read, update, delete) implemented.
  - Changes are reflected both in the UI and in the JSON file.

- **(15 pts) Search & Filtering**
  - Search works as expected and is responsive.
  - At least one meaningful filter (category or range) works correctly.

- **(15 pts) Analytics**
  - At least two analytics metrics implemented (e.g., count, average, max).
  - Results are correctly calculated and understandable to the user.

- **(15 pts) UI & UX Quality**
  - Layout is clean and consistent; widgets are logically grouped.
  - Labels, buttons, and messages are clear and user‑friendly.
  - Basic UX principles from Lab 07 are applied (feedback, validation, disabled
    states when appropriate).

- **(10 pts) Code Quality & Structure**
  - Code is organized into functions/modules.
  - Variable and function names are meaningful.
  - No obvious duplication or dead code.

- **(5 pts) Error Handling & Robustness**
  - Handles invalid input gracefully.
  - Handles missing or corrupt JSON data without crashing.

- **(5 pts) Documentation & Reflection**
  - `README` is complete and clear.
  - Brief reflection: what you learned and what you would improve next.

---

## 3. Choosing a Project

- Select **one** of the projects (A–G) as your final lab project.
- Make sure you:
  - Use **ipywidgets** or **PySide6**.
  - Implement all required **CRUD, search, filter, and analytics** features.
  - Follow the grading criteria in Section 2.

Each project is designed to connect directly to the skills developed across Labs 01–07: Python fundamentals, data structures, JSON handling, APIs, and user interface development with ipywidgets or PySide6.

---

## Project A – Course Gradebook Manager

### Problem Statement
Design a gradebook application to help an instructor manage a list of students and their exam grades for a single course. The app should support entering, editing, and analyzing student performance.

### Data Model (JSON)
Recommended JSON structure:

- List of student objects, each with:
  - `id` (string or integer)
  - `name` (string)
  - `exam1`, `exam2`, `exam3`, `exam4` (numbers)
  - `grade` (number)
  - Optional: `final_grade` (letter)

### Functional Requirements

- **CRUD**
  - Add a new student with four exam grades.
  - View all students in a list view.
  - Edit a student’s name and exam grades.
  - Delete a student.

- **Search & Filter**
  - Search students by name or ID.
  - Filter by:
    - Grade range (e.g., average >= 90).

- **Analytics**
  - Compute and display:
    - Class average for each exam.
    - Count of students in each letter‑grade range (A/B/C/D/F).

### UI Requirements

- Clear form for entering/editing one student.
- List showing all students and their averages.
- Buttons for:
  - Add student
  - Update student
  - Delete student
  - Recalculate analytics

---

## Project B – Task & Deadline Tracker

### Problem Statement
Create a task management application where users can record tasks, track their status, and see how many days remain until each due date.

### Data Model (JSON)

- List of task objects, each with:
  - `id`
  - `title`
  - `description`
  - `status` (e.g., `"todo"`, `"in_progress"`, `"done"`)
  - `due_date` (string in ISO format, e.g., `"2025-11-20"`)
  - Optional: `created_at`, `priority` (low/medium/high)

### Functional Requirements

- **CRUD**
  - Add new tasks with title, description, status, and due date.
  - Edit existing tasks (including changing status).
  - Delete tasks.
  - View all tasks in a list.

- **Search & Filter**
  - Search by text contained in the title or description.
  - Filter by:
    - Status (todo, in progress, done).
    - Due date range (e.g., tasks due this week).
    - Optional: priority.

- **Analytics**
  - Show:
    - Count of tasks by status.
    - Count of overdue tasks.
    - Average days remaining for tasks that are not completed.

### UI Requirements

- Input area for task details.
- List of tasks with key fields.
- Derived field showing “days remaining” or “overdue by X days”.
- Buttons/controls for filtering by status and date range.

---

## Project C – Fitness Activity Tracker

### Problem Statement
Build an application to track physical activities such as running, walking, or
cycling. Users should be able to record activities and analyze their total and
average exercise over time.

### Data Model (JSON)

- List of activity objects, each with:
  - `id`
  - `activity_type` (e.g., `"run"`, `"walk"`, `"bike"`)
  - `date` (ISO string)
  - `duration_minutes` (number)
  - Optional: `distance_km`, `notes`

### Functional Requirements

- **CRUD**
  - Add activities with type, date, and duration (and optional distance).
  - Edit and delete existing activities.
  - View all activities in a list.

- **Search & Filter**
  - Search by activity type or notes text.
  - Filter by:
    - Activity type.
    - Date range.

- **Analytics**
  - Show:
    - Total duration per activity type.
    - Total duration in a selected date range.
    - Longest single activity (max duration or distance).
    - Optional: average activity duration.

### UI Requirements

- Form for entering a new activity.
- List showing activities and key fields.
- Controls for selecting date range and activity type filters.
- Area to display analytics results.

---

## Project D – Study Habits Tracker

### Problem Statement
Create an application to log study sessions for different courses. The goal is
to help a student understand how much time they spend on each course or topic.

### Data Model (JSON)

- List of study session objects, each with:
  - `id`
  - `course` (e.g., `"COMP3083"`)
  - `topic` or `description`
  - `date` (ISO string)
  - `duration_minutes`
  - Optional: `tags` (list of strings), `mood`

### Functional Requirements

- **CRUD**
  - Add study sessions with course, topic, date, and duration.
  - Edit and delete sessions.
  - View sessions in a list.

- **Search & Filter**
  - Search by topic text.
  - Filter by:
    - Course.
    - Date range.
    - Optional: tag.

- **Analytics**
  - Show:
    - Total minutes/hours studied per course.
    - Average session length.
    - Course with the most total study time.

### UI Requirements

- Entry form for new sessions.
- List of sessions with key fields.
- Controls to choose course and date range filters.
- Analytics display area summarizing study patterns.

---

## Project E – Movie Dataset Explorer (GUI)

### Problem Statement
Develop a movie explorer application that allows users to browse, search, and analyze a collection of movies stored in a JSON file.

### Data Model (JSON)

- List of movie objects, each with fields such as:
  - `id`
  - `title`
  - `year`
  - `genre`
  - `director`
  - Optional: `rating`, `cast` (list of strings)

### Functional Requirements

- **CRUD**
  - Add new movies with the main fields.
  - Edit movie details.
  - Delete movies.
  - View all movies in a list.

- **Search & Filter**
  - Search by movie title.
  - Optional: search by director or actor name.
  - Filter by:
    - Genre.
    - Year or year range.

- **Analytics**
  - Show:
    - Number of movies per genre.
    - Oldest and newest movies (min/max year).
    - Optional: average rating (if ratings are included).

### UI Requirements

- Input section for movie details.
- List view of movies with sortable columns (if possible).
- Drop‑downs for genre and/or year filters.
- Analytics section summarizing the dataset.

---

## Project F – Weather History Dashboard (JSON‑Based)

### Problem Statement
Implement a weather dashboard that allows the user to explore historical or sample weather data stored locally in JSON. (Optional extension: fetch live data from an API and append it to the JSON file.)

### Data Model (JSON)

- List of weather records, each with:
  - `id`
  - `city`
  - `date` (ISO string, possibly including time)
  - `temperature_c`
  - `humidity`
  - `condition` (e.g., `"rainy"`, `"sunny"`, `"cloudy"`)

### Functional Requirements

- **CRUD**
  - Add new weather records manually (city, date, temperature, etc.).
  - Edit and delete records.
  - Display records in a list.

- **Search & Filter**
  - Search by city name.
  - Filter by:
    - City.
    - Date range.
    - Optional: temperature range or condition.

- **Analytics**
  - Show:
    - Average temperature per city.
    - Max and min temperature for a selected city or date range.
    - Count of days per condition (e.g., how many rainy days).

### UI Requirements

- Controls to select city and date range.
- List showing matching records.
- Clearly labeled area for analytics results.
- Optional: button to “Import latest data” from an API (if implemented as an
  extension).

---

## Project G – Personal Digital Library Manager (GUI)

### Problem Statement
Create a personal library manager to keep track of books or articles. Users should be able to record what they own, what they have read, and what they plan to read.

### Data Model (JSON)

- List of items, each with:
  - `id`
  - `title`
  - `author`
  - `year`
  - `status` (e.g., `"to_read"`, `"reading"`, `"finished"`)
  - Optional: `tags` (list), `rating` (number), `summary`

### Functional Requirements

- **CRUD**
  - Add new books/articles.
  - Edit existing entries (status, rating, etc.).
  - Delete entries.
  - View the collection in a list/table.

- **Search & Filter**
  - Search by title or author.
  - Filter by:
    - Status (to read/reading/finished).
    - Tag (e.g., `"AI"`, `"Databases"`).

- **Analytics**
  - Show:
    - Count of items per status.
    - Number of items per year or per tag.
    - Optional: average rating of finished items.

### UI Requirements

- Form for entering/editing items.
- List of items with sortable or filterable columns (if possible).
- Controls for choosing status and tag filters.
- Analytics summary section.


