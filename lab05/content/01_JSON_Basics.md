# JSON Basics and Syntax

## Overview

JSON (JavaScript Object Notation) is the universal language of data exchange on the web. Before we learn to work with JSON in Python, we need to understand JSON's structure, syntax rules, and how it differs from Python data types. This foundation will make everything else click into place.

## What is JSON?

JSON is a **text-based format** for representing structured data. Think of it as a standardized way to write down information that both humans and computers can understand. It's used everywhere:

- **Web APIs**: When your app requests data from a server, it usually comes back as JSON
- **Configuration files**: Many applications store settings in JSON format
- **Data storage**: JSON is a lightweight alternative to databases for simple data
- **Message passing**: Services communicate by sending JSON messages to each other

### Why JSON Matters

Imagine you're building a weather app. Your Python code needs to ask a weather service "What's the temperature in Miami?" The service can't send you a Python dictionary—it doesn't speak Python! Instead, it sends JSON text that looks very similar to Python, but works across all programming languages.

## JSON Structure: The Two Building Blocks

JSON is built from just **two fundamental structures**:

### 1. Objects (Like Python Dictionaries)

Objects are collections of **key-value pairs** enclosed in curly braces `{}`. Think of them as labeled boxes where each label (key) points to a value.

```json
{
  "name": "Alice Johnson",
  "age": 20,
  "major": "Computer Science"
}
```

**Key Rules for Objects:**
- Keys **must** be strings wrapped in double quotes
- Keys and values are separated by a colon `:`
- Pairs are separated by commas `,`
- The last pair has **no trailing comma**

### 2. Arrays (Like Python Lists)

Arrays are **ordered lists** of values enclosed in square brackets `[]`.

```json
[
  "Python",
  "JavaScript",
  "Java",
  "C++"
]
```

**Key Rules for Arrays:**
- Values are separated by commas `,`
- Values can be any JSON type (including other arrays or objects)
- Order matters—first item is at index 0
- The last item has **no trailing comma**

## JSON Data Types

JSON supports exactly **six data types**:

### 1. Strings
Text wrapped in **double quotes** (single quotes are invalid in JSON!)

```json
"Hello, World!"
"This is a string with \"escaped\" quotes"
```

### 2. Numbers
Integers or floating-point numbers (no quotes)

```json
42
3.14159
-17
2.5e10
```

### 3. Booleans
True or false values—but notice the **lowercase** spelling!

```json
true
false
```

### 4. Null
Represents "no value" or "missing data"

```json
null
```

### 5. Objects
Key-value collections (as shown above)

```json
{"key": "value"}
```

### 6. Arrays
Ordered lists (as shown above)

```json
[1, 2, 3]
```

## Nested Structures: The Power of JSON

JSON becomes truly powerful when you **nest** structures inside each other.

### Example: Student Record

```json
{
  "student_id": "S12345",
  "name": "Maria Rodriguez",
  "age": 21,
  "enrolled": true,
  "major": "Computer Science",
  "gpa": 3.85,
  "courses": [
    "COMP3083",
    "MATH2050",
    "PHYS1010"
  ],
  "contact": {
    "email": "maria.rodriguez@university.edu",
    "phone": "555-0123"
  },
  "graduation_year": null
}
```

Notice how this combines:
- Simple values (strings, numbers, boolean)
- An array of courses
- A nested object for contact info
- `null` for unknown graduation year

## JSON vs. Python: Spot the Differences

JSON looks similar to Python dictionaries and lists, but there are **critical differences**:

| Feature | Python | JSON |
|---------|--------|------|
| **String quotes** | Single `'` or double `"` | Only double `"` |
| **Boolean values** | `True`, `False` | `true`, `false` |
| **None/null** | `None` | `null` |
| **Object keys** | Can be unquoted | Must be quoted |
| **Trailing commas** | Allowed | **Not allowed** |
| **Comments** | Allowed (`#`) | **Not allowed** |
| **Data types** | Many (tuples, sets, etc.) | Only 6 types |

### Side-by-Side Comparison

**Valid Python (Invalid JSON):**
```python
{
    'name': 'Alice',        # Single quotes
    'active': True,         # Capital T
    'score': None,          # Capital N
    'items': [1, 2, 3,],    # Trailing comma
}
```

**Valid JSON (Python equivalent):**
```json
{
  "name": "Alice",
  "active": true,
  "score": null,
  "items": [1, 2, 3]
}
```

## JSON Syntax Rules: The Must-Know List

1. **All strings use double quotes** - `"text"` not `'text'`
2. **Object keys must be strings** - `{"name": "value"}` not `{name: "value"}`
3. **Booleans are lowercase** - `true` and `false`
4. **Use `null` for missing values** - not `None`
5. **No trailing commas** - `[1, 2, 3]` not `[1, 2, 3,]`
6. **No comments allowed** - JSON is pure data
7. **Proper nesting** - every `{` needs a `}`, every `[` needs a `]`

---

## Exercises: JSON Syntax Mastery

### Exercise 1: Syntax Sorting Game

**Task**: The following JSON snippets are scrambled. Rearrange them into valid JSON.

**Snippet A:**
```
"age": 25,
}
"Alice",
"name":
{
```

**Snippet B:**
```
3
1,
]
[
2,
```

**Snippet C:**
```
"enrolled": true,
"courses": ["COMP3083", "MATH2050"],
}
{
"student_id": "S001",
```

<details>
<summary>Solutions</summary>

**A:**
```json
{
  "name": "Alice",
  "age": 25
}
```

**B:**
```json
[1, 2, 3]
```

**C:**
```json
{
  "student_id": "S001",
  "enrolled": true,
  "courses": ["COMP3083", "MATH2050"]
}
```
</details>

### Exercise 2: JSON vs. Python Spot-the-Difference

**Task**: Identify all the errors in these "JSON" snippets (they're actually invalid Python-style syntax).

**Problem 1:**
```json
{
  'name': 'Bob Smith',
  'age': 22,
  'active': True
}
```

**Problem 2:**
```json
{
  "courses": ["Math", "Science", "English",],
  "gpa": None,
  "year": 2024
}
```

**Problem 3:**
```json
{
  name: "Charlie",
  "graduated": False,
  "credits": 120
}
```

<details>
<summary>Solutions</summary>

**Problem 1 Errors:**
- Single quotes around keys and string values (should be double quotes)
- `True` should be `true`

**Corrected:**
```json
{
  "name": "Bob Smith",
  "age": 22,
  "active": true
}
```

**Problem 2 Errors:**
- Trailing comma after "English"
- `None` should be `null`

**Corrected:**
```json
{
  "courses": ["Math", "Science", "English"],
  "gpa": null,
  "year": 2024
}
```

**Problem 3 Errors:**
- Unquoted key `name` (should be `"name"`)
- `False` should be `false`

**Corrected:**
```json
{
  "name": "Charlie",
  "graduated": false,
  "credits": 120
}
```
</details>

### Exercise 3: Manual JSON Authoring

**Task**: Write valid JSON for the following descriptions. Pay careful attention to syntax!

**A. Course Information:**
Create a JSON object representing a course with:
- Course code: "COMP3083"
- Title: "Introduction to Programming"
- Credits: 3
- Prerequisites: An array containing "COMP1001" and "MATH1050"
- Lab required: true

**B. Student Profile:**
Create a JSON object for a student with:
- Name: "Diana Lee"
- ID: "S67890"
- GPA: 3.92
- Major: "Data Science"
- Clubs: An array with "Robotics Club" and "Chess Club"
- Contact info: A nested object with email "diana.lee@university.edu" and phone "555-9876"

<details>
<summary>Solutions</summary>

**A:**
```json
{
  "course_code": "COMP3083",
  "title": "Introduction to Programming",
  "credits": 3,
  "prerequisites": ["COMP1001", "MATH1050"],
  "lab_required": true
}
```

**B:**
```json
{
  "name": "Diana Lee",
  "id": "S67890",
  "gpa": 3.92,
  "major": "Data Science",
  "clubs": ["Robotics Club", "Chess Club"],
  "contact": {
    "email": "diana.lee@university.edu",
    "phone": "555-9876"
  }
}
```
</details>

### Exercise 4: Structure Identification

**Task**: For each JSON snippet, identify:
1. Is the top-level structure an object or array?
2. How many keys/items are at the top level?
3. List the data type of each value

**Snippet A:**
```json
{
  "temperature": 72.5,
  "condition": "sunny",
  "humidity": 65,
  "wind_speed": 8.3
}
```

**Snippet B:**
```json
[
  {"name": "Alice", "score": 95},
  {"name": "Bob", "score": 88},
  {"name": "Charlie", "score": 92}
]
```

**Snippet C:**
```json
{
  "course": "COMP3083",
  "students": 24,
  "active": true,
  "topics": ["variables", "loops", "functions"],
  "instructor": {
    "name": "Dr. Smith",
    "office": "ENG-301"
  }
}
```

<details>
<summary>Solutions</summary>

**Snippet A:**
1. Object
2. 4 keys
3. Types:
   - `temperature`: number
   - `condition`: string
   - `humidity`: number
   - `wind_speed`: number

**Snippet B:**
1. Array
2. 3 items
3. Types: Each item is an object containing strings and numbers

**Snippet C:**
1. Object
2. 5 keys
3. Types:
   - `course`: string
   - `students`: number
   - `active`: boolean
   - `topics`: array (of strings)
   - `instructor`: object
</details>

### Exercise 5: Error Detective Drills

**Task**: Each JSON snippet below has 1-3 syntax errors. Find and fix them all!

**Problem 1:**
```json
{
  "name": "Eva",
  "age": 23,
  "hobbies": ["reading", "gaming", "coding",]
}
```

**Problem 2:**
```json
{
  "product": "Laptop"
  "price": 999.99,
  "in_stock": true
}
```

**Problem 3:**
```json
{
  'id': "P001",
  "category": 'Electronics',
  "quantity": 50
}
```

**Problem 4:**
```json
{
  "title": "Project Report",
  "pages": 45,
  "submitted": True,
  "grade": None
}
```

**Problem 5:**
```json
{
  "users": [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
  ],
  "total": 2
}
```

<details>
<summary>Solutions</summary>

**Problem 1:**
Error: Trailing comma in array
```json
{
  "name": "Eva",
  "age": 23,
  "hobbies": ["reading", "gaming", "coding"]
}
```

**Problem 2:**
Error: Missing comma after `"Laptop"`
```json
{
  "product": "Laptop",
  "price": 999.99,
  "in_stock": true
}
```

**Problem 3:**
Errors: Single quotes used instead of double quotes
```json
{
  "id": "P001",
  "category": "Electronics",
  "quantity": 50
}
```

**Problem 4:**
Errors: `True` should be `true`, `None` should be `null`
```json
{
  "title": "Project Report",
  "pages": 45,
  "submitted": true,
  "grade": null
}
```

**Problem 5:**
Error: Trailing comma after last object in array
```json
{
  "users": [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"}
  ],
  "total": 2
}
```
</details>

### Exercise 6: Build a Complex JSON Structure

**Task**: Create a JSON representation of a university course catalog entry with the following information:

- Department: "Computer Science"
- Courses: An array of 3 course objects, each containing:
  - code (string)
  - title (string)
  - credits (number)
  - prerequisites (array of strings, can be empty)
  - offered_semesters (array containing "Fall" and/or "Spring")
- Department head: A nested object with:
  - name (string)
  - email (string)
  - office (string)

Make up reasonable data for each course.

<details>
<summary>Sample Solution</summary>

```json
{
  "department": "Computer Science",
  "courses": [
    {
      "code": "COMP1001",
      "title": "Introduction to Computing",
      "credits": 3,
      "prerequisites": [],
      "offered_semesters": ["Fall", "Spring"]
    },
    {
      "code": "COMP2050",
      "title": "Data Structures",
      "credits": 4,
      "prerequisites": ["COMP1001"],
      "offered_semesters": ["Fall", "Spring"]
    },
    {
      "code": "COMP3083",
      "title": "Introduction to Programming",
      "credits": 3,
      "prerequisites": ["COMP1001", "MATH1050"],
      "offered_semesters": ["Fall"]
    }
  ],
  "department_head": {
    "name": "Dr. Sarah Johnson",
    "email": "s.johnson@university.edu",
    "office": "ENG-405"
  }
}
```
</details>

---

## Validation Tools

Before moving to the next module, you should know how to validate JSON:

### Online Validators
- [JSONLint](https://jsonlint.com/) - Copy/paste JSON to check for errors
- [JSON Formatter](https://jsonformatter.org/) - Validates and beautifies JSON

### Command-Line Validation (Python)
You can validate JSON using Python's built-in tools:

```bash
python -m json.tool your_file.json
```

This will either pretty-print valid JSON or show you where the error is.

---

## Key Takeaways

1. **JSON has only 2 structures**: objects `{}` and arrays `[]`
2. **JSON has only 6 data types**: string, number, boolean, null, object, array
3. **Syntax is strict**: Double quotes, no trailing commas, lowercase booleans
4. **JSON ≠ Python**: Similar but not identical—know the differences
5. **Nesting creates power**: Combine objects and arrays for complex data

Now that you understand JSON syntax and structure, you're ready to learn how to work with JSON in Python!

**Next Module**: [JSON and Python - Serialization and Deserialization](02_JSON_Python.md)
