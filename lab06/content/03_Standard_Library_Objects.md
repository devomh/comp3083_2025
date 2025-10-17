# Module 3: Python Standard Library - Core Objects

## Practical Mastery Through Essential Library Objects

Now that you understand object-oriented thinking, let's apply it to Python's **standard library**—a rich collection of pre-built modules that solve common programming problems.

**Key Insight**: Well-designed library objects follow **consistent patterns**. Once you learn one module's API, you can intuitively understand others.

In this module, we'll master four essential modules:
1. **`datetime`** — Date and time operations
2. **`pathlib`** — File system paths
3. **`random`** — Random number generation
4. **`collections`** — Specialized data structures

---

## 1. The `datetime` Module

Date and time handling is ubiquitous in programming. Python's `datetime` module provides powerful objects for working with dates, times, and durations.

### Creating `datetime` Objects

```python
from datetime import datetime, date, time, timedelta

# Get current date and time
now = datetime.now()
print(now)  # 2025-10-16 14:30:45.123456

# Create specific datetime
birthday = datetime(1995, 8, 15, 14, 30)  # Year, month, day, hour, minute
print(birthday)  # 1995-08-15 14:30:00

# Just date (no time)
today = date.today()
print(today)  # 2025-10-16

# Just time (no date)
lunch_time = time(12, 30, 0)  # Hour, minute, second
print(lunch_time)  # 12:30:00
```

**Key Insight**: These are **immutable objects**. Operations create new objects rather than modifying existing ones.

### Accessing `datetime` Attributes (State)

```python
now = datetime.now()

# Date components
print(now.year)    # 2025
print(now.month)   # 10
print(now.day)     # 16

# Time components
print(now.hour)    # 14
print(now.minute)  # 30
print(now.second)  # 45

# Other useful attributes
print(now.weekday())     # 3 (0=Monday, 6=Sunday)
print(now.isoweekday())  # 4 (1=Monday, 7=Sunday)
```

### Formatting Dates: `strftime()` Method

**"String From Time"** — Convert datetime to formatted string.

```python
now = datetime.now()

# Common formats
print(now.strftime("%Y-%m-%d"))           # 2025-10-16
print(now.strftime("%B %d, %Y"))          # October 16, 2025
print(now.strftime("%m/%d/%y"))           # 10/16/25
print(now.strftime("%I:%M %p"))           # 02:30 PM
print(now.strftime("%A, %B %d, %Y"))      # Thursday, October 16, 2025

# Full format
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-10-16 14:30:45
```

**Common Format Codes**:
- `%Y` — 4-digit year (2025)
- `%y` — 2-digit year (25)
- `%m` — Month as number (10)
- `%B` — Month full name (October)
- `%b` — Month short name (Oct)
- `%d` — Day of month (16)
- `%A` — Weekday full name (Thursday)
- `%a` — Weekday short name (Thu)
- `%H` — Hour 24-hour (14)
- `%I` — Hour 12-hour (02)
- `%M` — Minute (30)
- `%S` — Second (45)
- `%p` — AM/PM

### Parsing Dates: `strptime()` Method

**"String Parse Time"** — Convert string to datetime object.

```python
# Parse date strings
date_str = "2025-10-16"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed)  # 2025-10-16 00:00:00

# Parse with different format
date_str = "October 16, 2025"
parsed = datetime.strptime(date_str, "%B %d, %Y")
print(parsed)  # 2025-10-16 00:00:00

# Parse with time
datetime_str = "2025-10-16 14:30:45"
parsed = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2025-10-16 14:30:45
```

### Date Arithmetic with `timedelta`

**`timedelta`** represents a duration (difference between two dates/times).

```python
from datetime import timedelta

# Create timedeltas
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
two_hours = timedelta(hours=2)
mixed = timedelta(days=1, hours=3, minutes=30)

# Add/subtract timedeltas from datetimes
now = datetime.now()
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
in_90_minutes = now + timedelta(minutes=90)

print(f"Now: {now}")
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")

# Calculate difference between dates
birthday = datetime(1995, 8, 15)
today = datetime.now()
age_delta = today - birthday

print(f"Age in days: {age_delta.days}")
print(f"Age in years: {age_delta.days // 365}")
```

### Practical Example: Days Until Event

```python
from datetime import datetime, timedelta

def days_until(event_date_str, event_name):
    """Calculate days until an event."""
    # Parse the event date
    event_date = datetime.strptime(event_date_str, "%Y-%m-%d")

    # Get today's date
    today = datetime.now()

    # Calculate difference
    delta = event_date - today

    if delta.days < 0:
        return f"{event_name} was {abs(delta.days)} days ago"
    elif delta.days == 0:
        return f"{event_name} is TODAY!"
    else:
        return f"{event_name} is in {delta.days} days"

# Test it
print(days_until("2025-12-25", "Christmas"))
print(days_until("2025-11-01", "Project deadline"))
```

---

## 2. The `pathlib` Module

**`pathlib.Path`** is the modern, object-oriented way to work with file system paths in Python.

**Why Use `pathlib`?**
- Cross-platform (works on Windows, Mac, Linux)
- Readable (`.stem` vs. `os.path.splitext(os.path.basename(path))[0]`)
- Safe (built-in existence checks, error handling)
- Elegant (operator overloading with `/`)

### Creating `Path` Objects

```python
from pathlib import Path

# Get current working directory
current_dir = Path.cwd()
print(current_dir)  # /home/user/projects/lab06

# Get home directory
home = Path.home()
print(home)  # /home/user

# Create path from string
data_path = Path("data/students.json")
print(data_path)  # data/students.json

# Build paths with / operator
project_file = Path.cwd() / "src" / "main.py"
print(project_file)  # /home/user/projects/lab06/src/main.py
```

**Key Insight**: The `/` operator is **overloaded** to join path components. This is much cleaner than string concatenation!

### Path Attributes (State)

```python
file_path = Path("/home/user/documents/report.pdf")

# Path components
print(file_path.name)     # report.pdf (filename with extension)
print(file_path.stem)     # report (filename without extension)
print(file_path.suffix)   # .pdf (file extension)
print(file_path.parent)   # /home/user/documents (parent directory)
print(file_path.parents)  # List of all parent directories

# Full path info
print(file_path.absolute())  # Convert to absolute path
print(file_path.is_absolute())  # True (starts with /)
```

### Path Methods (Behavior)

```python
from pathlib import Path

file_path = Path("data/students.json")

# Check existence
if file_path.exists():
    print("File exists!")

# Check type
if file_path.is_file():
    print("It's a file")
elif file_path.is_dir():
    print("It's a directory")

# Create directories
new_dir = Path("output/reports")
new_dir.mkdir(parents=True, exist_ok=True)
# parents=True: create parent dirs if needed
# exist_ok=True: don't error if already exists

# Read/write files directly
content = file_path.read_text()  # Read entire file
file_path.write_text("New content")  # Write entire file

# Read bytes (for binary files)
image_path = Path("photo.jpg")
if image_path.exists():
    image_data = image_path.read_bytes()
```

### Finding Files with `glob()`

**`glob()`** finds files matching a pattern.

```python
from pathlib import Path

# Find all Python files in current directory
current_dir = Path.cwd()
python_files = list(current_dir.glob("*.py"))
print(f"Python files: {python_files}")

# Find recursively (all subdirectories)
all_python = list(current_dir.glob("**/*.py"))
# ** means "all subdirectories recursively"

# Find all JSON files in data directory
data_dir = Path("data")
if data_dir.exists():
    json_files = list(data_dir.glob("*.json"))
    print(f"JSON files: {json_files}")
```

### Practical Example: File Organizer

```python
from pathlib import Path

def organize_by_extension(source_dir):
    """Organize files into folders by extension."""
    source = Path(source_dir)

    if not source.exists():
        print(f"Directory {source} doesn't exist!")
        return

    # Get all files (not directories)
    files = [f for f in source.iterdir() if f.is_file()]

    for file_path in files:
        # Get extension (without the dot)
        ext = file_path.suffix.lstrip('.')

        if not ext:
            ext = "no_extension"

        # Create folder for this extension
        target_dir = source / ext
        target_dir.mkdir(exist_ok=True)

        # Move file
        target_path = target_dir / file_path.name
        print(f"Moving {file_path.name} to {ext}/")
        # file_path.rename(target_path)  # Uncomment to actually move

# Test it
organize_by_extension("downloads")
```

---

## 3. The `random` Module

The `random` module generates pseudo-random numbers and makes random selections.

**Use Cases**: Games, simulations, testing, sampling, shuffling

### Random Number Generation

```python
import random

# Random float between 0.0 and 1.0
print(random.random())  # 0.7384... (changes each time)

# Random integer between a and b (inclusive)
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")  # 1, 2, 3, 4, 5, or 6

# Random float between a and b
temperature = random.uniform(20.0, 30.0)
print(f"Temperature: {temperature:.1f}°C")  # 24.7°C (example)
```

### Random Selection

```python
import random

# Pick one random element
colors = ["red", "green", "blue", "yellow"]
random_color = random.choice(colors)
print(f"Chosen color: {random_color}")

# Pick multiple WITH replacement (can repeat)
samples = random.choices(colors, k=3)
print(f"3 samples (with replacement): {samples}")
# Example: ['red', 'red', 'blue']

# Pick multiple WITHOUT replacement (no repeats)
samples = random.sample(colors, k=2)
print(f"2 samples (without replacement): {samples}")
# Example: ['green', 'yellow']

# Shuffle a list IN PLACE
deck = list(range(1, 53))  # Cards 1-52
random.shuffle(deck)  # Modifies deck in place
print(f"Shuffled deck (first 5): {deck[:5]}")
```

**Key Difference**:
- `choice()` — Pick one
- `choices(k=n)` — Pick n with replacement (can repeat)
- `sample(k=n)` — Pick n without replacement (no repeats)
- `shuffle()` — Randomize entire list in place

### Seeding for Reproducibility

**Seeding** makes "random" sequences reproducible (same seed = same sequence).

```python
import random

# Set seed for reproducibility
random.seed(42)
print(random.randint(1, 100))  # Always 82 with seed 42
print(random.randint(1, 100))  # Always 15 next

# Reset seed to get same sequence again
random.seed(42)
print(random.randint(1, 100))  # 82 again
print(random.randint(1, 100))  # 15 again
```

**When to Use Seeding**:
- **Testing**: Make tests reproducible
- **Debugging**: Reproduce "random" bugs
- **Demonstrations**: Show same output each time

**When NOT to Seed**:
- **Production code**: Want true randomness
- **Games**: Would make game predictable

### Practical Example: Password Generator

```python
import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # All possible characters
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    special = "!@#$%^&*"

    all_chars = lowercase + uppercase + digits + special

    # Ensure at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill remaining with random choices
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle so required chars aren't always first
    random.shuffle(password)

    return ''.join(password)

# Generate passwords
for _ in range(3):
    print(generate_password(16))
# Example output:
# K9@mPx2!aLbNqW7z
# F3#rTyUi8$oPlKm1
# X5%jNhB2!gVcMq9w
```

---

## 4. The `collections` Module

The `collections` module provides specialized container data types beyond basic `list`, `dict`, and `set`.

### `Counter` — Frequency Counting Made Easy

**`Counter`** counts occurrences of elements automatically.

```python
from collections import Counter

# Count letters in text
text = "hello world"
letter_counts = Counter(text)
print(letter_counts)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Count words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words)
print(word_counts)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common elements
print(word_counts.most_common(2))  # [('apple', 3), ('banana', 2)]

# Access counts like a dictionary
print(word_counts['apple'])  # 3
print(word_counts['grape'])  # 0 (doesn't exist, returns 0 not error!)
```

**Why Use `Counter` Instead of Dict?**
- Automatic counting (no need for `dict.get(key, 0) + 1`)
- `most_common()` method for top N
- Returns 0 for missing keys (no KeyError)
- Supports arithmetic operations

```python
# Counter arithmetic
c1 = Counter(['a', 'b', 'a'])
c2 = Counter(['a', 'c'])

print(c1 + c2)  # Counter({'a': 3, 'b': 1, 'c': 1})
print(c1 - c2)  # Counter({'b': 1, 'a': 1})
```

### `defaultdict` — No More KeyError

**`defaultdict`** automatically creates values for missing keys.

```python
from collections import defaultdict

# Regular dict problem
word_index = {}
words = ["hello", "world", "hello"]
for i, word in enumerate(words):
    if word not in word_index:  # Must check existence
        word_index[word] = []
    word_index[word].append(i)

# defaultdict solution
word_index = defaultdict(list)  # list is the "factory function"
words = ["hello", "world", "hello"]
for i, word in enumerate(words):
    word_index[word].append(i)  # No check needed!

print(dict(word_index))  # {'hello': [0, 2], 'world': [1]}
```

**Common Factory Functions**:
```python
from collections import defaultdict

# Default to empty list
index = defaultdict(list)

# Default to 0 (for counting)
counts = defaultdict(int)
counts['apple'] += 1  # No initialization needed

# Default to empty set
groups = defaultdict(set)
groups['fruits'].add('apple')

# Default to custom value
config = defaultdict(lambda: "default_value")
```

### `deque` — Double-Ended Queue

**`deque`** (pronounced "deck") is efficient for adding/removing from both ends.

```python
from collections import deque

# Create deque
queue = deque([1, 2, 3])

# Add to right (end)
queue.append(4)
print(queue)  # deque([1, 2, 3, 4])

# Add to left (beginning)
queue.appendleft(0)
print(queue)  # deque([0, 1, 2, 3, 4])

# Remove from right
last = queue.pop()
print(f"Removed: {last}")  # 4
print(queue)  # deque([0, 1, 2, 3])

# Remove from left
first = queue.popleft()
print(f"Removed: {first}")  # 0
print(queue)  # deque([1, 2, 3])
```

**When to Use `deque`**:
- Task queues (FIFO: first-in-first-out)
- Recent history (with `maxlen`)
- Sliding windows

```python
# Recent history with maxlen
recent = deque(maxlen=3)
for i in range(10):
    recent.append(i)
    print(f"Recent 3: {list(recent)}")

# Output shows only last 3 items
# Recent 3: [7, 8, 9]
```

### `namedtuple` — Lightweight Structured Data

**`namedtuple`** creates tuple subclasses with named fields.

```python
from collections import namedtuple

# Define structure
Student = namedtuple('Student', ['name', 'id', 'gpa'])

# Create instances
alice = Student(name="Alice", id="12345", gpa=3.8)
bob = Student("Bob", "67890", 3.5)  # Can use positional args too

# Access by name (readable!)
print(alice.name)  # Alice
print(alice.gpa)   # 3.8

# Access by index (like tuple)
print(alice[0])    # Alice
print(alice[2])    # 3.8

# Immutable (like tuple)
# alice.gpa = 4.0  # Error! Can't modify

# Convert to dict
print(alice._asdict())
# {'name': 'Alice', 'id': '12345', 'gpa': 3.8}
```

**When to Use `namedtuple`**:
- Lightweight records (alternative to full classes)
- Immutable data structures
- CSV/database rows
- Function returns with multiple values

```python
# Example: Better than returning tuple
def get_user_info(user_id):
    # Instead of: return ("Alice", 30, "alice@example.com")
    UserInfo = namedtuple('UserInfo', ['name', 'age', 'email'])
    return UserInfo("Alice", 30, "alice@example.com")

user = get_user_info(123)
print(user.name)   # Alice - much clearer than user[0]!
print(user.email)  # alice@example.com
```

---

## Exercises

### Exercise 1: Task Scheduler

Build a task management system using `datetime` and `collections`.

```python
from datetime import datetime, timedelta
from collections import namedtuple, defaultdict

# Define Task structure
Task = namedtuple('Task', ['id', 'description', 'due_date', 'completed'])

# Your implementation:

def create_task(task_id, description, days_from_now):
    """Create a task with due date N days from now."""
    # Your code here
    pass

def list_overdue_tasks(tasks):
    """Return list of tasks past their due date."""
    # Your code here
    pass

def tasks_by_week(tasks):
    """Group tasks by week number."""
    # Hint: Use defaultdict and datetime.isocalendar()
    # Your code here
    pass

def days_until_due(task):
    """Return number of days until task is due."""
    # Your code here
    pass

# Test your implementation
tasks = [
    create_task(1, "Complete Lab 06", 3),
    create_task(2, "Study for exam", -2),  # Overdue
    create_task(3, "Project presentation", 10),
]

print("Overdue tasks:", list_overdue_tasks(tasks))
print("Tasks by week:", tasks_by_week(tasks))
```

---

### Exercise 2: File Organizer

Create a utility that organizes files by type using `pathlib`.

```python
from pathlib import Path
from collections import Counter

def analyze_directory(dir_path):
    """
    Analyze a directory and return:
    - Total number of files
    - Total size in bytes
    - File count by extension
    - Largest file
    """
    directory = Path(dir_path)

    if not directory.exists():
        return None

    # Your code here:
    # 1. Get all files (not directories)
    # 2. Count by extension using Counter
    # 3. Calculate total size
    # 4. Find largest file

    pass

def organize_files(source_dir, dry_run=True):
    """
    Organize files into folders by extension.
    If dry_run=True, only print what would be done.
    """
    # Your code here:
    # 1. Create folders for each extension
    # 2. Move (or print move) files to appropriate folders
    # 3. Handle files with no extension

    pass

def find_duplicate_names(dir_path):
    """Find files with the same name but different extensions."""
    # Hint: Use defaultdict to group by stem
    # Your code here
    pass

# Test your implementation
stats = analyze_directory(".")
if stats:
    print(f"Total files: {stats['count']}")
    print(f"Total size: {stats['size']} bytes")
    print(f"Extensions: {stats['extensions']}")
    print(f"Largest: {stats['largest']}")
```

---

### Exercise 3: Data Generator

Build a test data generator using `random` and other modules.

```python
import random
from datetime import datetime, timedelta
from collections import namedtuple

# Define Student structure
Student = namedtuple('Student', ['id', 'name', 'email', 'gpa', 'enrolled_date'])

def generate_student_id():
    """Generate random student ID (5 digits)."""
    # Your code here
    pass

def generate_name():
    """Generate random name from lists."""
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    # Your code here
    pass

def generate_email(name):
    """Generate email from name."""
    # Example: alice.smith@university.edu
    # Your code here
    pass

def generate_gpa():
    """Generate realistic GPA (2.0-4.0)."""
    # Hint: Use random.uniform with realistic distribution
    # Your code here
    pass

def generate_enrollment_date():
    """Generate random date in past 4 years."""
    # Hint: Use datetime and timedelta
    # Your code here
    pass

def generate_students(count):
    """Generate list of random students."""
    students = []
    for _ in range(count):
        # Your code here: combine all generators
        pass
    return students

def generate_course_enrollments(students, courses):
    """
    For each student, enroll in 3-6 random courses.
    Return dict: {student_id: [course_ids]}
    """
    # Hint: Use random.sample to pick courses
    # Your code here
    pass

# Test your implementation
random.seed(42)  # For reproducibility
students = generate_students(10)
for student in students[:3]:
    print(student)

courses = ["MATH101", "ENG101", "COMP3083", "PHYS201", "HIST101"]
enrollments = generate_course_enrollments(students, courses)
print("\\nSample enrollments:", list(enrollments.items())[:2])
```

---

## Key Takeaways

By completing this module, you should be able to:

✅ **Use `datetime`** to create, format, parse, and perform arithmetic on dates

✅ **Use `pathlib.Path`** for cross-platform file system operations

✅ **Use `random`** for number generation, selection, and shuffling

✅ **Use `Counter`** for frequency counting and finding most common items

✅ **Use `defaultdict`** to avoid KeyError when building dictionaries

✅ **Use `deque`** for efficient double-ended queue operations

✅ **Use `namedtuple`** for lightweight structured data

✅ **Recognize patterns** across library APIs (consistent method naming, similar workflows)

---

## What's Next?

In **Module 4**, we'll explore more advanced library objects including `itertools` for functional programming patterns, `typing` for type hints, and `dataclasses` for structured data—your bridge to creating custom classes.

---

## Additional Resources

- [`datetime` module documentation](https://docs.python.org/3/library/datetime.html)
- [`pathlib` module documentation](https://docs.python.org/3/library/pathlib.html)
- [`random` module documentation](https://docs.python.org/3/library/random.html)
- [`collections` module documentation](https://docs.python.org/3/library/collections.html)
- [strftime.org](https://strftime.org/) - Interactive datetime format reference
