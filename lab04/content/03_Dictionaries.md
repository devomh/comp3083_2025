# Dictionaries in Python

## Overview

Dictionaries are unordered (in Python versions before 3.7), mutable collections that store data in key-value pairs. They are ideal for representing structured data, creating fast lookups, and organizing information where each piece of data has a unique identifier (the key).

## Dictionary Creation and Basic Operations

### Creating Dictionaries

```python
# A dictionary of a student
student = {
    "name": "Alice Johnson",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"Student data: {student}")

# Empty dictionary
empty_dict = {}

# Using the dict() constructor
from_keywords = dict(name="Bob", age=25, city="New York")
print(f"From keywords: {from_keywords}")
```

### Basic Dictionary Operations

```python
person = {"name": "Charlie", "age": 30, "job": "Engineer"}

# Get dictionary length
print(f"Length of person dict: {len(person)}")

# Check if a key exists
print(f"'name' in person: {"name" in person}")
print(f"'salary' in person: {"salary" in person}")
```

## Accessing and Modifying Dictionary Data

### Accessing Values

```python
student = {
    "name": "Diana",
    "grades": [85, 92, 78],
    "active": True
}

# Direct key access (raises KeyError if key doesn't exist)
print(f"Name: {student['name']}")

# Safe access with the get() method
# Returns None if the key is not found
print(f"Major: {student.get('major')}")
# Returns a default value if the key is not found
print(f"Major: {student.get('major', 'Undeclared')}")
```

### Adding and Updating Values

```python
inventory = {"apples": 50, "bananas": 30}
print(f"Initial inventory: {inventory}")

# Add a new key-value pair
inventory["oranges"] = 25
print(f"Added oranges: {inventory}")

# Update an existing value
inventory["apples"] = 45
print(f"Updated apples: {inventory}")

# Update multiple values at once
inventory.update({"bananas": 35, "grapes": 20})
print(f"Updated with dict: {inventory}")
```

### Removing Items

```python
scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 98}

# Remove a specific key and return its value
removed_score = scores.pop("Bob")
print(f"Removed Bob's score of {removed_score}. Current: {scores}")

# Delete a specific key (without returning it)
del scores["Alice"]
print(f"Deleted Alice: {scores}")

# Clear all items from the dictionary
scores.clear()
print(f"Cleared scores: {scores}")
```

## Iterating Through Dictionaries

```python
student_grades = {"Alice": 92, "Bob": 87, "Charlie": 95}

# Iterate over keys (the default behavior)
print("\nIterating over keys:")
for student in student_grades:
    print(f"  {student} has a grade of {student_grades[student]}")

# Iterate over values
print("\nIterating over values:")
for grade in student_grades.values():
    print(f"  Grade: {grade}")

# Iterate over key-value pairs (most common)
print("\nIterating over items (key-value pairs):")
for student, grade in student_grades.items():
    print(f"  {student}: {grade}")
```

## Dictionary Comprehensions

Similar to list comprehensions, dictionary comprehensions offer a concise way to create and transform dictionaries.

```python
# Create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(f"Squares dict: {squares}")

# Filter a dictionary
students_scores = {"Alice": 95, "Bob": 72, "Charlie": 88, "Diana": 91}
high_scorers = {name: score for name, score in students_scores.items() if score >= 90}
print(f"High scorers: {high_scorers}")
```

## Nested Dictionaries

Dictionaries can contain other dictionaries, which is useful for modeling complex, structured data.

```python
university = {
    "departments": {
        "CS": {
            "name": "Computer Science",
            "head": "Dr. Johnson",
            "courses": ["COMP3083", "COMP4087"]
        },
        "MATH": {
            "name": "Mathematics", 
            "head": "Dr. Brown",
            "courses": ["MATH2050", "MATH3060"]
        }
    }
}

# Accessing nested data
cs_dept_name = university["departments"]["CS"]["name"]
print(f"CS Department: {cs_dept_name}")

math_head = university.get("departments", {}).get("MATH", {}).get("head", "N/A")
print(f"Math Department Head: {math_head}")
```

## Practical Examples

### Example 1: Word Frequency Counter
This is a classic use case for dictionaries: counting the occurrences of items in a sequence.

```python
text = """
Python is a powerful programming language. Python is easy to learn and
Python is widely used. Programming with Python is fun and programming
skills are valuable.
"""

# Clean and split the text into words
clean_text = text.lower().replace(".", "").replace(",", "")
words = clean_text.split()

# Count frequencies
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Sort the words by frequency in descending order
# sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

print("--- Word Frequency Report ---")
print(f"Total unique words: {len(word_freq)}")
print("Top 5 most frequent words:")
for word, count in sorted_words[:5]:
    print(f"  '{word}': {count} times")
```

### Example 2: Student Gradebook
This example shows how a nested dictionary can effectively model a real-world structure like a gradebook.

```python
gradebook = {
    "COMP3083": {
        "course_name": "Programming I",
        "students": {
            "12345": {"name": "Alice", "grades": [85, 92, 78, 90]},
            "67890": {"name": "Bob", "grades": [91, 88, 95, 87]},
            "54321": {"name": "Charlie", "grades": [76, 82, 79, 85]}
        }
    }
}

# Calculate and add average to each student
course = gradebook["COMP3083"]
for student_id, student_info in course["students"].items():
    grades = student_info["grades"]
    average = sum(grades) / len(grades)
    student_info["average"] = round(average, 1)

# Generate a report
print("\n--- Grade Report for COMP3083 ---")
for student_id, student_info in course["students"].items():
    name = student_info["name"]
    avg = student_info["average"]
    print(f"  Student: {name} (ID: {student_id}), Average: {avg}%")
```

## Best Practices

1.  **Use `get()` for safe access**: When a key might be missing, `d.get(key, default_value)` is safer than `d[key]` because it avoids a `KeyError`.
2.  **Keys must be immutable**: Dictionary keys must be of a type that cannot be changed, such as strings, numbers, or tuples.
3.  **Use `setdefault()` to initialize keys**: `d.setdefault(key, [])` is a concise way to create a key with a default value (like an empty list) only if it doesn't already exist.
4.  **Iterate with `.items()`**: When you need both the key and the value in a loop, using `for key, value in d.items():` is the most direct and readable approach.

--- 

## Exercises

### 1. Ages Dictionary
Create a dictionary called `edades` that stores the names and ages of the following people:
- Carlos, 22
- Jorge, 15
- Melinda, 19
- Laura, 9

### 2. Formatted Dictionary Output
Using the `edades` dictionary from the previous exercise, write a loop that prints its content in the following format:
```
Estudiante: Carlos    | Edad:  22 años
Estudiante: Jorge     | Edad:  15 años
...
```
*Hint: Use f-string formatting to align the text.*

### 3. Name Lookup
Write a program that asks the user for a name and, using the `edades` dictionary, returns the person's age. If the name is not in the dictionary, it should print the message "No registrado".

### 4. Word Frequency Counter
Write a program that, given a sentence, counts how many times each word appears. The result should be a dictionary where the keys are the words and the values are their frequencies. Assume the text is lowercase and has no punctuation.

**Example Input:** `"I think I will do great I think"`
**Example Output:** `{'i': 2, 'think': 2, 'will': 1, 'do': 1, 'great': 1}`
