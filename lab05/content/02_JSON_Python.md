# JSON and Python: Serialization and Deserialization

## Overview

Now that you understand JSON syntax from [Module 1](01_JSON_Basics.md), it's time to work with JSON in Python. This module teaches you how to convert between Python objects and JSON text—a process called **serialization** (Python → JSON) and **deserialization** (JSON → Python).

### Prerequisites
- Understanding of JSON syntax and structure (Module 1)
- Familiarity with Python dictionaries and lists (Lab 04)
- Basic file I/O concepts

## Python's `json` Module

Python's built-in `json` module provides four essential functions for working with JSON:

| Function | Purpose | Memory/File |
|----------|---------|-------------|
| `json.dumps()` | **Dump** Python object to JSON **string** | Memory (string) |
| `json.loads()` | **Load** JSON **string** to Python object | Memory (string) |
| `json.dump()` | **Dump** Python object to JSON **file** | File |
| `json.load()` | **Load** JSON **file** to Python object | File |

**Memory Aid**: The "s" in `dumps`/`loads` stands for "string"!

## Type Mapping: Python ↔ JSON

When converting between Python and JSON, types are automatically mapped:

| Python Type | → | JSON Type | ← | Python Type |
|-------------|---|-----------|---|-------------|
| `dict` | → | object `{}` | ← | `dict` |
| `list`, `tuple` | → | array `[]` | ← | `list` |
| `str` | → | string | ← | `str` |
| `int`, `float` | → | number | ← | `int` or `float` |
| `True` | → | `true` | ← | `True` |
| `False` | → | `false` | ← | `False` |
| `None` | → | `null` | ← | `None` |

**Important**: Tuples become lists when converted to JSON (JSON has no tuple type).

---

## Serialization: Python to JSON

Serialization is the process of converting a Python object into a JSON-formatted string.

### Basic Serialization with `dumps()`

```python
import json

# Python dictionary
student_data = {
    "name": "Alice Johnson",
    "student_id": "12345",
    "is_enrolled": True,
    "courses": ["COMP3083", "MATH2050"],
    "gpa": 3.8,
    "advisor": None
}

# Convert to a compact JSON string
json_string = json.dumps(student_data)
print("Compact JSON string:")
print(json_string)
print(f"Type: {type(json_string)}")  # <class 'str'>
```

**Output:**
```
Compact JSON string:
{"name": "Alice Johnson", "student_id": "12345", "is_enrolled": true, "courses": ["COMP3083", "MATH2050"], "gpa": 3.8, "advisor": null}
Type: <class 'str'>
```

### Pretty-Printing with `indent`

For human-readable JSON, use the `indent` parameter:

```python
import json

student_data = {
    "name": "Alice Johnson",
    "student_id": "12345",
    "is_enrolled": True,
    "courses": ["COMP3083", "MATH2050"],
    "gpa": 3.8,
    "advisor": None
}

# Convert to a pretty-printed JSON string
pretty_json = json.dumps(student_data, indent=2)
print("Pretty JSON string:")
print(pretty_json)
```

**Output:**
```json
{
  "name": "Alice Johnson",
  "student_id": "12345",
  "is_enrolled": true,
  "courses": [
    "COMP3083",
    "MATH2050"
  ],
  "gpa": 3.8,
  "advisor": null
}
```

### Sorting Keys with `sort_keys`

To ensure consistent output (useful for comparison or version control):

```python
import json

data = {"zebra": 1, "apple": 2, "mango": 3}

# Sort keys alphabetically
sorted_json = json.dumps(data, indent=2, sort_keys=True)
print(sorted_json)
```

**Output:**
```json
{
  "apple": 2,
  "mango": 3,
  "zebra": 1
}
```

---

## Deserialization: JSON to Python

Deserialization is the process of parsing a JSON string into a Python object.

### Basic Deserialization with `loads()`

```python
import json

# JSON string (notice the triple quotes for multi-line strings)
json_string = '''
{
  "name": "Bob Smith",
  "age": 22,
  "courses": ["PHYS1010", "MATH2051"],
  "active": true,
  "graduation_year": null
}
'''

# Convert JSON string to Python dictionary
student_data = json.loads(json_string)

print("Python object:")
print(student_data)
print(f"Type: {type(student_data)}")  # <class 'dict'>

# Access data like a normal Python dictionary
print(f"\nStudent name: {student_data['name']}")
print(f"First course: {student_data['courses'][0]}")
print(f"Graduation year: {student_data['graduation_year']}")
```

**Output:**
```
Python object:
{'name': 'Bob Smith', 'age': 22, 'courses': ['PHYS1010', 'MATH2051'], 'active': True, 'graduation_year': None}
Type: <class 'dict'>

Student name: Bob Smith
First course: PHYS1010
Graduation year: None
```

### Handling Nested Structures

```python
import json

# JSON with nested objects and arrays
json_data = '''
{
  "university": "Springfield University",
  "location": {
    "city": "Springfield",
    "state": "IL",
    "country": "USA"
  },
  "departments": ["Computer Science", "Mathematics", "Physics"],
  "founded": 1965
}
'''

data = json.loads(json_data)

# Access nested data
print(f"University: {data['university']}")
print(f"City: {data['location']['city']}")
print(f"First department: {data['departments'][0]}")
print(f"Number of departments: {len(data['departments'])}")
```

---

## File Operations with JSON

Working with JSON files is one of the most common tasks in data processing.

### Saving Data to a JSON File with `dump()`

```python
import json

students_database = {
    "university": "Springfield University",
    "year": 2025,
    "students": [
        {
            "id": "001",
            "name": "Alice Johnson",
            "major": "Computer Science",
            "gpa": 3.8
        },
        {
            "id": "002",
            "name": "Bob Smith",
            "major": "Mathematics",
            "gpa": 3.6
        },
        {
            "id": "003",
            "name": "Charlie Davis",
            "major": "Physics",
            "gpa": 3.9
        }
    ]
}

# Save to file with pretty-printing
# 'w' mode means "write" (will overwrite existing file)
with open("students_database.json", "w") as file:
    json.dump(students_database, file, indent=2)

print("✓ Data saved to students_database.json")
```

### Loading Data from a JSON File with `load()`

```python
import json

# Load data from the JSON file we just created
# 'r' mode means "read"
try:
    with open("students_database.json", "r") as file:
        loaded_data = json.load(file)

    print("✓ Data loaded successfully!")
    print(f"University: {loaded_data['university']}")
    print(f"Number of students: {len(loaded_data['students'])}")

    # Access individual student data
    for student in loaded_data['students']:
        print(f"  - {student['name']}: {student['major']} (GPA: {student['gpa']})")

except FileNotFoundError:
    print("❌ JSON file not found. Please check the file path.")
except json.JSONDecodeError as e:
    print(f"❌ Error parsing JSON: {e}")
```

**Output:**
```
✓ Data loaded successfully!
University: Springfield University
Number of students: 3
  - Alice Johnson: Computer Science (GPA: 3.8)
  - Bob Smith: Mathematics (GPA: 3.6)
  - Charlie Davis: Physics (GPA: 3.9)
```

---

## Error Handling: Robust JSON Processing

Always use error handling when working with JSON, especially from external sources.

### Common JSON Errors

```python
import json

# 1. JSONDecodeError: Invalid JSON syntax
invalid_json = '{"name": "Alice", "age": 25,}'  # Trailing comma!

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"❌ JSON Decode Error: {e}")
    print(f"   Error at line {e.lineno}, column {e.colno}")

# 2. FileNotFoundError: File doesn't exist
try:
    with open("nonexistent_file.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ File not found error")

# 3. TypeError: Trying to serialize non-JSON-compatible types
try:
    import datetime
    data = {"timestamp": datetime.datetime.now()}
    json_string = json.dumps(data)
except TypeError as e:
    print(f"❌ Type Error: {e}")
```

### Safe JSON Loading Pattern

```python
import json

def load_json_file(filename):
    """Safely load JSON from a file with comprehensive error handling."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in '{filename}': {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Usage
data = load_json_file("students.json")
if data:
    print("✓ Data loaded successfully!")
else:
    print("Using default data instead...")
```

---

## Practical Application: Configuration Manager

JSON files are commonly used for application configuration. This example shows a robust configuration manager.

```python
import json
import os

def get_config(config_file="app_config.json"):
    """
    Load configuration from a JSON file.
    Returns default config if file not found.
    """
    # Default configuration (fallback)
    default_config = {
        "app_name": "Student Manager",
        "version": "1.0",
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "students_db"
        },
        "debug_mode": False,
        "max_students": 1000
    }

    # Try to load from file
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                user_config = json.load(f)
            print(f"✓ Configuration loaded from {config_file}")
            return user_config
        except json.JSONDecodeError as e:
            print(f"⚠️  Config file has errors: {e}")
            print("Using default configuration instead.")
            return default_config
    else:
        print(f"⚠️  Config file '{config_file}' not found.")
        print("Creating default configuration...")

        # Save default config for future use
        with open(config_file, "w") as f:
            json.dump(default_config, f, indent=2)

        return default_config

# Use the configuration
config = get_config()

print(f"\n--- {config['app_name']} v{config['version']} ---")
print(f"Debug mode: {'ON' if config['debug_mode'] else 'OFF'}")
print(f"Database: {config['database']['host']}:{config['database']['port']}")
print(f"Max students: {config['max_students']}")
```

---

## Handling Special Data Types

JSON does not natively support types like Python's `datetime`, `set`, or `Decimal`. To handle these, create a custom encoder.

### Custom JSON Encoder for Dates

```python
import json
from datetime import datetime, date

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()  # Convert to ISO 8601 string
        return super().default(obj)

# Data with dates
event_data = {
    "event": "Tech Conference 2025",
    "start_date": datetime(2025, 10, 15, 9, 0),
    "end_date": date(2025, 10, 17),
    "location": "Miami, FL"
}

# Use the custom encoder
json_output = json.dumps(event_data, cls=CustomJSONEncoder, indent=2)

print("JSON with Custom Encoder:")
print(json_output)
```

**Output:**
```json
{
  "event": "Tech Conference 2025",
  "start_date": "2025-10-15T09:00:00",
  "end_date": "2025-10-17",
  "location": "Miami, FL"
}
```

---

## Exercises

### Exercise 1: Basic Serialization

Create a Python dictionary representing your favorite book with keys: `title`, `author`, `year_published`, `genres` (list), and `is_available` (boolean). Convert it to a pretty-printed JSON string and print it.

<details>
<summary>Solution</summary>

```python
import json

book = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "year_published": 1979,
    "genres": ["Science Fiction", "Comedy", "Adventure"],
    "is_available": True
}

json_string = json.dumps(book, indent=2)
print(json_string)
```
</details>

### Exercise 2: Deserialization and Data Access

Given the JSON string below, parse it and print:
1. The person's name
2. Their second hobby
3. The city they live in

```python
json_data = '''
{
  "name": "Emma Wilson",
  "age": 25,
  "hobbies": ["photography", "hiking", "coding"],
  "address": {
    "city": "Portland",
    "state": "OR"
  }
}
'''
```

<details>
<summary>Solution</summary>

```python
import json

json_data = '''
{
  "name": "Emma Wilson",
  "age": 25,
  "hobbies": ["photography", "hiking", "coding"],
  "address": {
    "city": "Portland",
    "state": "OR"
  }
}
'''

person = json.loads(json_data)

print(f"Name: {person['name']}")
print(f"Second hobby: {person['hobbies'][1]}")
print(f"City: {person['address']['city']}")
```
</details>

### Exercise 3: Save and Load Contact Card

1. Create a Python dictionary representing a contact card with `name`, `email`, `phone`, and a list of `hobbies`.
2. Save it to a file named `contact.json` with proper formatting.
3. Load the data back from the file and print: `"[Name]'s second hobby is [Hobby]."`

<details>
<summary>Solution</summary>

```python
import json

# Step 1: Create contact dictionary
contact = {
    "name": "Sarah Chen",
    "email": "sarah.chen@example.com",
    "phone": "555-0199",
    "hobbies": ["painting", "yoga", "traveling", "cooking"]
}

# Step 2: Save to file
with open("contact.json", "w") as file:
    json.dump(contact, file, indent=2)

print("✓ Contact saved to contact.json")

# Step 3: Load from file and display
with open("contact.json", "r") as file:
    loaded_contact = json.load(file)

print(f"{loaded_contact['name']}'s second hobby is {loaded_contact['hobbies'][1]}.")
```
</details>

### Exercise 4: Process Student Records

Given this JSON file content, load it and calculate:
1. The average GPA of all students
2. The number of students majoring in "Computer Science"
3. List the names of students with GPA > 3.7

```python
students_json = '''
{
  "students": [
    {"name": "Alice", "major": "Computer Science", "gpa": 3.8},
    {"name": "Bob", "major": "Mathematics", "gpa": 3.6},
    {"name": "Charlie", "major": "Computer Science", "gpa": 3.9},
    {"name": "Diana", "major": "Physics", "gpa": 3.5},
    {"name": "Eve", "major": "Computer Science", "gpa": 3.75}
  ]
}
'''
```

<details>
<summary>Solution</summary>

```python
import json

students_json = '''
{
  "students": [
    {"name": "Alice", "major": "Computer Science", "gpa": 3.8},
    {"name": "Bob", "major": "Mathematics", "gpa": 3.6},
    {"name": "Charlie", "major": "Computer Science", "gpa": 3.9},
    {"name": "Diana", "major": "Physics", "gpa": 3.5},
    {"name": "Eve", "major": "Computer Science", "gpa": 3.75}
  ]
}
'''

data = json.loads(students_json)
students = data['students']

# 1. Average GPA
total_gpa = sum(student['gpa'] for student in students)
avg_gpa = total_gpa / len(students)
print(f"Average GPA: {avg_gpa:.2f}")

# 2. Count Computer Science majors
cs_count = sum(1 for student in students if student['major'] == "Computer Science")
print(f"Computer Science majors: {cs_count}")

# 3. Students with GPA > 3.7
high_achievers = [student['name'] for student in students if student['gpa'] > 3.7]
print(f"Students with GPA > 3.7: {', '.join(high_achievers)}")
```

**Output:**
```
Average GPA: 3.71
Computer Science majors: 3
Students with GPA > 3.7: Alice, Charlie, Eve
```
</details>

### Exercise 5: Configuration File Manager

Create a function `update_config(filename, key, value)` that:
1. Loads a JSON config file
2. Updates the specified key with the new value
3. Saves the updated config back to the file
4. Handles errors gracefully (file not found, invalid JSON, etc.)

Test it by creating a config file and updating a value.

<details>
<summary>Solution</summary>

```python
import json
import os

def update_config(filename, key, value):
    """Update a single key in a JSON config file."""
    # Load existing config or create new
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️  Invalid JSON in {filename}. Creating new config.")
            config = {}
    else:
        print(f"⚠️  File {filename} not found. Creating new config.")
        config = {}

    # Update the key
    config[key] = value

    # Save back to file
    with open(filename, "w") as f:
        json.dump(config, f, indent=2)

    print(f"✓ Updated {key} = {value} in {filename}")

# Test the function
update_config("app_config.json", "app_name", "My Awesome App")
update_config("app_config.json", "version", "2.0")
update_config("app_config.json", "debug", True)

# Verify
with open("app_config.json", "r") as f:
    print("\nFinal configuration:")
    print(f.read())
```
</details>

### Exercise 6: Round-Trip Validation

Create a function that:
1. Takes a Python dictionary
2. Converts it to JSON
3. Converts it back to Python
4. Compares the original and final dictionaries
5. Returns `True` if they match, `False` otherwise

Test with various data types.

<details>
<summary>Solution</summary>

```python
import json

def validate_round_trip(data):
    """
    Validate that data survives a round trip to JSON and back.
    Returns True if data is unchanged, False otherwise.
    """
    try:
        # Python -> JSON -> Python
        json_string = json.dumps(data)
        recovered_data = json.loads(json_string)

        # Compare
        if data == recovered_data:
            print("✓ Round trip successful!")
            return True
        else:
            print("❌ Data changed during round trip!")
            print(f"   Original: {data}")
            print(f"   Recovered: {recovered_data}")
            return False
    except (TypeError, json.JSONDecodeError) as e:
        print(f"❌ Error during round trip: {e}")
        return False

# Test cases
print("Test 1: Simple dictionary")
validate_round_trip({"name": "Alice", "age": 25})

print("\nTest 2: Nested structure")
validate_round_trip({
    "user": {
        "name": "Bob",
        "scores": [95, 87, 92]
    }
})

print("\nTest 3: Tuple (will become list)")
validate_round_trip({"coordinates": (10, 20)})  # Note: tuple becomes list!

print("\nTest 4: Mixed types")
validate_round_trip({
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "bool": True,
    "null": None,
    "array": [1, 2, 3],
    "object": {"nested": "value"}
})
```
</details>

---

## Key Takeaways

1. **`dumps`/`loads` work with strings** - use for in-memory operations
2. **`dump`/`load` work with files** - use for persistent storage
3. **Always use error handling** - JSON from external sources may be invalid
4. **`indent` parameter** makes JSON human-readable
5. **Type mapping is automatic** - but be aware of limitations (tuples → lists)
6. **Custom encoders handle special types** - datetime, Decimal, etc.
7. **Configuration files** are a perfect use case for JSON

**Next Module**: [JSON Data Processing and Manipulation](03_JSON_Data_Processing.md)
