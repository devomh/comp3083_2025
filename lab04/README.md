# Introduction to Programming and CS I - Lab 04

## Overview

Lab 04 focuses on mastering fundamental Python data structures and control flow patterns. Students will work extensively with strings, lists, dictionaries, and loops while building practical applications that demonstrate real-world programming scenarios. This lab emphasizes hands-on coding, problem-solving approaches, and JSON data handling as preparation for future API integration.

## Learning Objectives

By the end of this lab, students will be able to:

- Master string manipulation techniques for text processing and validation
- Create and manipulate lists for data collection and processing  
- Utilize dictionaries for structured key-value data relationships
- Implement efficient for and while loops for iteration and data processing
- Apply problem-solving methodologies to break down complex programming challenges
- Work with JSON for data storage, retrieval, and interchange
- Write clean, well-organized code following Python best practices
- Debug and test code systematically using appropriate techniques

## Lab Structure

### Core Content Modules

1. **Strings** - [📖 Guide](content/01_Strings.md) | [📓 Notebook](content/01_Strings.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/lab04/content/01_Strings.ipynb)
   - String creation, indexing, and slicing techniques
   - Essential string methods for cleaning and processing text
   - Advanced formatting with f-strings and format methods
   - Practical applications: validation, parsing, and text analysis

2. **Lists** - [📖 Guide](content/02_Lists.md) | [📓 Notebook](content/02_Lists.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/lab04/content/02_Lists.ipynb)
   - List creation, modification, and organization methods
   - Indexing, slicing, and advanced list operations
   - List comprehensions for efficient data processing
   - Nested lists and complex data structure management

3. **Dictionaries** - [📖 Guide](content/03_Dictionaries.md) | [📓 Notebook](content/03_Dictionaries.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/lab04/content/03_Dictionaries.ipynb)
   - Dictionary fundamentals and key-value relationships
   - Dictionary methods, iteration, and comprehensions
   - Nested dictionaries for complex data representation
   - Practical applications in data management and configuration

4. **Loops** - [📖 Guide](content/04_Loops.md) | [📓 Notebook](content/04_Loops.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/lab04/content/04_Loops.ipynb)
   - For loops with range, enumerate, and multiple iterables
   - While loops for condition-based iteration
   - Loop control with break, continue, and else clauses
   - Practical patterns: accumulator, search, filter, and validation

5. **JSON Data Handling** - [📖 Guide](content/05_JSON.md) | [📓 Notebook](content/05_JSON.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/lab04/content/05_JSON.ipynb)
   - Introduction to JSON format and its importance
   - Converting between Python objects and JSON strings
   - File operations for persistent data storage
   - Error handling and data validation techniques

### Practical Applications

#### **Coding Problems**
- **[10 Practical Problems](content/practical_problems.py)**: Hands-on coding exercises applying all concepts
  1. Text Analyzer - comprehensive text statistics
  2. Grade Calculator - student performance analysis
  3. Contact Manager - data storage and retrieval system
  4. Shopping List Manager - inventory tracking with calculations
  5. Word Frequency Counter - text analysis with filtering
  6. Student Database - complex querying and filtering
  7. Temperature Converter - unit conversion system
  8. Inventory Manager - transaction processing
  9. Simple Calculator - mathematical operations on data sets
  10. Data Validator - comprehensive input validation

### Interactive Learning Options

#### **Multiple Formats Available**
Each lesson is available in multiple formats to suit different learning preferences:

- **📖 Markdown Guides**: Static documentation with explanations and code examples
- **📓 Jupyter Notebooks**: Interactive notebooks for hands-on learning and experimentation
- **🚀 Google Colab**: Cloud-based execution with zero setup required

All notebooks include:
- Interactive code cells for immediate execution
- Comprehensive explanations and theory
- Practical exercises and examples
- Real-world applications and use cases

## Prerequisites

- Completion of Lab 03 (IDE Setup and Environment Management)
- Understanding of basic Python syntax, variables, and functions
- Familiarity with input-compute-output paradigm
- Access to Python development environment (VS Code, Miniconda)

## Getting Started

### Choose Your Learning Path

1. **📖 Static Reading**: Start with the markdown guides to understand concepts theoretically
2. **📓 Local Notebooks**: Download and run Jupyter notebooks locally for hands-on practice
3. **🚀 Cloud Learning**: Click the Colab badges to open notebooks directly in Google Colab (no setup required!)

### Quick Start with Google Colab

The fastest way to get started is using Google Colab - just click any of the "Open In Colab" badges above. No installation or setup required!

### Local Development Setup

```bash
# Navigate to the lab04 directory
cd lab04

# Start Jupyter Lab to work with notebooks locally
jupyter lab

# Or work with the practical problems directly
python content/practical_problems.py
```

### For GitHub Integration

To use the Colab badges with your repository, replace `YOUR_USERNAME/YOUR_REPO_NAME` in the badge URLs with your actual GitHub username and repository name.

## Key Programming Concepts Reinforced

### Data Structures
- **Strings**: Text processing, validation, and formatting
- **Lists**: Sequential data, sorting, and comprehensions
- **Dictionaries**: Key-value mapping, nested structures, and iteration
- **JSON**: Data serialization and external data exchange

### Control Flow
- **For Loops**: Definite iteration with various patterns
- **While Loops**: Indefinite iteration based on conditions
- **Loop Control**: Strategic use of break, continue, and else

### Problem-Solving Methodology
- **Analysis**: Breaking down complex problems into manageable steps
- **Design**: Planning data structures and algorithms before coding
- **Implementation**: Writing clean, readable, and efficient code
- **Testing**: Systematic verification of solution correctness

## Best Practices Emphasized

1. **Code Organization**: Use meaningful variable names and consistent formatting
2. **Error Handling**: Anticipate and handle edge cases gracefully  
3. **Efficiency**: Choose appropriate data structures for specific tasks
4. **Readability**: Write self-documenting code with clear logic flow
5. **Testing**: Verify solutions with multiple test cases and edge conditions

## Troubleshooting Common Issues

### Data Structure Issues
- **Index Errors**: Always check list bounds before accessing elements
- **Key Errors**: Use `.get()` method for safe dictionary access
- **Type Errors**: Validate data types before performing operations

### Loop Problems
- **Infinite Loops**: Ensure while loop conditions eventually become False
- **Modification During Iteration**: Avoid changing lists while iterating over them
- **Off-by-One Errors**: Be careful with range boundaries and indexing

### JSON Handling
- **JSON Decode Errors**: Always use try-except blocks for JSON operations
- **File Not Found**: Check file paths and handle missing files gracefully
- **Data Validation**: Verify JSON structure matches expected format

## Additional Resources

- **Python Official Documentation**: [docs.python.org](https://docs.python.org/3/)
- **JSON Specification**: [json.org](https://www.json.org/)
- **Python Style Guide**: [PEP 8](https://pep8.org/)

Success in this lab demonstrates readiness for more advanced programming concepts and real-world application development!