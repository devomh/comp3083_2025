# Introduction to Programming and CS I - Lab 06

## Object-Oriented Thinking and Python Standard Library Objects

### Overview

Lab 06 represents a crucial pivot point in your programming journey. You've mastered basic programming constructs, data structures, and external APIs. Now it's time to understand the **object-oriented paradigm**—the philosophy that programming is fundamentally about objects that encapsulate data and behavior.

Rather than diving immediately into class definitions (which can be abstract), we'll build your intuition through Python's standard library. You'll discover that the strings, lists, and dictionaries you've been using are actually sophisticated objects with rich APIs.

**Primary Focus**: Understanding objects, methods, and the dot notation philosophy
**Secondary Focus**: Mastering Python's essential standard library modules

**Core Philosophy**: **"Use objects before you build objects"** — Gain confidence working with well-designed library objects before creating your own classes.

---

## Understanding APIs: A Broader Perspective

An **API (Application Programming Interface)** is a contract defining how software components communicate. It specifies the "rules of engagement"—methods, parameters, and data formats.

### Two Contexts of APIs

**1. Internal APIs: Libraries and Objects**

When you use Python's standard library, you're working with **internal APIs**:

```python
from datetime import datetime
now = datetime.now()  # The API: how you interact with datetime objects
formatted = now.strftime("%Y-%m-%d")  # Another API method
```

The **public methods and attributes** of a class constitute its API. Good API design makes code intuitive and hides internal complexity.

**2. External APIs: Web Services**

APIs over the internet (like those in Lab 05) use HTTP protocols:

```python
response = requests.get("https://api.example.com/users/42")
# The API: URL structure, HTTP methods, JSON format
```

### Why This Matters for Lab 06

Throughout this lab, you're learning to:
- **Use existing APIs** (Python standard library modules)
- **Understand API patterns** (consistent method naming, predictable behavior)
- **Explore APIs independently** (using `dir()` and `help()`)

This prepares you to both **consume** well-designed APIs and eventually **design** your own when creating custom classes in Lab 07.

**Key Insight**: Whether internal (object methods) or external (web services), APIs are about **clear interfaces** that enable different components to work together seamlessly.

---

## Learning Objectives

By the end of this lab, students will be able to:

### Conceptual Understanding
- ✅ Explain the difference between primitive values and reference types
- ✅ Understand that all Python data are objects with identity, type, and value
- ✅ Articulate the "objects receive messages" mental model
- ✅ Distinguish between methods (object behavior) and functions (standalone procedures)

### Technical Skills
- ✅ Use `type()`, `id()`, `is`, and `isinstance()` to inspect objects
- ✅ Navigate API documentation to discover and use object methods
- ✅ Apply dot notation to invoke methods on objects
- ✅ Chain method calls for fluent interfaces
- ✅ Import and use standard library modules effectively

### Practical Application
- ✅ Work with `datetime` objects for date/time operations
- ✅ Use `pathlib.Path` for cross-platform file system operations
- ✅ Leverage `collections` module for specialized data structures
- ✅ Apply `random` module for probabilistic operations
- ✅ Use `typing` for type hints and better code documentation
- ✅ Create structured data with `dataclasses`

---

## Lab Structure

### 📚 Core Content Modules

#### **Module 1: Variables and Types Review**
**File**: [01_Variables_Types_Review.md](content/01_Variables_Types_Review.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab06/content/01_Variables_Types_Review.ipynb)

**Reconceptualizing Variables** — This isn't just review; it's understanding variables as *references to objects*.

**Topics Covered:**
- Everything is an object: `type()`, `id()`, `dir()`
- Identity vs. equality: `is` vs. `==`
- Mutability hierarchy: immutable vs. mutable types
- Type checking patterns: `isinstance()` and type hints

**Key Insights:**
- Why `list.append()` modifies in place but `string.upper()` returns new
- Memory efficiency and copy vs. view semantics
- The "box analogy" for understanding mutability

**Embedded Exercises:**
1. Identity Detective — Predict `is` vs. `==` results
2. Mutation Station — Identify in-place vs. new object operations
3. Type Explorer — Use inspection tools on various objects
4. Reference Puzzle — Debug aliasing issues
5. Type Annotation Practice — Add type hints to functions
6. Memory Model Drawing — Visualize variable references

**Estimated Time**: 45 minutes

---

#### **Module 2: Objects and Methods Fundamentals**
**File**: [02_Objects_Methods.md](content/02_Objects_Methods.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab06/content/02_Objects_Methods.ipynb)

**The Dot Notation Philosophy** — Formalizing `object.method()` as "sending a message to an object."

**Topics Covered:**
- Methods vs. functions: the crucial distinction
- Dot notation: objects as active agents
- Object state (attributes) vs. behavior (methods)
- Method chaining with fluent interfaces
- Self-discovery with `dir()` and `help()`

**Mental Model**: Methods are "verbs that objects can perform" or "messages objects can receive."

**Embedded Exercises:**
1. Method Hunt — Find methods using `dir()` with criteria
2. Method vs. Function Sort — Categorize code patterns
3. Chain Reaction — Rewrite nested calls as method chains
4. State vs. Behavior — Identify attributes vs. methods
5. Documentation Deep Dive — Solve problems using `help()`

**Estimated Time**: 45 minutes

---

#### **Module 3: Python Standard Library - Core Objects**
**File**: [03_Standard_Library_Objects.md](content/03_Standard_Library_Objects.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab06/content/03_Standard_Library_Objects.ipynb)

**Practical Mastery** — Work with Python's most essential library objects.

**Topics Covered:**

**1. `datetime` Module**
- Creating datetime objects
- Formatting with `strftime()` / parsing with `strptime()`
- Date arithmetic with `timedelta`
- Real-world applications: age calculators, countdowns, scheduling

**2. `pathlib.Path` Module**
- Modern, object-oriented file path handling
- Cross-platform path operations
- File system queries and manipulation
- The elegant `/` operator for path joining

**3. `random` Module**
- Random number generation
- Random selection: `choice()`, `choices()`, `sample()`
- Shuffling and seeding for reproducibility
- Applications: simulations, games, testing

**4. `collections` Module**
- `Counter`: Frequency counting made easy
- `defaultdict`: No more KeyError on missing keys
- `deque`: Efficient double-ended queue
- `namedtuple`: Lightweight structured data

**Integrated Exercises:**
1. Task Scheduler — Combine `datetime` and `collections`
2. File Organizer — Build utility with `pathlib`
3. Data Generator — Create test data with `random`

**Estimated Time**: 45 minutes

---

#### **Module 4: Advanced Library Objects**
**File**: [04_Advanced_Library_Objects.md](content/04_Advanced_Library_Objects.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab06/content/04_Advanced_Library_Objects.ipynb)

**Reinforcement and Extension** — Build on patterns from Module 3 with advanced concepts.

**Topics Covered:**

**1. `json` Module (OOP Perspective)**
- Revisit Lab 05 with object-oriented lens
- Module as API: consistent method patterns

**2. `math` and `statistics` Modules**
- Mathematical functions and constants
- Statistical analysis: mean, median, stdev
- Applications: scientific computing, data analysis

**3. `itertools` Module**
- Lazy evaluation and infinite iterators
- Combinatorics: `combinations()`, `permutations()`
- Functional programming patterns
- Memory-efficient iteration

**4. `typing` Module**
- Type hints for documentation and IDE support
- `Optional`, `Union`, `List`, `Dict`
- Type aliases for complex structures
- Professional code quality standards

**5. `dataclasses` Module**
- Structured data without boilerplate
- Bridge to custom classes
- Auto-generated methods
- Type-annotated attributes

**Integrated Exercises:**
1. Data Analyzer — Statistical analysis with type safety
2. Configuration Validator — Type-safe config handling
3. Test Data Generator — Combine `dataclasses`, `random`, `itertools`

**Estimated Time**: 45 minutes

---

## Prerequisites

### Required Knowledge
- Completion of Labs 01-05
- Python dictionaries and list comprehensions
- Basic file I/O operations
- Understanding of functions and error handling
- JSON serialization/deserialization

### Technical Setup
- Python 3.8+ installed
- Text editor or IDE (VS Code recommended)
- Google account for Colab (optional but recommended)

---

## Getting Started

### Recommended Learning Path

**Week 1: Foundations**
1. Read and complete Module 1 (Variables & Types Review)
2. Work through Module 2 (Objects & Methods)
3. Start Module 3 (Core Library Objects)

**Week 2: Practice & Application**
4. Complete Module 3 with all integrated exercises
5. Read and work through Module 4 (Advanced Objects)
6. Practice with real-world scenarios

**Week 3: Mastery**
7. Complete all Module 4 exercises
8. Review and consolidate learning
9. Explore extension projects

### Quick Start

```bash
# Navigate to lab06
cd lab06

# Explore module files
ls content/

# Start with Module 1
# Open in your preferred editor or use Colab
```

---

## Key Programming Concepts

### From Previous Labs
- **Strings** (Lab 04): Now understand as immutable objects with rich methods
- **Lists** (Lab 04): Mutable objects with in-place modification methods
- **Dictionaries** (Lab 04): Key-value objects with powerful query methods
- **JSON** (Lab 05): Serialization as object-to-format transformation
- **Error Handling** (Lab 03): Critical for robust object operations

### New Concepts
- **Object Identity**: Every object has unique identity, type, and value
- **Reference Semantics**: Variables are references to objects, not containers
- **Encapsulation**: Data and behavior bundled together
- **API Design**: Consistent patterns across library modules
- **Type Hints**: Documentation and IDE support through annotations

---

## Common Challenges & Solutions

### Challenge 1: Method Returns `None`

**Problem**: `my_list.sort()` returns `None` instead of sorted list

**Solution**: Mutable objects that modify in place return `None` to signal "I changed myself"
```python
# ❌ Wrong - sort() returns None
result = numbers.sort()  # result is None

# ✅ Correct - use sorted() for new list
result = sorted(numbers)  # new sorted list

# ✅ Or modify in place
numbers.sort()  # numbers is now sorted
```

---

### Challenge 2: String Methods Don't Change String

**Problem**: `my_string.upper()` doesn't change `my_string`

**Solution**: Strings are immutable — methods return new strings
```python
name = "alice"
name.upper()  # ❌ Doesn't change name
print(name)   # Still "alice"

name = name.upper()  # ✅ Assign returned value
print(name)  # Now "ALICE"
```

---

### Challenge 3: When to Use `is` vs. `==`

**Problem**: Confusion about identity vs. equality

**Solution**: Use `==` for value comparison (99% of cases)
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # ✅ True (same values)
print(a is b)  # False (different objects)

# Use 'is' only for:
if value is None:  # ✅ Checking for None
    pass

if a is b:  # Only when checking same object identity
    pass
```

---

### Challenge 4: Path Objects vs. Strings

**Problem**: `AttributeError: 'str' object has no attribute 'read_text'`

**Solution**: Convert strings to Path objects
```python
# ❌ Wrong - string doesn't have Path methods
file_path = "data/file.txt"
content = file_path.read_text()  # ERROR

# ✅ Correct - create Path object
from pathlib import Path
file_path = Path("data/file.txt")
content = file_path.read_text()  # Works!
```

---

## Assessment & Success Criteria

Students demonstrate mastery by:

### Conceptual Understanding (30%)
- ✅ Correctly explain object identity, type, and value
- ✅ Distinguish between methods and functions
- ✅ Understand mutability and its implications

### Technical Proficiency (40%)
- ✅ Use object inspection tools (`type()`, `id()`, `dir()`, `help()`)
- ✅ Navigate API documentation independently
- ✅ Apply appropriate library modules to solve problems
- ✅ Write type-annotated code

### Practical Application (30%)
- ✅ Complete all embedded exercises (Modules 1-2)
- ✅ Successfully complete 2 of 3 integrated exercises per module (Modules 3-4)
- ✅ Demonstrate clean, object-oriented code style

---

## Additional Resources

### Official Documentation
- [Python Standard Library](https://docs.python.org/3/library/index.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Type Hints (PEP 484)](https://peps.python.org/pep-0484/)
- [Dataclasses (PEP 557)](https://peps.python.org/pep-0557/)

### Module-Specific Documentation
- [`datetime` module](https://docs.python.org/3/library/datetime.html)
- [`pathlib` module](https://docs.python.org/3/library/pathlib.html)
- [`collections` module](https://docs.python.org/3/library/collections.html)
- [`itertools` module](https://docs.python.org/3/library/itertools.html)
- [`typing` module](https://docs.python.org/3/library/typing.html)

### Visualization Tools
- [Python Tutor](https://pythontutor.com/) - Visualize code execution and object references
- [Real Python - OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)

### Practice Resources
- [Exercism Python Track](https://exercism.org/tracks/python)
- [Python Morsels](https://www.pythonmorsels.com/)

---

## Troubleshooting

### Issue: Code works in Colab but fails locally
**Cause**: Usually file path differences
**Solution**: Use `Path(__file__).parent` for script-relative paths

### Issue: `JSONDecodeError` when loading files
**Cause**: Manually edited JSON with syntax errors
**Solution**: Always use `json.dump()` to write; validate with JSONLint

### Issue: Timezone-related datetime errors
**Cause**: Mixing naive and aware datetime objects
**Solution**: Stick with naive datetimes for this lab (both without timezone)

---

**Last Updated**: October 2025
