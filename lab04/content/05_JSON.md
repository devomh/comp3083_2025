# JSON in Python

## Overview

JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format that is easy for humans to read and for machines to parse. It has become the de facto standard for data exchange in web APIs, configuration files, and data storage.

### JSON Structure and Syntax

JSON is built on two main structures:
-   **Objects**: Collections of key-value pairs, enclosed in curly braces `{}` (like Python dictionaries).
-   **Arrays**: Ordered lists of values, enclosed in square brackets `[]` (like Python lists).

JSON supports strings, numbers, booleans (`true`/`false`), `null`, objects, and arrays.

## Python's `json` Module

Python's built-in `json` module provides the tools to work with JSON data.

-   `json.dumps()`: **Dumps** a Python object to a JSON formatted **string**.
-   `json.loads()`: **Loads** a JSON formatted **string** into a Python object.
-   `json.dump()`: **Dumps** a Python object to a **file**.
-   `json.load()`: **Loads** a JSON object from a **file**.

### Converting Python to JSON (Serialization)

Serialization is the process of converting a Python object into a JSON string.

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

# Convert to a pretty-printed JSON string for readability
pretty_json = json.dumps(student_data, indent=2, sort_keys=True)
print("\nPretty JSON string:")
print(pretty_json)
```

### Converting JSON to Python (Deserialization)

Deserialization is the process of parsing a JSON string into a Python object.

```python
import json

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

# You can now access the data like a normal Python dictionary
print(f"\nStudent name: {student_data['name']}")
print(f"First course: {student_data['courses'][0]}")
```

## File Operations with JSON

Working with JSON files is a very common task.

### Saving Data to a JSON File

```python
import json

students_database = {
    "university": "Springfield University",
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
        }
    ]
}

# Save the dictionary to a file with pretty-printing
# The 'w' means we are opening the file for writing
with open("students_database.json", "w") as file:
    json.dump(students_database, file, indent=2)

print("Data saved to students_database.json")
```

### Loading Data from a JSON File

```python
import json

# Load data from the JSON file we just created
# The 'r' means we are opening the file for reading
try:
    with open("students_database.json", "r") as file:
        loaded_data = json.load(file)
    
    print("\nData loaded successfully!")
    print(f"University: {loaded_data['university']}")
    print(f"Number of students: {len(loaded_data['students'])}")

except FileNotFoundError:
    print("JSON file not found. Please check the file path.")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
```

## Practical Application: Configuration Manager

JSON files are commonly used for application configuration. This example shows a simple configuration manager.

```python
import json

def get_config(config_file="app_config.json"):
    """Loads configuration from a JSON file."""
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found. Returning default config.")
        # Default configuration
        return {
            "app_name": "My Awesome App",
            "version": "1.0",
            "database": {
                "host": "localhost",
                "port": 5432
            },
            "debug_mode": False
        }

# Load configuration
config = get_config()

# Use configuration settings in the application
print(f"\nRunning {config.get('app_name')} v{config.get('version')}")
if config.get('debug_mode', False):
    print("Debug mode is ON.")
else:
    print("Debug mode is OFF.")

print(f"Connecting to database at {config.get('database', {}).get('host')}")
```

## Handling Special Data Types

JSON does not natively support types like Python's `datetime` or `Decimal`. To handle these, you can create a custom encoder.

```python
import json
from datetime import datetime, date

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat() # Convert datetime to ISO 8601 string
        return super().default(obj)

data_with_dates = {
    "event": "Conference 2024",
    "start_date": datetime(2024, 10, 15, 9, 0),
    "end_date": date(2024, 10, 17),
}

# Use the custom encoder with the `cls` argument
json_output = json.dumps(data_with_dates, cls=CustomJSONEncoder, indent=2)

print("\n--- JSON with Custom Encoder ---")
print(json_output)
```

---

## Exercises

### 1. Create and Save a JSON object

1.  Create a Python dictionary that represents a simple contact card for a person. It should include keys for `name`, `email`, `phone`, and a list of `hobbies`.
2.  Use the `json` module to save this dictionary to a file named `contact.json`. Make sure the output in the file is nicely formatted (pretty-printed).

### 2. Load and Access JSON Data

1.  Write a Python script that loads the data from the `contact.json` file you created in the previous exercise.
2.  After loading the data into a Python dictionary, print a message to the console that says: `"[Name]'s second hobby is [Hobby]."` by accessing the appropriate values from the dictionary.


