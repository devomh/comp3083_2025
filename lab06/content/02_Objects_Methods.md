# Module 2: Objects and Methods Fundamentals

## The Dot Notation Philosophy

You've written `"hello".upper()` and `my_list.append(5)` countless times. Now it's time to understand the **profound paradigm shift** behind that simple dot.

**Key Insight**: The dot notation `object.method()` represents **sending a message to an object**. You're not running a function on data—you're asking an object to perform an action on itself.

This is the essence of **Object-Oriented Programming (OOP)**.

### Quick Recap: Objects and Classes

From Module 1, remember:
- **Object** = A bundle of data + behavior + identity
- **Class** = A blueprint/template that defines what objects of that type can do
- **Instance** = A specific object created from a class (e.g., "hello" is an instance of the `str` class)

In this module, we focus on how to **interact with objects** through the dot notation.

---

## 1. Methods vs. Functions: The Crucial Distinction

### Functions: Standalone Procedures

A **function** is a standalone piece of code that takes inputs and produces outputs.

```python
# Functions take objects as arguments
len([1, 2, 3])        # Ask the function: "What's the length of this list?"
max([5, 2, 8, 1])     # Ask the function: "What's the max of these values?"
sorted([3, 1, 2])     # Ask the function: "Give me a sorted version of this"

# The function operates ON the object
result = sum([1, 2, 3, 4])  # sum() operates on the list
```

**Mental Model**: Functions are like external services. You hand them data and they process it.

### Methods: Object Behavior

A **method** is behavior that belongs to an object. It's called ON the object using dot notation.

```python
# Methods are invoked BY objects
[1, 2, 3].count(2)      # Ask the list: "How many times does 2 appear in you?"
"hello".upper()         # Ask the string: "Give me your uppercase version"
[3, 1, 2].sort()        # Tell the list: "Sort yourself"

# The object performs the action on itself
my_list = [1, 2, 3]
my_list.append(4)  # The list modifies itself
```

**Mental Model**: Methods are like asking an object to do something. The object is an active agent, not passive data.

### Side-by-Side Comparison

```python
# Function approach (external operation)
text = "hello world"
length = len(text)          # Function: len(object)
words = text.split()        # Method: object.method()

# Method approach (object behavior)
numbers = [3, 1, 4, 1, 5]
count = numbers.count(1)    # Method: object.method(args)
numbers.sort()              # Method: object.method()

# Some operations have both!
numbers = [3, 1, 2]
sorted_func = sorted(numbers)  # Function: returns new list
numbers.sort()                  # Method: modifies in place
```

**Why Both Exist?**
- **Functions** like `len()`, `max()`, `sum()` work across many types (duck typing)
- **Methods** are type-specific behaviors unique to that object type
- **Design choice**: Python favors methods for object-specific operations

---

## 2. Reading the Dot: "Object Receives Message"

When you see `object.method()`, read it as:

> "I'm asking the **object** to execute its **method** behavior."

### Examples with Natural Language

```python
# Code: name.upper()
# Read as: "Ask the name object to give me its uppercase version"
name = "alice"
shout = name.upper()  # "ALICE"

# Code: numbers.append(10)
# Read as: "Tell the numbers list to append 10 to itself"
numbers = [1, 2, 3]
numbers.append(10)  # numbers is now [1, 2, 3, 10]

# Code: data.get('key', default)
# Read as: "Ask the data dictionary to get 'key' or return default"
data = {"name": "Alice"}
age = data.get('age', 0)  # Returns 0 (default)

# Code: path.exists()
# Read as: "Ask the path object if it exists in the filesystem"
from pathlib import Path
file_path = Path("data.txt")
if file_path.exists():
    print("File found!")
```

### Why This Mental Model Matters

**Procedural Thinking (OLD)**:
```python
# Thinking: "Run the upper function on name"
result = upper(name)  # This doesn't exist in Python!
```

**Object-Oriented Thinking (NEW)**:
```python
# Thinking: "Ask name to uppercase itself"
result = name.upper()  # This is Python!
```

This shift from "functions operating on passive data" to "objects performing actions" is the **core of object-oriented programming**.

---

## 3. Object State vs. Behavior

Every object bundles together:
- **State** (data/attributes) — What the object knows
- **Behavior** (methods) — What the object can do

### Accessing State: Attributes

**Attributes** are data attached to an object. Access them without parentheses.

```python
from datetime import datetime

# Create a datetime object
now = datetime.now()

# Access attributes (state)
print(now.year)    # 2025
print(now.month)   # 10
print(now.day)     # 16
print(now.hour)    # 14
print(now.minute)  # 30

# Attributes are data, not actions
print(type(now.year))  # <class 'int'>
```

### Invoking Behavior: Methods

**Methods** are actions the object can perform. Call them with parentheses.

```python
from datetime import datetime

now = datetime.now()

# Invoke methods (behavior)
formatted = now.strftime("%Y-%m-%d")      # "2025-10-16"
iso_format = now.isoformat()              # "2025-10-16T14:30:00"
weekday = now.strftime("%A")              # "Thursday"

# Methods are functions, they do things
print(type(now.strftime))  # <class 'builtin_function_or_method'>
```

### Key Difference: Parentheses

```python
# ❌ Common mistake: Forgetting parentheses
text = "hello"
result = text.upper  # Returns the method object, doesn't call it!
print(result)  # <built-in method upper of str object at 0x...>

# ✅ Correct: Call the method with parentheses
result = text.upper()
print(result)  # "HELLO"

# Attributes: NO parentheses
now = datetime.now()
year = now.year   # ✅ Correct
year = now.year() # ❌ Error: int is not callable

# Methods: WITH parentheses
upper = text.upper()   # ✅ Correct
upper = text.upper     # ❌ Wrong: doesn't execute method
```

---

## 4. Method Chaining: Fluent Interfaces

Some methods return objects, allowing you to chain multiple method calls.

### Chaining with Immutable Objects

Immutable objects return new objects, perfect for chaining:

```python
# String method chaining
text = "  Hello World  "
result = text.strip().lower().replace(" ", "_")
print(result)  # "hello_world"

# Breaking it down:
# Step 1: text.strip() → "Hello World"
# Step 2: .lower() → "hello world"
# Step 3: .replace(" ", "_") → "hello_world"

# Each method returns a NEW string object
```

### Chaining Example: Path Operations

```python
from pathlib import Path

# Chain Path operations
home_docs = Path.home() / "Documents" / "projects"
print(home_docs)

# Even though / is an operator, it returns a Path object
# So you can chain it with methods:
if home_docs.exists():
    files = list(home_docs.glob("*.py"))
```

### Non-Chainable: Methods That Return `None`

**Important**: Methods that modify mutable objects in place usually return `None`.

```python
# ❌ This doesn't work - sort() returns None
numbers = [3, 1, 2]
result = numbers.sort().reverse()  # Error! NoneType has no method 'reverse'

# ✅ Do modifications separately
numbers = [3, 1, 2]
numbers.sort()     # Returns None, modifies in place
numbers.reverse()  # Returns None, modifies in place
print(numbers)     # [3, 2, 1]

# ✅ Or use functions that return new objects
numbers = [3, 1, 2]
result = sorted(numbers, reverse=True)  # Returns [3, 2, 1]
```

**Design Principle**: Returning `None` from mutating methods signals "I changed the object in place, I didn't create a new one."

---

## 5. Exploring APIs with `dir()` and `help()`

The most important skill: **teaching yourself** how to use objects by exploring their APIs.

### Using `dir()` to Discover Methods

`dir(object)` returns a list of all attributes and methods:

```python
# Discover what a string can do
text = "hello"
methods = dir(text)

# Filter out special methods (those starting with underscore)
public_methods = [m for m in methods if not m.startswith('_')]
print(public_methods)
# ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', ...]

# Search for specific methods
count_methods = [m for m in dir(text) if 'count' in m.lower()]
print(count_methods)  # ['count']
```

### Using `help()` to Understand Methods

`help(object.method)` shows detailed documentation:

```python
# Get detailed help on a method
text = "hello"
help(text.count)

# Output shows:
# count(sub[, start[, end]]) -> int
#     Return the number of non-overlapping occurrences of substring sub
#     in string S[start:end]. Optional arguments start and end are
#     interpreted as in slice notation.

# Now you understand how to use it!
text = "hello world hello"
print(text.count("hello"))        # 2
print(text.count("hello", 0, 5))  # 1 (only first 5 characters)
```

### Interactive Exploration Pattern

**Pro Tip**: Use this workflow to learn any new object:

```python
# 1. Create an instance
from collections import Counter
word_counts = Counter(['apple', 'banana', 'apple'])

# 2. Explore available methods
methods = [m for m in dir(word_counts) if not m.startswith('_')]
print("Available methods:", methods)

# 3. Get help on interesting methods
help(word_counts.most_common)

# 4. Experiment!
print(word_counts.most_common(1))  # [('apple', 2)]
```

---

## Exercises

### Exercise 1: Method Hunt

Use `dir()` to find methods matching specific criteria.

```python
# Part A: Find all methods of a list that contain 'remove'
my_list = [1, 2, 3]
remove_methods = [m for m in dir(my_list) if 'remove' in m.lower()]
print(f"Remove methods: {remove_methods}")

# Part B: Find all methods of a string that start with 'is'
text = "Hello123"
is_methods = [m for m in dir(text) if m.startswith('is')]
print(f"Is methods: {is_methods}")

# Part C: Experiment with one method from each category
# Test one 'is' method from strings
print(f"text.isalpha(): {text.isalpha()}")  # False (contains numbers)

# Your tasks:
# 1. Find all dictionary methods that contain 'get'
# 2. Find all list methods that end with 'sort'
# 3. Discover and test a method you've never used on each type
```

---

### Exercise 2: Method vs. Function Sort

Categorize each operation as either a **method call** or **function call**.

```python
# Example code snippets
snippets = [
    "len([1, 2, 3])",           # Function or method?
    "[1, 2, 3].count(2)",       # Function or method?
    "max([5, 2, 8])",           # Function or method?
    "numbers.append(10)",       # Function or method?
    "sorted([3, 1, 2])",        # Function or method?
    "text.upper()",             # Function or method?
    "sum([1, 2, 3])",           # Function or method?
    "data.get('key')",          # Function or method?
    "isinstance(x, int)",       # Function or method?
    "name.split(',')",          # Function or method?
]

# Your task: Create two lists
methods = []
functions = []

# Bonus: Explain the difference in when you'd use each
```

---

### Exercise 3: Chain Reaction

Rewrite these nested function calls as method chains.

```python
# Example:
# Nested: upper(strip(text))
# Chained: text.strip().upper()

# Challenge 1: Nested functions to method chain
text = "  HELLO WORLD  "
# Nested version:
result = upper(strip(text))
# Method chain version:
result = # Your code here

# Challenge 2:
words = "apple,banana,cherry"
# Nested version (pseudocode):
result = sorted(split(words, ','))
# Method chain version:
result = # Your code here

# Challenge 3:
numbers = [1, 2, 3, 4, 5]
# Create a comma-separated string of the numbers
# Try to use method chaining!
# Hint: convert numbers to strings first, then join
result = # Your code here

# Challenge 4: Build your own chain
# Start with "  hello world  " and create "HELLO_WORLD" using method chaining
# Your code here
```

---

### Exercise 4: State vs. Behavior

For each item, identify if it's **state (attribute)** or **behavior (method)**.

```python
from datetime import datetime
from pathlib import Path

now = datetime.now()
file_path = Path("data/sample.txt")

# Classify each:
items = [
    ("now.year", "attribute or method?"),
    ("now.strftime('%Y')", "attribute or method?"),
    ("file_path.name", "attribute or method?"),
    ("file_path.exists()", "attribute or method?"),
    ("file_path.suffix", "attribute or method?"),
    ("now.isoformat()", "attribute or method?"),
    ("file_path.parent", "attribute or method?"),
    ("now.weekday()", "attribute or method?"),
]

# Your task:
# 1. Classify each item
# 2. Explain how you can tell the difference
# 3. Test each one to verify your classification
```

---

### Exercise 5: Documentation Deep Dive

Use `help()` to solve these problems WITHOUT looking at tutorials or Stack Overflow.

```python
# Challenge 1: String splitting with maxsplit
# Use help(str.split) to figure out how to split only the first 2 commas
text = "apple,banana,cherry,date,elderberry"
# Expected result: ['apple', 'banana', 'cherry,date,elderberry']
result = # Your code using split with maxsplit parameter

# Challenge 2: List insertion
# Use help(list.insert) to insert "Python" at index 2
languages = ["Java", "C++", "JavaScript", "Ruby"]
# Expected: ["Java", "C++", "Python", "JavaScript", "Ruby"]
# Your code here

# Challenge 3: String formatting
# Use help(str.format) to create: "Alice scored 95 points"
name = "Alice"
score = 95
result = # Your code using .format()

# Challenge 4: Dictionary setdefault
# Use help(dict.setdefault) to solve this problem:
word_index = {}
words = ["hello", "world", "hello", "python"]
for i, word in enumerate(words):
    # Add index to word's list, creating list if word is new
    # Use setdefault - don't use if statements!
    # Your code here
    pass

print(word_index)
# Expected: {'hello': [0, 2], 'world': [1], 'python': [3]}

# Challenge 5: Discover a new method
# Pick an object type (str, list, dict, set)
# Find a method you've never used via dir()
# Use help() to learn what it does
# Write code that demonstrates it
```

---

## Real-World Application: Method-Based Design

Let's see how methods make code more readable and maintainable.

### Example: Data Processing Pipeline

```python
# Procedural style (function-based)
def process_data_procedural(text):
    text = strip_whitespace(text)
    text = convert_to_lowercase(text)
    text = replace_spaces(text, '_')
    words = split_text(text, '_')
    words = filter_empty(words)
    words = remove_duplicates(words)
    return sort_words(words)

# Object-oriented style (method-based)
def process_data_oop(text):
    words = (text
             .strip()
             .lower()
             .replace(' ', '_')
             .split('_'))
    # Use set to remove duplicates, sorted to sort
    return sorted(set(word for word in words if word))

# The OOP version:
# - Reads left to right (natural flow)
# - Uses built-in methods (no custom functions needed)
# - Is more concise and maintainable
```

### Example: Path Operations

```python
from pathlib import Path

# Old way (os.path functions)
import os
file_path = "/home/user/documents/report.txt"
directory = os.path.dirname(file_path)
filename = os.path.basename(file_path)
name_only = os.path.splitext(filename)[0]
extension = os.path.splitext(filename)[1]

# New way (Path methods)
file_path = Path("/home/user/documents/report.txt")
directory = file_path.parent
filename = file_path.name
name_only = file_path.stem
extension = file_path.suffix

# The method-based approach is:
# - More readable (attributes have clear names)
# - Harder to mess up (no index errors)
# - Chainable for complex operations
```

---

## Key Takeaways

By completing this module, you should understand:

✅ **Methods belong to objects**, functions are standalone

✅ **Dot notation** represents objects performing actions on themselves

✅ **Attributes (state)** are accessed without parentheses: `object.attribute`

✅ **Methods (behavior)** are called with parentheses: `object.method()`

✅ **Method chaining** works when methods return objects

✅ **Mutating methods return `None`** to signal in-place modification

✅ **`dir()` and `help()`** are your tools for exploring any object's API

✅ **Reading documentation** is a critical skill for independent programming

---

## What's Next?

In **Module 3**, we'll apply this object-oriented thinking to Python's standard library. You'll master essential modules like `datetime`, `pathlib`, `collections`, and `random` — all designed around rich object APIs.

You'll see how consistent method patterns make learning new libraries easier, and you'll build practical tools using these powerful objects.

---

## Additional Resources

- [Python Data Model - Methods](https://docs.python.org/3/reference/datamodel.html)
- [Real Python - Python's Instance, Class, and Static Methods](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Fluent Python (Book) - Chapter 1](https://www.oreilly.com/library/view/fluent-python/9781491946237/)
