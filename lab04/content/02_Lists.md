# Lists in Python

## Overview

Lists are ordered, mutable collections that can store multiple items. They are one of the most versatile data structures in Python, allowing you to store different data types, modify contents, and perform various operations on collections of data.

## List Creation and Basic Operations

### Creating Lists

```python
# Different ways to create lists
numbers = [1, 2, 3, 4, 5]
mixed_list = ["apple", 42, True, 3.14]
empty_list = []
nested_list = [[1, 2], [3, 4], [5, 6]]

# Using list() constructor
from_string = list("Hello")
print(f"From string: {from_string}")

from_range = list(range(1, 6))
print(f"From range: {from_range}")

# List with repeated values
zeros = [0] * 5
print(f"Zeros: {zeros}")
```

### Basic List Properties

```python
fruits = ["apple", "banana", "cherry", "date"]

# Length of list
print(f"Length: {len(fruits)}")

# Check if item exists
print(f"'apple' in fruits: {"apple" in fruits}")
print(f"'orange' in fruits: {"orange" in fruits}")

# List concatenation
more_fruits = ["elderberry", "fig"]
all_fruits = fruits + more_fruits
print(f"All fruits: {all_fruits}")
```

## List Indexing and Slicing

### Indexing

```python
colors = ["red", "green", "blue", "yellow", "orange"]

# Positive indexing
print(f"First color: {colors[0]}")
print(f"Third color: {colors[2]}")

# Negative indexing
print(f"Last color: {colors[-1]}")
print(f"Second to last: {colors[-2]}")
```

### Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end]
print(f"Slice [2:6]: {numbers[2:6]}")
print(f"Slice [:4]: {numbers[:4]}")
print(f"Slice [6:]: {numbers[6:]}")

# Slicing with step [start:end:step]
print(f"Every 2nd element: {numbers[::2]}")
print(f"Reversed list: {numbers[::-1]}")
```

## List Methods and Modification

### Adding Elements

```python
fruits = ["apple", "banana"]
print(f"Initial: {fruits}")

# Add single element to end
fruits.append("cherry")
print(f"Appended: {fruits}")

# Insert element at specific position
fruits.insert(1, "apricot")
print(f"Inserted: {fruits}")

# Add multiple elements
fruits.extend(["date", "elderberry"])
print(f"Extended: {fruits}")
```

### Removing Elements

```python
numbers = [1, 2, 3, 2, 4, 5, 2]
print(f"Initial: {numbers}")

# Remove first occurrence of value
numbers.remove(2)
print(f"Removed 2: {numbers}")

# Remove and return element at index
removed_item = numbers.pop(0)
print(f"Popped index 0: {numbers} (removed: {removed_item})")

# Remove and return last element
last_item = numbers.pop()
print(f"Popped last: {numbers} (removed: {last_item})")

# Clear all elements
numbers.clear()
print(f"Cleared: {numbers}")
```

## List Methods for Organization

### Sorting and Reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
names = ["Alice", "Charlie", "Bob", "Diana"]

# Sort in place (modifies original list)
print(f"Original numbers: {numbers}")
numbers.sort()
print(f"Sorted numbers: {numbers}")

# Sort in descending order
numbers.sort(reverse=True)
print(f"Reverse sorted: {numbers}")

# Create sorted copy (doesn\'t modify original)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(f"Original list: {original}")
print(f"Sorted copy: {sorted_copy}")
```

### Counting and Finding

```python
letters = ['a', 'b', 'a', 'c', 'a', 'b']

# Count occurrences
print(f"Count of 'a': {letters.count('a')}")

# Find index of first occurrence
print(f"Index of 'b': {letters.index('b')}")

# Find index with start parameter
print(f"Index of 'a' after index 1: {letters.index('a', 1)}")
```

## List Comprehensions

List comprehensions provide a concise way to create lists. They are often more readable and performant than using explicit `for` loops.

### Basic List Comprehensions

```python
# Traditional approach
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension approach
squares_comp = [x ** 2 for x in range(1, 6)]

print(f"Squares (loop): {squares}")
print(f"Squares (comprehension): {squares_comp}")
```

### List Comprehensions with Conditions

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Square even numbers only
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Squares of evens: {even_squares}")
```

## Reading Lists from User Input

A common task is to read a list of items from a user.

### Reading a list element by element

```python
# This example requires user input. 
# You can run it in a Python environment.

# n = int(input('Cantidad de elementos: '))
# resultado = []
# for i in range(n):
#     elemento = int(input('Valor: '))
#     resultado.append(elemento)
# print(resultado)
```

### Reading a list from a single line of input

This is a more common and efficient method using `split()`.

```python
# This example requires user input. 
# You can run it in a Python environment.

# cadena = input('Ingrese las notas separadas por comas: ')
# # The split() method creates a list of strings
# notas_str = cadena.split(',')
# # We can use a list comprehension to convert them to numbers
# resultado = [int(e) for e in notas_str]
# print(resultado)
```

## Advanced Practical Examples

### Example 1: Grade Management System

This example uses a list of dictionaries to manage student data, calculates averages, and ranks students.

```python
students = [
    {"name": "Alice", "grades": [85, 92, 78, 90]},
    {"name": "Bob", "grades": [91, 88, 95, 87]},
    {"name": "Charlie", "grades": [76, 82, 79, 85]},
    {"name": "Diana", "grades": [94, 89, 97, 92]}
]

# Calculate averages and add to each student dictionary
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    student["average"] = round(avg, 1)

# Sort students by average grade (highest first)
# The `key` argument takes a function that returns the value to sort by
students.sort(key=lambda s: s["average"], reverse=True)

print("--- Student Rankings ---")
for i, student in enumerate(students, 1):
    print(f"{i}. {student['name']}: {student['average']} avg")

# Find students who are above the class average
class_avg = sum(s["average"] for s in students) / len(students)
above_avg_students = [s["name"] for s in students if s["average"] > class_avg]

print(f"\nClass average: {class_avg:.1f}")
print(f"Students above average: {above_avg_students}")
```

### Example 2: Inventory Management

This example uses a list of dictionaries to represent an inventory, calculates total value, and identifies items that need restocking.

```python
inventory = [
    {"item": "Laptops", "quantity": 15, "price": 999.99},
    {"item": "Mice", "quantity": 50, "price": 25.99},
    {"item": "Keyboards", "quantity": 30, "price": 79.99},
    {"item": "Monitors", "quantity": 8, "price": 299.99}
]

# Calculate total inventory value using a list comprehension and sum()
total_value = sum(item["quantity"] * item["price"] for item in inventory)

# Find low stock items (quantity < 20)
low_stock_items = [item["item"] for item in inventory if item["quantity"] < 20]

# Find the most expensive item
most_expensive = sorted(inventory, key=lambda x: x["price"], reverse=True)[0]

print("\n--- Inventory Report ---")
print(f"Total inventory value: ${total_value:,.2f}")
print(f"Low stock items to reorder: {low_stock_items}")
print(f"Most expensive item: {most_expensive['item']} (${most_expensive['price']:.2f})")
```

## Common Pitfalls and Best Practices

### List Copying
-   Assigning a list to a new variable (`new_list = old_list`) does **not** create a copy. It creates a reference. Both variables point to the same list.
-   To create a true copy (a "shallow copy"), use `old_list.copy()` or `old_list[:]`.
-   For lists containing other lists (nested lists), you need a "deep copy" to copy everything. Use `import copy; new_list = copy.deepcopy(old_list)`.

```python
# Shallow copy vs deep copy
import copy

original = [[1, 2], [3, 4]]

# Shallow copy
shallow_copy = original.copy()
shallow_copy[0][0] = 99
print(f"Original after shallow copy mod: {original}") # Original is modified!

# Deep copy
original = [[1, 2], [3, 4]] # Reset original
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 99
print(f"Original after deep copy mod:  {original}") # Original is NOT modified
```

### Modifying Lists During Iteration
Avoid removing items from a list while you are looping over it. This can lead to skipping items or other unexpected behavior. The best practice is to loop over a *copy* of the list or create a new list with a list comprehension.

```python
# Problematic approach
# numbers = [1, 2, 3, 4, 5, 6]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num) # This will not work as expected!

# Better approach: use a list comprehension
numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = [num for num in numbers if num % 2 != 0]
print(f"Correctly filtered numbers: {filtered_numbers}")
```

---

## Exercises

### 1. List Comprehension Analysis
Determine the result of the following list comprehensions. Try to predict the output before running the code.

```python
# Exercise 1a
edades = [45, 33, 55, 30, 25, 33, 25, 40]
mayoria = [e-21 for e in edades]
print(f"Result of 1a: {mayoria}")

# Exercise 1b
seleccionados = [e for e in edades if e%2==0]
print(f"Result of 1b: {seleccionados}")

# Exercise 1c
cadena = 'A, B; C: D.'
punt = ['.', ',', ':', ';']
resultado = [c for c in cadena if c not in punt and c != ' ']
print(f"Result of 1c: {resultado}")
```

### 2. List Comprehension Construction
Build the following lists using a single list comprehension for each.

```python
# Exercise 2a: Find all integers divisible by 11 between 0 and 500.
divisible_by_11 = [i for i in range(501) if i % 11 == 0]
print(f"Divisible by 11: {divisible_by_11}")

# Exercise 2b: Find all integers between 1 and 100 that contain the digit '3'.
contains_digit_3 = [i for i in range(1, 101) if '3' in str(i)]
print(f"Contains digit 3: {contains_digit_3}")

# Exercise 2c: Calculate the current ages based on a list of birth years.
from datetime import date
nacimientos = [1985, 1992, 2000, 1995, 1990, 2005, 1998]
current_year = date.today().year
current_ages = [current_year - year for year in nacimientos]
print(f"Current ages: {current_ages}")
```
