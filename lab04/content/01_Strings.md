# Strings in Python

## Overview

Strings are sequences of characters used to represent text data. They are one of the most fundamental data types in Python and essential for processing textual information, user input, and data formatting.

## String Creation and Basic Operations

### Creating Strings

```python
# Different ways to create strings
single_quotes = 'Hello, World!'
double_quotes = "Hello, World!"
triple_quotes = """This is a
multi-line string
that can span several lines"""

# Empty string
empty_string = ""
```

### Basic String Operations

```python
message = "Python Programming"

# Length of string
print(f"Length: {len(message)}")

# Concatenation
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)

# Repetition
separator = "-" * 20
print(separator)
```

## String Indexing and Slicing

### Indexing

```python
text = "Python"

# Positive indexing (starts from 0)
print(text[0])
print(text[1])
print(text[5])

# Negative indexing (starts from -1)
print(text[-1])
print(text[-2])
```

### Slicing

```python
sentence = "Python programming is fun"

# Basic slicing [start:end]
print(sentence[0:6])
print(sentence[7:18])
print(sentence[19:])

# Advanced slicing [start:end:step]
print(sentence[::2])
print(sentence[::-1])
```

## Essential String Methods

### Case Conversion

```python
text = "Hello World"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())
```

### String Cleaning

```python
messy_text = "  Hello, World!  \n"

print(f"Original: '{messy_text}'")
print(f"Stripped: '{messy_text.strip()}'")
print(f"Left-stripped: '{messy_text.lstrip()}'")
print(f"Right-stripped: '{messy_text.rstrip()}'")

# Remove specific characters
text_with_punctuation = "Hello, World!!!"
print(f"Stripped '!!!': '{text_with_punctuation.strip('!')}'")
```

### String Searching and Testing

```python
email = "alice@university.edu"

# Search methods
print(f"Index of '@': {email.find('@')}")
print(f"Count of 'e': {email.count('e')}")
print(f"Starts with 'alice': {email.startswith('alice')}")
print(f"Ends with '.edu': {email.endswith('.edu')}")

# Testing methods
print(f"Is alphabetic? {'hello'.isalpha()}")
print(f"Is numeric? {'12345'.isdigit()}")
print(f"Is alphanumeric? {'Hello123'.isalnum()}")
```

### String Splitting and Joining

```python
# Splitting strings
sentence = "Python is awesome and powerful"
words = sentence.split()
print(f"Words: {words}")

csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(",")
print(f"Fruits: {fruits}")

# Joining strings
word_list = ["Python", "is", "great"]
joined = " ".join(word_list)
print(f"Joined sentence: '{joined}'")
```

### String Replacement

```python
text = "I love Java programming"

# Replace all occurrences
new_text = text.replace("Java", "Python")
print(new_text)

# Replace with limit
text_with_multiple = "ha ha ha ha"
limited_replace = text_with_multiple.replace("ha", "ho", 2)
print(limited_replace)
```

## String Formatting

### F-strings (Recommended - Python 3.6+)

```python
name = "Alice"
age = 25
gpa = 3.847

# Basic f-string formatting
message = f"Hello, {name}! You are {age} years old."
print(message)

# Number formatting
formatted_gpa = f"Your GPA is {gpa:.2f}"
print(formatted_gpa)

# Advanced formatting
width = 10
print(f"Right aligned: '{name:>{width}}'")
print(f"Left aligned: '{name:<{width}}'")
print(f"Center aligned: '{name:^{width}}'")
```

### Format Method

```python
# Using .format() method
template = "Hello, {}! You scored {:.1f}%"
result = template.format("Bob", 87.5)
print(result)

# Named placeholders
template = "Hello, {name}! You scored {score:.1f}%"
result = template.format(name="Charlie", score=92.3)
print(result)
```

## Advanced Practical Examples

These examples integrate multiple string concepts to solve practical problems.

### Example 1: Email Processor

This example parses an email address into its components (username, domain, TLD) and performs basic validation.

```python
def parse_email(email):
    """Parse email address into components if valid."""
    if "@" not in email or email.count('@') != 1:
        return None
    
    username, domain_part = email.split("@", 1)
    
    if "." not in domain_part:
        return None
    
    domain_parts = domain_part.split(".")
    domain = ".".join(domain_parts[:-1])
    tld = domain_parts[-1]
    
    # Basic validation checks
    if not username or not domain or not tld:
        return None
        
    return {
        "username": username,
        "domain": domain,
        "tld": tld,
    }

# Test emails
test_emails = [
    "alice@university.edu",
    "bob.smith@company.com",
    "invalid-email",
    "user@domain",
    "test@site.xyz"
]

print("\n--- Email Analysis ---")
for email in test_emails:
    parsed = parse_email(email)
    print(f"\nEmail: {email}")
    if parsed:
        print(f"  Username: {parsed['username']}")
        print(f"  Domain:   {parsed['domain']}")
        print(f"  TLD:      {parsed['tld']}")
    else:
        print("  Result: Invalid email format")
```

### Example 2: Password Validator

This example checks a password for several requirements to determine its strength.

```python
def validate_password(password):
    """Validate password strength based on a set of rules."""
    requirements = []
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
        requirements.append("✓ At least 8 characters")
    else:
        requirements.append("✗ At least 8 characters")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
        requirements.append("✓ Contains uppercase letter")
    else:
        requirements.append("✗ Contains uppercase letter")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
        requirements.append("✓ Contains lowercase letter")
    else:
        requirements.append("✗ Contains lowercase letter")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
        requirements.append("✓ Contains digit")
    else:
        requirements.append("✗ Contains digit")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
        requirements.append("✓ Contains special character")
    else:
        requirements.append("✗ Contains special character")
    
    # Determine strength
    if score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return strength, requirements

# Test passwords
test_passwords = ["password", "Password123", "MySecurePass123!", "weak"]
for pwd in test_passwords:
    strength, reqs = validate_password(pwd)
    print(f"\nPassword: '{pwd}'")
    print(f"Strength: {strength}")
    for req in reqs:
        print(f"  {req}")
```

## Common Pitfalls and Best Practices

### String Immutability

Strings are **immutable**, meaning they cannot be changed after creation. Any operation that seems to modify a string actually creates a new one.

```python
# This will cause an error!
text = "Hello"
# text[0] = "h" # TypeError: 'str' object does not support item assignment

# Instead, create a new string
text = "h" + text[1:]
print(text)
```

### Efficient String Building

When combining many strings in a loop, using `+` is inefficient because it creates a new string in every iteration. The recommended approach is to append strings to a list and then use `join()`.

```python
# Inefficient for many concatenations
result = ""
for i in range(10):
    result += str(i)

# Efficient approach
numbers = []
for i in range(10):
    numbers.append(str(i))
result = "".join(numbers)
print(f"Efficiently joined string: {result}")
```

## Key Takeaways

1.  **Strings are immutable**: Operations create new strings rather than modifying existing ones.
2.  **F-strings are preferred**: Use them for modern, readable string formatting (Python 3.6+).
3.  **Master the methods**: Use built-in methods like `strip()`, `split()`, `replace()`, and `join()` for common tasks.
4.  **Be mindful of case sensitivity**: Use `.lower()` or `.upper()` for case-insensitive comparisons.
5.  **Build strings efficiently**: Use `join()` for combining many strings.

---

## Exercises

### 1. Whitespace Counter
Write a program that reads a string and shows the number of whitespace characters it contains.
- **a)** Solve using the `count()` method.
- **b)** Solve using string traversal with a `for` loop.

### 2. Word Search
Write a program that asks for a block of text and then a word to search for. The program should print a message indicating whether the word was found in the text.

### 3. Vowel Replacer
Write a program that asks for a sentence and returns the same text with all vowels (`a, e, i, o, u`) replaced by an 'x'. Assume the input text is always lowercase.

### 4. Binary Validator (Challenge)
Write a program that asks for a number in binary format (read as a string) and determines if the input is a valid binary number (i.e., it only contains the characters '0' and '1').

```
```