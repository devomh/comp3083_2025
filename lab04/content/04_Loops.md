# Loops in Python

## Overview

Loops are control structures that allow you to execute a block of code repeatedly. Python provides two main types of loops: `for` loops (for iterating over sequences) and `while` loops (for repeating based on a condition). Mastering loops is essential for processing data, automating repetitive tasks, and implementing algorithms.

## For Loops

`for` loops are used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).

### Looping with `range()`

The `range()` function generates a sequence of numbers, which is useful for looping a specific number of times.

```python
# Loop 5 times, with index from 0 to 4
for i in range(5):
    print(f"Count: {i}")

# Loop from 2 up to (but not including) 8
for i in range(2, 8):
    print(f"Number: {i}")

# Loop from 0 to 10, with a step of 2
for i in range(0, 10, 2):
    print(f"Even: {i}")
```

### Looping over Sequences

```python
# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Looping over a string
for letter in "Python":
    print(f"Letter: {letter}")
```

### `enumerate()` for Index and Value

When you need both the index and the value from a sequence, use `enumerate()`.

```python
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")
```

### Looping Through Dictionaries

```python
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Loop through key-value pairs
for student, grade in student_grades.items():
    print(f"{student} scored {grade}")
```

### Nested For Loops

A loop can be nested inside another loop. This is useful for working with nested data structures like a list of lists (a matrix).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ") # Print items in the same line
    print() # Move to the next line after each row
```

## While Loops

`while` loops repeat as long as a certain condition is true.

### Basic While Loop Structure

```python
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Important: update the condition variable to prevent an infinite loop!

print("Loop finished")
```

### Input Validation Loop

A `while` loop is ideal for repeatedly asking for user input until it meets a certain condition.

```python
# This example requires user input to run.

# while True:
#     user_input = input("Enter a positive number (or 'quit' to exit): ")
#     if user_input.lower() == 'quit':
#         break
#     try:
#         number = float(user_input)
#         if number > 0:
#             print(f"Thank you! You entered: {number}")
#             break
#         else:
#             print("Please enter a POSITIVE number.")
#     except ValueError:
#         print("That's not a valid number. Please try again.")
```

## Loop Control Statements

### `break` Statement

The `break` statement exits the current loop immediately.

```python
# Find the first even number in a list
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
```

### `continue` Statement

The `continue` statement skips the rest of the code in the current iteration and proceeds to the next one.

```python
# Print only the odd numbers
for i in range(1, 11):
    if i % 2 == 0:  # If the number is even, skip to the next iteration
        continue
    print(f"Odd number: {i}")
```

### The `else` Clause in Loops

Loops can have an `else` block that executes only if the loop completes normally (i.e., it was not terminated by a `break` statement).

```python
# Search for a number in a list
numbers = [2, 4, 6, 8, 10]
search_for = 7

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}")
        break
else:
    # This runs only if the loop finishes without a break
    print(f"{search_for} was not found in the list.")
```

## Practical Loop Patterns

### Accumulator Pattern

This pattern involves initializing an "accumulator" variable before the loop and updating it in each iteration.

```python
# Calculate the sum and product of a list of numbers
test_scores = [85, 92, 78, 96, 88]

# Initialize accumulators
total_sum = 0
highest_score = 0

for score in test_scores:
    # Accumulate sum
    total_sum += score
    # Find the maximum value
    if score > highest_score:
        highest_score = score

average = total_sum / len(test_scores)

print(f"Scores: {test_scores}")
print(f"Average: {average:.1f}")
print(f"Highest Score: {highest_score}")
```

### Filter and Transform Pattern

This pattern involves iterating through a sequence, filtering out items that meet a certain condition, and then transforming the remaining items.

```python
# Filter for even numbers and then square them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = []
for num in numbers:
    if num % 2 == 0:  # 1. Filter for even numbers
        even_squares.append(num ** 2)  # 2. Transform the number (square it)

print(f"Original numbers: {numbers}")
print(f"Even squares: {even_squares}")

# This is often done more concisely with a list comprehension
even_squares_comp = [num ** 2 for num in numbers if num % 2 == 0]
print(f"Even squares (comprehension): {even_squares_comp}")
```

## Advanced Loop Techniques

### `zip()` for Parallel Iteration

Use `zip()` to iterate over multiple sequences at the same time.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [20, 22, 21]
majors = ["CS", "Math", "Physics"]

for name, age, major in zip(names, ages, majors):
    print(f"{name} is {age} years old and studies {major}")
```

---

## Exercises

### `while` Loop Exercises

1.  **First n Even Numbers**: Write a program that prints the first `n` even numbers (starting from 2). Let `n=10`.
2.  **Sum Formula with `while`**: Using a `while` loop, find the sum of the series: 3 + 6 + 9 + ... + 60.

### `for` Loop Exercises

1.  **Factorial with `for`**: Using a `for` loop, find the factorial of 15 (1 × 2 × 3 × ... × 15).
2.  **Multiplication Table**: Write a program that prints the multiplication table for a number entered by the user. If the user enters `4`, the output should be:
    ```
    4 x 1 = 4
    4 x 2 = 8
    ...
    4 x 12 = 48
    ```
3.  **Range Sum**: Write a program that, given two integers `m` and `n` where `m <= n`, finds the sum of all numbers from `m` to `n` (inclusive).

