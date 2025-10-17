# Module 1: Variables and Types Review

## Reconceptualizing Variables as Object References

Welcome to a new way of thinking about variables! You've used variables hundreds of times, but now we'll understand what's *really* happening in Python's memory when you write `x = 42`.

**Key Insight**: In Python, **everything is an object**. Even simple integers have methods, identity, and type. Variables are not boxes that hold values—they're **names that reference objects**.

---

## 1. Everything is an Object

### What is an Object?

An **object** is a self-contained unit that bundles together:
- **Data** (attributes/properties) — What it knows
- **Behavior** (methods) — What it can do
- **Identity** — A unique existence in memory

Think of objects as **entities** that combine information with the operations you can perform on that information.

**Real-world analogy**: A car is an object. It has:
- **Data**: color, speed, fuel level, position
- **Behavior**: accelerate(), brake(), turn()
- **Identity**: This specific car (VIN number)

### What is a Class?

A **class** is a blueprint or template for creating objects. It defines:
- What data the objects will store
- What operations the objects can perform

**Analogy**: A class is like an architectural blueprint, objects are the actual buildings constructed from that blueprint.

```python
# Python has built-in classes:
# - int class creates integer objects
# - str class creates string objects
# - list class creates list objects

x = 42              # Creates an int object
name = "Alice"      # Creates a str object
items = [1, 2, 3]   # Creates a list object
```

In Python, **types are classes**. When you check `type(42)`, you see `<class 'int'>` — the integer class.

### Everything is an Object in Python

In Python, all data are objects. Every object has three fundamental properties:

1. **Identity** — A unique identifier (memory address)
2. **Type** — What kind of object it is (which class created it)
3. **Value** — The data it holds

### Inspecting Objects

Python provides built-in functions to inspect these properties:

```python
# Create a simple integer
x = 42

# Check its type
print(type(x))  # <class 'int'>

# Check its identity (memory address)
print(id(x))  # 140234567891234 (will vary)

# Discover what methods it has!
print(dir(x))  # Lists all available attributes and methods
```

**Surprising Truth**: Even integers have methods! Try this:

```python
# Integers have methods like other objects
number = 42
print(number.bit_length())  # 6 (number of bits needed to represent 42)
print(number.to_bytes(2, 'big'))  # b'\x00*' (convert to bytes)
```

### The Box Analogy

Think of objects as boxes in a warehouse:
- Each box has a **location** (identity/memory address)
- Each box has a **label** describing its contents (type)
- Each box contains **something** (value)
- Variables are **name tags** pointing to boxes

```python
# The variable 'name' is a tag pointing to a string object
name = "Alice"

# We can create another tag pointing to the same box
another_name = name  # Both tags point to same object

print(id(name) == id(another_name))  # True - same box!
```

---

## 2. Identity vs. Equality: `is` vs. `==`

This is a **critical distinction** that trips up many programmers.

- **`==`** checks if two objects have the **same value** (equality)
- **`is`** checks if two variables reference the **exact same object** (identity)

### Example: Two Lists with Same Values

```python
# Create two separate lists with identical contents
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Value equality (do they contain the same values?)
print(list1 == list2)  # True - same contents

# Identity (are they the same object in memory?)
print(list1 is list2)  # False - different objects

# Proof: different memory addresses
print(id(list1))  # e.g., 140234567891234
print(id(list2))  # e.g., 140234567891456
```

### Example: Aliasing (Two Names, One Object)

```python
# Create one list
original = [1, 2, 3]

# Create an alias (another name for the same object)
alias = original

# Both equality AND identity are True
print(alias == original)  # True - same values
print(alias is original)  # True - SAME OBJECT

# Modifying through alias affects original
alias.append(4)
print(original)  # [1, 2, 3, 4] - changed!
```

### When to Use `is` vs. `==`

**Rule of Thumb**:
- Use `==` for value comparison (99% of cases)
- Use `is` only for:
  - Checking if something is `None`: `if value is None:`
  - Checking if two names reference the exact same object (rare)

```python
# ✅ Correct usage
if response is None:
    print("No response received")

if user_input == "quit":  # Value comparison
    break

# ❌ Common mistake
if name is "Alice":  # DON'T DO THIS
    pass  # Unreliable! Use == instead
```

**Why the mistake?** String interning makes small strings sometimes share identity, but it's not guaranteed. Always use `==` for value comparison.

---

## 3. Mutability: The Fundamental Divide

Python objects fall into two categories:

### Immutable Objects (Sealed Boxes)
Once created, they **cannot be changed**. Operations create **new objects**.

**Immutable Types**:
- `int`, `float`, `complex`
- `str` (strings)
- `tuple`
- `frozenset`
- `bool`, `NoneType`

```python
# Strings are immutable
name = "alice"
name.upper()  # Creates NEW string "ALICE", doesn't change original

print(name)  # Still "alice" - original unchanged

# To use the new value, assign it
name = name.upper()
print(name)  # Now "ALICE"
```

**Analogy**: Immutable objects are sealed boxes. If you want to change contents, you must create a new box with different contents.

### Mutable Objects (Boxes with Doors)
Can be **modified in place** without creating new objects.

**Mutable Types**:
- `list`
- `dict`
- `set`

```python
# Lists are mutable
numbers = [1, 2, 3]
numbers.append(4)  # Modifies IN PLACE

print(numbers)  # [1, 2, 3, 4] - original changed
```

**Analogy**: Mutable objects have doors. You can open them and change contents without replacing the whole box.

### Why Mutability Matters: The Aliasing Problem

```python
# Immutable example (no surprises)
x = 10
y = x
x = 20  # Creates NEW int object, rebinds x

print(x)  # 20
print(y)  # 10 - unchanged

# Mutable example (surprise!)
list1 = [1, 2, 3]
list2 = list1  # Both names point to SAME list
list1.append(4)  # Modifies the shared list

print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3, 4] - also changed!
```

### Creating Independent Copies

```python
# For lists: use .copy() or list()
original = [1, 2, 3]
independent = original.copy()  # or list(original)

original.append(4)
print(original)     # [1, 2, 3, 4]
print(independent)  # [1, 2, 3] - unaffected

# For nested structures: use copy.deepcopy()
import copy

nested = [[1, 2], [3, 4]]
shallow = nested.copy()  # Copies outer list only
deep = copy.deepcopy(nested)  # Copies all levels

nested[0].append(99)
print(nested)   # [[1, 2, 99], [3, 4]]
print(shallow)  # [[1, 2, 99], [3, 4]] - inner list shared!
print(deep)     # [[1, 2], [3, 4]] - fully independent
```

---

## 4. Type Checking Patterns

### Runtime Type Checking with `isinstance()`

**Best Practice**: Use `isinstance()` instead of `type()` for type checking.

```python
# ✅ Preferred: isinstance()
def process_data(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sum(data.values())
    else:
        return data

# ❌ Avoid: comparing type() directly
def process_data_bad(data):
    if type(data) == list:  # Less flexible
        return sum(data)
```

**Why `isinstance()` is better**:
- Works with inheritance (advanced topic)
- More Pythonic and readable
- Can check multiple types: `isinstance(x, (int, float))`

### Type Hints (Documentation + IDE Support)

**Type hints** are annotations that document expected types. They don't enforce types at runtime but provide valuable documentation and IDE autocomplete.

```python
# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_average(scores: list) -> float:
    return sum(scores) / len(scores)

# Type hints with specific types (Python 3.9+)
def process_scores(scores: list[float]) -> float:
    return sum(scores) / len(scores)

# Type hints for dictionaries
def get_student_gpa(student: dict[str, float]) -> float:
    return student['gpa']
```

**Benefits**:
1. **Self-documentation**: Function signatures show expected types
2. **IDE autocomplete**: Editor knows what methods are available
3. **Error detection**: Tools like `mypy` can catch type errors before runtime

```python
# Example: IDE autocomplete benefits
def uppercase_name(name: str) -> str:
    # Type hint tells IDE that 'name' is a string
    # IDE will suggest .upper(), .lower(), .split(), etc.
    return name.upper()
```

### Using the `typing` Module (Preview)

For complex types, use the `typing` module:

```python
from typing import List, Dict, Optional, Union

# List of strings
def process_names(names: List[str]) -> int:
    return len(names)

# Dictionary with string keys and integer values
def count_items(inventory: Dict[str, int]) -> int:
    return sum(inventory.values())

# Optional means "can be None"
def find_student(student_id: str) -> Optional[Dict]:
    # Returns dict or None
    return None

# Union means "one of these types"
def format_value(value: Union[int, float, str]) -> str:
    return str(value)
```

We'll explore `typing` in depth in Module 4.

---

## Exercises

### Exercise 1: Identity Detective

Predict the output of the following code. Then run it to check your understanding.

```python
# Part A
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Part A:")
print(f"a == b: {a == b}")  # Predict: ?
print(f"a is b: {a is b}")  # Predict: ?
print(f"a is c: {a is c}")  # Predict: ?

# Part B
x = 100
y = 100
print("\nPart B:")
print(f"x is y: {x is y}")  # Predict: ?

# Part C (surprising!)
str1 = "hello"
str2 = "hello"
print("\nPart C:")
print(f"str1 is str2: {str1 is str2}")  # Predict: ?

# Part D
large_num1 = 1000
large_num2 = 1000
print("\nPart D:")
print(f"large_num1 is large_num2: {large_num1 is large_num2}")  # Predict: ?
```

**Questions**:
1. Why is `a is b` False but `a is c` True?
2. Why might `str1 is str2` be True? (Hint: string interning)
3. What's the difference between small and large integer behavior?

---

### Exercise 2: Mutation Station

For each operation, determine if it creates a **new object** or modifies **in place**.

```python
# Test each operation
numbers = [5, 2, 8, 1, 9]
text = "hello world"
data = {"name": "Alice", "age": 30}

# Operation 1
numbers.sort()  # New object or in-place? ________

# Operation 2
result = sorted(numbers)  # New object or in-place? ________

# Operation 3
upper_text = text.upper()  # New object or in-place? ________

# Operation 4
text.replace("world", "Python")  # New object or in-place? ________

# Operation 5
data["city"] = "Boston"  # New object or in-place? ________

# Operation 6
numbers.append(10)  # New object or in-place? ________

# Operation 7
new_numbers = numbers + [11, 12]  # New object or in-place? ________
```

**Challenge**: Rewrite each in-place operation as a new-object operation, and vice versa.

---

### Exercise 3: Type Explorer

Use `type()`, `dir()`, and `help()` to explore objects.

```python
# Create various objects
number = 42
text = "Python"
items = [1, 2, 3]
person = {"name": "Alice", "age": 30}

# Task 1: Find all methods that start with 'is' for a string
text_methods = [m for m in dir(text) if m.startswith('is')]
print(f"String 'is' methods: {text_methods}")

# Task 2: Find all methods that contain 'add' for a list
# Your code here

# Task 3: Use help() to understand what str.isdigit() does
help(text.isdigit)

# Task 4: Discover a method you've never used before on:
# - integers (hint: check dir(number))
# - lists (hint: look for methods you haven't learned yet)
# - dictionaries (hint: explore dict methods)

# Your exploration code here
```

---

### Exercise 4: Reference Puzzle

Debug the following code. It's supposed to create independent student records, but modifications to one student affect others. Why?

```python
# Buggy code
default_courses = ["MATH101", "ENG101"]

students = []
for name in ["Alice", "Bob", "Charlie"]:
    student = {
        "name": name,
        "courses": default_courses
    }
    students.append(student)

# Try to add a course to Alice
students[0]["courses"].append("COMP3083")

# Print all students
for student in students:
    print(f"{student['name']}: {student['courses']}")

# Expected: Only Alice has COMP3083
# Actual: All students have COMP3083!
```

**Tasks**:
1. Explain why all students have "COMP3083"
2. Fix the code so each student has independent course lists
3. Verify using `id()` that each student's course list is different

---

### Exercise 5: Type Annotation Practice

Add type hints to the following functions:

```python
# Function 1: Calculate total price with tax
def calculate_total(price, tax_rate):
    return price * (1 + tax_rate)

# Function 2: Find students with GPA above threshold
def filter_students(students, min_gpa):
    return [s for s in students if s['gpa'] >= min_gpa]

# Function 3: Create a greeting message
def create_greeting(name, title=None):
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"

# Function 4: Count word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
```

**Hints**:
- Use `float`, `str`, `list`, `dict` as appropriate
- For optional parameters, use `Optional[type]` from `typing`
- For dictionaries, specify key and value types: `Dict[str, int]`

---

### Exercise 6: Memory Model Drawing

For the following code, draw a memory diagram showing:
- Objects (boxes with type and value)
- Variable names (arrows pointing to objects)
- Identity relationships

```python
# Code to visualize
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = a.copy()

a.append(4)
```

**Questions**:
1. After `a.append(4)`, what does each variable reference?
2. Which variables point to the same object?
3. Which variables have equal values (`==`) but different identities?

**Tool**: Use [Python Tutor](https://pythontutor.com/) to visualize and check your understanding!

---

## Key Takeaways

By completing this module, you should understand:

✅ **Everything in Python is an object** with identity, type, and value

✅ **Variables are references**, not containers — they point to objects

✅ **`is` checks identity** (same object), **`==` checks equality** (same value)

✅ **Immutable objects** (int, str, tuple) can't be changed; operations create new objects

✅ **Mutable objects** (list, dict, set) can be modified in place

✅ **Aliasing** can cause unexpected behavior with mutable objects

✅ **Type hints** improve code documentation and IDE support

---

## What's Next?

In **Module 2**, we'll explore the **dot notation philosophy** — understanding `object.method()` as "sending a message to an object." You'll learn the crucial distinction between methods and functions, and master the art of exploring object APIs.

---

## Additional Resources

- [Python Data Model (Official Docs)](https://docs.python.org/3/reference/datamodel.html)
- [Python Tutor - Visualize Code Execution](https://pythontutor.com/)
- [Real Python - Immutability in Python](https://realpython.com/python-immutability/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
