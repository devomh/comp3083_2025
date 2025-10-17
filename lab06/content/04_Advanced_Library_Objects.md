# Module 4: Advanced Library Objects

## Reinforcement and Extension

You've mastered the core standard library objects. Now let's explore more advanced modules that will elevate your Python skills to a professional level.

**Key Insight**: These modules follow the same patterns you've already learned. The consistent API design across Python's standard library makes learning new modules intuitive.

In this module, we'll explore:
1. **`json`** — Data serialization (OOP perspective)
2. **`math` & `statistics`** — Mathematical operations
3. **`itertools`** — Functional programming and lazy evaluation
4. **`typing`** — Type hints and type safety
5. **`dataclasses`** — Structured data without boilerplate

---

## 1. The `json` Module (Revisited)

You learned JSON in Lab 05. Now let's view it through an **object-oriented lens**.

### The Module as an API

```python
import json

# The json module is an object with consistent method patterns
data = {"name": "Alice", "scores": [85, 92, 78]}

# Serialize to STRING: dumps() = "dump string"
json_string = json.dumps(data, indent=2)
print(json_string)

# Serialize to FILE: dump() = "dump"
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Deserialize from STRING: loads() = "load string"
parsed = json.loads(json_string)
print(parsed)

# Deserialize from FILE: load() = "load"
with open("data.json", "r") as f:
    loaded = json.load(f)
```

**Pattern Recognition**: The `s` suffix means "string" version!
- `dump` / `dumps`
- `load` / `loads`

This pattern appears in other modules too (e.g., `pickle`).

### Type Mapping: Python ↔ JSON

| Python Type | JSON Type |
|-------------|-----------|
| `dict` | object |
| `list`, `tuple` | array |
| `str` | string |
| `int`, `float` | number |
| `True` | true |
| `False` | false |
| `None` | null |

```python
# Python to JSON
python_data = {
    "name": "Alice",
    "age": 30,
    "grades": [85, 92, 78],
    "active": True,
    "address": None
}

json_str = json.dumps(python_data, indent=2)
print(json_str)
# {
#   "name": "Alice",
#   "age": 30,
#   "grades": [85, 92, 78],
#   "active": true,
#   "address": null
# }
```

---

## 2. The `math` and `statistics` Modules

Mathematical operations organized into domain-specific modules.

### The `math` Module

**Constants and common mathematical functions.**

```python
import math

# Mathematical constants
print(math.pi)     # 3.141592653589793
print(math.e)      # 2.718281828459045
print(math.tau)    # 6.283185307179586 (2 * pi)
print(math.inf)    # Infinity
print(math.nan)    # Not a Number

# Rounding functions
print(math.ceil(4.3))   # 5 (round up)
print(math.floor(4.7))  # 4 (round down)
print(math.trunc(4.7))  # 4 (remove decimal part)

# Power and logarithms
print(math.sqrt(16))      # 4.0
print(math.pow(2, 3))     # 8.0 (2^3)
print(math.log(100, 10))  # 2.0 (log base 10)
print(math.log2(8))       # 3.0 (log base 2)
print(math.exp(2))        # 7.389... (e^2)

# Trigonometry (radians!)
print(math.sin(math.pi/2))    # 1.0
print(math.cos(0))             # 1.0
print(math.tan(math.pi/4))     # 1.0

# Convert degrees to radians and back
degrees = 90
radians = math.radians(degrees)
print(f"{degrees}° = {radians} radians")
print(f"sin({degrees}°) = {math.sin(radians)}")

# Convert radians to degrees
print(math.degrees(math.pi))  # 180.0
```

**Practical Example: Compound Interest Calculator**

```python
import math

def compound_interest(principal, rate, compounds_per_year, years):
    """
    Calculate compound interest.

    A = P(1 + r/n)^(nt)
    where:
      P = principal (initial amount)
      r = annual interest rate (as decimal)
      n = number of times interest compounds per year
      t = time in years
    """
    amount = principal * math.pow(1 + rate/compounds_per_year,
                                   compounds_per_year * years)
    return amount

# $1000 at 5% annual interest, compounded monthly, for 10 years
initial = 1000
final = compound_interest(1000, 0.05, 12, 10)
profit = final - initial

print(f"Initial: ${initial:.2f}")
print(f"Final: ${final:.2f}")
print(f"Profit: ${profit:.2f}")
```

### The `statistics` Module

**Statistical analysis of numeric data.**

```python
import statistics

# Sample data: test scores
scores = [85, 92, 78, 90, 88, 95, 73, 89, 91, 87]

# Measures of central tendency
print(f"Mean: {statistics.mean(scores)}")       # 86.8
print(f"Median: {statistics.median(scores)}")   # 88.5
print(f"Mode: {statistics.mode([1,1,2,3,3,3])}")  # 3 (most common)

# Measures of spread
print(f"Std Dev: {statistics.stdev(scores):.2f}")    # 6.63
print(f"Variance: {statistics.variance(scores):.2f}") # 43.96

# Quantiles (percentiles)
print(f"Quartiles: {statistics.quantiles(scores, n=4)}")
# [82.75, 88.5, 91.0] (25th, 50th, 75th percentiles)

# Robust statistics (less affected by outliers)
data_with_outlier = [1, 2, 3, 4, 5, 100]
print(f"Mean: {statistics.mean(data_with_outlier)}")      # 19.17 (affected)
print(f"Median: {statistics.median(data_with_outlier)}")  # 3.5 (robust)
```

**Practical Example: Grade Analyzer**

```python
import statistics
from collections import Counter

def analyze_grades(grades):
    """Comprehensive grade analysis."""
    if not grades:
        return None

    analysis = {
        'count': len(grades),
        'mean': statistics.mean(grades),
        'median': statistics.median(grades),
        'mode': statistics.mode(grades) if len(set(grades)) < len(grades) else None,
        'std_dev': statistics.stdev(grades) if len(grades) > 1 else 0,
        'min': min(grades),
        'max': max(grades),
        'range': max(grades) - min(grades)
    }

    # Letter grade distribution
    def letter_grade(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        elif score >= 60: return 'D'
        else: return 'F'

    letter_grades = [letter_grade(g) for g in grades]
    analysis['distribution'] = dict(Counter(letter_grades))

    return analysis

# Test
scores = [85, 92, 78, 90, 88, 95, 73, 89, 91, 87]
result = analyze_grades(scores)

print(f"Grade Analysis:")
print(f"  Count: {result['count']}")
print(f"  Mean: {result['mean']:.2f}")
print(f"  Median: {result['median']}")
print(f"  Std Dev: {result['std_dev']:.2f}")
print(f"  Range: {result['min']}-{result['max']}")
print(f"  Distribution: {result['distribution']}")
```

---

## 3. The `itertools` Module

**`itertools`** provides functional programming tools for efficient iteration.

**Key Concept**: **Lazy Evaluation** — Iterators generate values on-demand rather than creating entire lists in memory.

### Infinite Iterators

**Warning**: These iterators never end! Use with caution.

```python
from itertools import count, cycle, repeat

# count() - infinite counting
counter = count(start=10, step=2)
for i in counter:
    print(i)
    if i > 20:
        break
# Output: 10, 12, 14, 16, 18, 20

# cycle() - infinite cycling through a sequence
colors = cycle(['red', 'green', 'blue'])
color_list = [next(colors) for _ in range(7)]
print(color_list)
# ['red', 'green', 'blue', 'red', 'green', 'blue', 'red']

# repeat() - repeat a value
fives = repeat(5, times=3)
print(list(fives))  # [5, 5, 5]
```

### Combinatorics

**Generate combinations and permutations.**

```python
from itertools import combinations, permutations, product

items = ['A', 'B', 'C']

# combinations(items, r) - r-length combinations (no repeats, order doesn't matter)
print(list(combinations(items, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# permutations(items, r) - r-length permutations (no repeats, order matters)
print(list(permutations(items, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# product(*iterables) - Cartesian product (like nested loops)
print(list(product(['A', 'B'], [1, 2])))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# product with repeat (like rolling dice multiple times)
dice_rolls = list(product(range(1, 7), repeat=2))  # All possible 2-dice rolls
print(f"Total combinations: {len(dice_rolls)}")  # 36
print(f"Sample: {dice_rolls[:5]}")
```

**Practical Example: Lottery Number Generator**

```python
from itertools import combinations

def generate_lottery_combinations(numbers, pick):
    """Generate all possible lottery combinations."""
    return list(combinations(numbers, pick))

# Pick 6 from 49
lottery_numbers = range(1, 50)
all_combinations = generate_lottery_combinations(lottery_numbers, 6)
print(f"Total possible combinations: {len(all_combinations):,}")
# Total possible combinations: 13,983,816

# Sample combinations
print(f"Sample combinations:")
for combo in all_combinations[:5]:
    print(combo)
```

### Iterators for Chaining and Grouping

```python
from itertools import chain, groupby

# chain() - combine multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined = chain(list1, list2, list3)
print(list(combined))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# groupby() - group consecutive identical elements
data = ['A', 'A', 'B', 'B', 'B', 'C', 'A']
for key, group in groupby(data):
    print(f"{key}: {list(group)}")
# A: ['A', 'A']
# B: ['B', 'B', 'B']
# C: ['C']
# A: ['A']  (Note: not grouped with first A's!)

# groupby with key function
students = [
    ('Alice', 'A'),
    ('Bob', 'B'),
    ('Charlie', 'A'),
    ('Diana', 'B'),
]
# Sort first (groupby requires sorted data)
students.sort(key=lambda s: s[1])
for grade, group in groupby(students, key=lambda s: s[1]):
    names = [name for name, _ in group]
    print(f"Grade {grade}: {names}")
# Grade A: ['Alice', 'Charlie']
# Grade B: ['Bob', 'Diana']
```

---

## 4. The `typing` Module

**Type hints** improve code documentation, IDE support, and error detection.

**Important**: Type hints are **not enforced at runtime** by Python itself. They're for documentation and tooling (like `mypy`).

### Basic Type Hints

```python
# Basic types
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def calculate_average(scores: list) -> float:
    return sum(scores) / len(scores)

# Python 3.9+ - use built-in types directly
def process_scores(scores: list[float]) -> float:
    return sum(scores) / len(scores)

def get_student(student_id: str) -> dict[str, any]:
    return {"id": student_id, "name": "Alice"}
```

### Advanced Type Hints

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any

# List with specific element type
def process_names(names: List[str]) -> int:
    return len(names)

# Dictionary with specific key and value types
def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Tuple with specific element types
def get_coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)  # NYC coordinates

# Optional - can be the type or None
def find_user(user_id: str) -> Optional[Dict[str, Any]]:
    # Returns dict or None if not found
    return None

# Union - one of several types
def format_value(value: Union[int, float, str]) -> str:
    return str(value)

# Any - any type (use sparingly!)
def process_data(data: Any) -> Any:
    return data
```

### Type Aliases

For complex types, create aliases for readability.

```python
from typing import Dict, List, Tuple

# Define type aliases
StudentRecord = Dict[str, Union[str, int, List[float]]]
Coordinates = Tuple[float, float]
GradeBook = Dict[str, List[float]]

# Use aliases in function signatures
def add_student(students: List[StudentRecord],
                student: StudentRecord) -> List[StudentRecord]:
    students.append(student)
    return students

def calculate_distance(point1: Coordinates,
                       point2: Coordinates) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# Clear and readable!
students: List[StudentRecord] = []
alice: StudentRecord = {
    "name": "Alice",
    "id": "12345",
    "gpa": 3.8,
    "scores": [85, 92, 78]
}
```

### Practical Example: Type-Safe Configuration

```python
from typing import Dict, List, Optional, Union

ConfigValue = Union[str, int, float, bool, List, Dict]
Config = Dict[str, ConfigValue]

def load_config(file_path: str) -> Optional[Config]:
    """Load configuration from JSON file."""
    import json
    try:
        with open(file_path) as f:
            config: Config = json.load(f)
            return config
    except FileNotFoundError:
        return None

def get_config_value(config: Config,
                     key: str,
                     default: ConfigValue = None) -> ConfigValue:
    """Get configuration value with default."""
    return config.get(key, default)

def validate_config(config: Config,
                    required_keys: List[str]) -> bool:
    """Check if all required keys are present."""
    return all(key in config for key in required_keys)

# Usage with type hints provides IDE autocomplete
config = load_config("settings.json")
if config:
    db_host: str = get_config_value(config, "database_host", "localhost")
    db_port: int = get_config_value(config, "database_port", 5432)
```

---

## 5. The `dataclasses` Module

**`dataclasses`** automatically generate boilerplate code for classes.

**Bridge to Custom Classes**: Dataclasses use the same syntax as regular classes, but with automatic method generation.

### Basic Dataclass

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    student_id: str
    gpa: float

# Automatic __init__, __repr__, __eq__ generated!
alice = Student(name="Alice", student_id="12345", gpa=3.8)
print(alice)  # Student(name='Alice', student_id='12345', gpa=3.8)

bob = Student("Bob", "67890", 3.5)
print(bob)

# Equality checking works automatically
alice2 = Student("Alice", "12345", 3.8)
print(alice == alice2)  # True (same values)
```

### Dataclass with Default Values

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    student_id: str
    gpa: float = 0.0
    courses: List[str] = field(default_factory=list)
    # default_factory for mutable defaults

# Use defaults
alice = Student(name="Alice", student_id="12345")
print(alice.gpa)  # 0.0
print(alice.courses)  # []

# Override defaults
bob = Student(
    name="Bob",
    student_id="67890",
    gpa=3.5,
    courses=["MATH101", "ENG101"]
)
```

### Adding Methods to Dataclasses

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    student_id: str
    gpa: float
    courses: List[str] = field(default_factory=list)

    def add_course(self, course: str) -> None:
        """Add a course to student's schedule."""
        if course not in self.courses:
            self.courses.append(course)

    def drop_course(self, course: str) -> None:
        """Remove a course from student's schedule."""
        if course in self.courses:
            self.courses.remove(course)

    def course_count(self) -> int:
        """Return number of enrolled courses."""
        return len(self.courses)

    def __str__(self) -> str:
        """Custom string representation."""
        return f"{self.name} (ID: {self.student_id}, GPA: {self.gpa})"

# Usage
alice = Student(name="Alice", student_id="12345", gpa=3.8)
alice.add_course("COMP3083")
alice.add_course("MATH201")
print(alice)
print(f"Courses: {alice.courses}")
print(f"Course count: {alice.course_count()}")
```

### Dataclass Options

```python
from dataclasses import dataclass

# Frozen (immutable) dataclass
@dataclass(frozen=True)
class Point:
    x: float
    y: float

point = Point(3.0, 4.0)
# point.x = 5.0  # Error! Frozen dataclass

# Order comparison
@dataclass(order=True)
class Student:
    name: str
    gpa: float

alice = Student("Alice", 3.8)
bob = Student("Bob", 3.5)
print(alice > bob)  # True (compares by fields in order)
```

---

## Exercises

### Exercise 1: Data Analyzer with Type Safety

Build a statistical analysis tool with proper type hints.

```python
import statistics
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class DataSummary:
    """Summary statistics for a dataset."""
    count: int
    mean: float
    median: float
    std_dev: float
    min_value: float
    max_value: float

def analyze_data(data: List[float]) -> Optional[DataSummary]:
    """
    Analyze numeric data and return summary statistics.
    Returns None if data is empty.
    """
    # Your implementation here
    pass

def load_data_from_json(file_path: str) -> Optional[List[float]]:
    """Load numeric data from JSON file."""
    import json
    # Your implementation here
    pass

def compare_datasets(data1: List[float],
                     data2: List[float]) -> Dict[str, float]:
    """
    Compare two datasets.
    Return dict with differences in mean, median, std_dev.
    """
    # Your implementation here
    pass

# Test your implementation
scores1 = [85, 92, 78, 90, 88]
scores2 = [75, 82, 68, 80, 78]

summary1 = analyze_data(scores1)
summary2 = analyze_data(scores2)
comparison = compare_datasets(scores1, scores2)

print(f"Dataset 1: {summary1}")
print(f"Dataset 2: {summary2}")
print(f"Comparison: {comparison}")
```

---

### Exercise 2: Configuration Validator

Create a configuration file validator with type hints.

```python
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import json

@dataclass
class ConfigSchema:
    """Define expected configuration structure."""
    required_keys: List[str]
    optional_keys: List[str]
    key_types: Dict[str, type]

def load_config(file_path: str) -> Optional[Dict[str, Any]]:
    """Load configuration from JSON file."""
    # Your implementation
    pass

def validate_config(config: Dict[str, Any],
                    schema: ConfigSchema) -> tuple[bool, List[str]]:
    """
    Validate configuration against schema.
    Returns (is_valid, errors)
    """
    errors = []

    # Check required keys
    # Check types
    # Your implementation

    return len(errors) == 0, errors

def get_typed_value(config: Dict[str, Any],
                    key: str,
                    expected_type: type,
                    default: Any = None) -> Any:
    """Get configuration value with type checking."""
    # Your implementation
    pass

# Test
schema = ConfigSchema(
    required_keys=['host', 'port', 'database'],
    optional_keys=['timeout', 'ssl'],
    key_types={
        'host': str,
        'port': int,
        'database': str,
        'timeout': int,
        'ssl': bool
    }
)

config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'mydb',
    'ssl': True
}

is_valid, errors = validate_config(config, schema)
print(f"Valid: {is_valid}")
if errors:
    print(f"Errors: {errors}")
```

---

### Exercise 3: Test Data Generator (Advanced)

Combine `dataclasses`, `random`, and `itertools` to generate realistic test data.

```python
from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta
import random
from itertools import combinations

@dataclass
class Course:
    code: str
    name: str
    credits: int

@dataclass
class Student:
    student_id: str
    name: str
    email: str
    gpa: float
    enrolled_courses: List[str] = field(default_factory=list)
    enrollment_date: datetime = field(default_factory=datetime.now)

    def add_course(self, course_code: str) -> None:
        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)

def generate_student_id() -> str:
    """Generate random 5-digit student ID."""
    # Your implementation
    pass

def generate_realistic_gpa() -> float:
    """
    Generate GPA with realistic distribution.
    Use weighted random selection to favor 3.0-3.5 range.
    """
    # Hint: Use random.choices with weights
    # Your implementation
    pass

def generate_enrollment_date(years_back: int = 4) -> datetime:
    """Generate random enrollment date within past N years."""
    # Your implementation
    pass

def generate_students(count: int,
                      available_courses: List[Course]) -> List[Student]:
    """Generate list of students with random enrollments."""
    # Your implementation
    pass

def find_course_conflicts(students: List[Student]) -> Dict[str, int]:
    """
    Find which course pairs are most commonly taken together.
    Use itertools.combinations to check all course pairs.
    """
    # Your implementation
    pass

# Test
courses = [
    Course("MATH101", "Calculus I", 4),
    Course("ENG101", "English Composition", 3),
    Course("COMP3083", "Intro to Programming", 4),
    Course("PHYS201", "Physics I", 4),
]

random.seed(42)
students = generate_students(20, courses)

print(f"Generated {len(students)} students")
print(f"Sample student: {students[0]}")

conflicts = find_course_conflicts(students)
print(f"\\nCourse pair frequencies: {conflicts}")
```

---

## Key Takeaways

By completing this module, you should be able to:

✅ **Use `json`** module with understanding of its API patterns

✅ **Use `math` and `statistics`** for mathematical and statistical operations

✅ **Use `itertools`** for functional programming and efficient iteration

✅ **Apply type hints** to improve code documentation and IDE support

✅ **Create `dataclasses`** for structured data without boilerplate

✅ **Recognize consistent API patterns** across Python's standard library

✅ **Combine multiple modules** to solve complex problems

---

## What's Next?

You've completed Lab 06! You now understand:
- Object-oriented thinking and the dot notation philosophy
- How to explore and use library APIs independently
- Python's essential standard library modules
- Type hints and modern Python practices

---

## Additional Resources

- [`itertools` module documentation](https://docs.python.org/3/library/itertools.html)
- [`typing` module documentation](https://docs.python.org/3/library/typing.html)
- [`dataclasses` module documentation](https://docs.python.org/3/library/dataclasses.html)
- [mypy - Static Type Checker](http://mypy-lang.org/)
- [PEP 557 - Data Classes](https://peps.python.org/pep-0557/)
- [Real Python - Type Checking](https://realpython.com/python-type-checking/)
