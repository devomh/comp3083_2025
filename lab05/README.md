# Introduction to Programming and CS I - Lab 05

## JSON Mastery and API Integration

### Overview

Lab 05 is a comprehensive exploration of **JSON (JavaScript Object Notation)**—the universal language of data exchange on the web. This lab builds your mastery from JSON syntax fundamentals through data processing, culminating in real-world API integration. By the end, you'll confidently parse complex JSON structures, transform data, and consume external APIs to build interactive applications.

**Primary Focus**: JSON data manipulation and processing
**Secondary Focus**: HTTP APIs and external data integration

---

## Learning Objectives

By the end of this lab, students will be able to:

### JSON Fundamentals
- ✅ Understand JSON structure, syntax rules, and data types
- ✅ Identify differences between JSON and Python syntax
- ✅ Validate JSON manually and programmatically
- ✅ Serialize Python objects to JSON strings and files
- ✅ Deserialize JSON data into Python data structures

### Data Processing
- ✅ Navigate deeply nested JSON structures safely
- ✅ Query and filter JSON data using comprehensions
- ✅ Transform and restructure JSON objects
- ✅ Merge multiple JSON sources with proper conflict resolution
- ✅ Validate JSON data against custom schemas

### API Integration
- ✅ Understand HTTP request/response cycles
- ✅ Make GET requests to public APIs using Python
- ✅ Parse and process API responses
- ✅ Handle API errors and network failures gracefully
- ✅ Manage API keys securely using environment variables

### Professional Practices
- ✅ Write robust error handling for JSON operations
- ✅ Build modular, reusable data processing functions
- ✅ Apply debugging strategies for JSON parsing issues
- ✅ Follow security best practices for credential management

---

## Lab Structure

### 📚 Core Content Modules

#### **Module 1: JSON Basics and Syntax**
**File**: [01_JSON_Basics.md](content/01_JSON_Basics.md) | **Notebook**: [01_JSON_Basics.ipynb](content/01_JSON_Basics.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lessons/lab05/content/01_JSON_Basics.ipynb)

Foundation before code—master JSON's structure and syntax rules.

**Topics Covered:**
- JSON structure: objects and arrays
- The six JSON data types
- Syntax rules and common pitfalls
- JSON vs. Python: critical differences
- Manual validation techniques

**Embedded Exercises:**
- Syntax sorting game (fix malformed JSON)
- Spot-the-difference (JSON vs Python)
- Manual JSON authoring from descriptions
- Structure identification
- Error detective drills (6 debugging challenges)
- Complex structure building

**Why Start Here**: Understanding JSON syntax *before* coding prevents frustrating debugging sessions later.

---

#### **Module 2: JSON and Python Serialization**
**File**: [02_JSON_Python.md](content/02_JSON_Python.md) | **Notebook**: [02_JSON_Python.ipynb](content/02_JSON_Python.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lessons/lab05/content/02_JSON_Python.ipynb)

Convert between Python objects and JSON using the `json` module.

**Topics Covered:**
- `dumps()` / `loads()` for string operations
- `dump()` / `load()` for file operations
- Type mapping between Python and JSON
- Pretty-printing and formatting
- Comprehensive error handling
- Custom encoders for special types (datetime)

**Key Patterns:**
- Configuration file management
- Safe JSON loading with fallbacks
- Round-trip validation
- Data persistence workflows

**Exercises**: 6 progressive problems from basic serialization to configuration managers.

---

#### **Module 3: JSON Data Processing**
**File**: [03_JSON_Data_Processing.md](content/03_JSON_Data_Processing.md) | **Notebook**: [03_JSON_Data_Processing.ipynb](content/03_JSON_Data_Processing.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lessons/lab05/content/03_JSON_Data_Processing.ipynb)

Real-world JSON manipulation—the skills you'll use daily.

**Topics Covered:**
- Navigating nested structures safely
- Querying with list comprehensions
- Filtering by multiple criteria
- Aggregating statistics
- Data transformation and restructuring
- Deep merging of JSON objects
- Data validation patterns

**Practical Examples:**
- E-commerce order processing
- Student database queries
- Movie database with full CRUD operations
- Configuration overrides

**Exercises**: 5 hands-on problems including product catalogs, data merging, and search functions.

---

#### **Module 4: JSON Practice Problems**
**File**: [04_JSON_Practice_Problems.py](content/04_JSON_Practice_Problems.py)

Comprehensive coding challenges to cement your skills.

**10 Progressive Problems:**
1. **Contact Card Creator** - Basic serialization
2. **Course Catalog Builder** - Structured data creation
3. **Student GPA Calculator** - File I/O and statistics
4. **Inventory Tracker** - Class-based persistence (CRUD operations)
5. **Configuration Validator** - Schema validation
6. **JSON Data Merger** - Multi-source integration
7. **Nested Data Extractor** - Path-based navigation
8. **JSON-Based Search Engine** - Flexible querying
9. **CSV to JSON Converter** - Format transformation
10. **Schema Validator (Advanced)** - Custom validation framework

**Format**: Each problem includes:
- Detailed specifications
- Test cases
- Hidden solutions (try first!)
- Progressive difficulty

---

#### **Module 5: Introduction to APIs**
**File**: [05_API_Basics.md](content/05_API_Basics.md)

Apply your JSON skills to consume real-world web APIs.

**Topics Covered:**
- What are APIs? The request-response cycle
- HTTP fundamentals (methods, status codes, endpoints)
- Browser-based API exploration (no code)
- Making GET requests with Python's `requests` library
- Comprehensive error handling patterns
- API key management with environment variables

**Practical Examples:**
- Age predictor API (no auth required)
- Nationality predictor API
- Multi-API data integration

**Exercises**: 4 hands-on API challenges building from simple requests to multi-source integration.

---

#### **Module 6: Weather Checker Capstone**
**File**: [06_weather_checker.py](content/06_weather_checker.py)

Culminating project combining all lab skills.

**Features:**
- Secure API key management via environment variables
- Live weather data from OpenWeatherMap API
- Nested JSON parsing and data extraction
- Smart weather recommendations
- Query history persistence (local JSON storage)
- Comprehensive error handling
- Offline testing mode with sample data

**Enhancement Challenges:**
- Multi-day forecast
- Multiple city comparison
- Unit conversion (Celsius/Fahrenheit)
- Weather alerts
- Data visualization (matplotlib)
- Response caching
- Location auto-detection

---

### 📦 Supporting Data Files

The [data/](data/) folder contains sample JSON files for exercises:

| File | Purpose |
|------|---------|
| `students.json` | Student records for filtering/querying exercises |
| `movies.json` | Movie database for complex queries and statistics |
| `courses.json` | Course catalog with nested enrollment data |
| `weather_sample.json` | Mock API response for offline testing |
| `config_base.json` | Base configuration for merge exercises |
| `config_override.json` | Override configuration for deep merge practice |
| `broken_sample1.json` | Intentionally malformed JSON for debugging practice |
| `broken_sample2.json` | Additional error detection exercise |

---

## Prerequisites

### Required Knowledge
- Completion of Lab 04 (Strings, Lists, Dictionaries, Loops)
- Python dictionaries and list comprehensions
- Basic file I/O operations
- Understanding of functions and error handling

### Technical Setup
- Python 3.8+ installed
- `requests` library: `pip install requests`
- Text editor or IDE (VS Code recommended)
- Internet connection (for API modules)

---

## Getting Started

### Recommended Learning Path

**Week 1: JSON Fundamentals**
1. Read Module 1 - Complete all syntax exercises
2. Work through Module 2 - Practice serialization
3. Read Module 3 - Study data processing patterns

**Week 2: Practice & Application**
4. Attempt Module 4 problems (at least 5 of 10)
5. Read Module 5 - Understand API concepts
6. Start Module 6 - Register for API key, test basic functionality

**Week 3: Integration & Enhancement**
7. Complete Module 6 with full features
8. Attempt enhancement challenges
9. Review and consolidate learning

### Quick Start

```bash
# Navigate to lab05
cd lab05

# Install dependencies
pip install requests

# Explore sample data
cat data/students.json

# Try practice problems
python content/04_JSON_Practice_Problems.py

# For API work: Set environment variable (see Module 5)
export WEATHER_API_KEY="your-key-here"
python content/06_weather_checker.py
```

---

## Key Programming Concepts Reinforced

### From Previous Labs
- **Strings** (Lab 04): JSON is text-based, string manipulation skills apply
- **Lists** (Lab 04): JSON arrays map directly to Python lists
- **Dictionaries** (Lab 04): JSON objects are Python dictionaries
- **Loops** (Lab 04): Iterating through JSON arrays and object keys
- **Error Handling** (Lab 03): Critical for robust JSON/API operations

### New Concepts
- **Serialization/Deserialization**: Converting between formats
- **Schema Validation**: Ensuring data structure correctness
- **HTTP Protocol**: Request-response cycles
- **API Authentication**: Secure credential management
- **Data Transformation**: Restructuring and merging complex data

---

## Common Challenges & Solutions

### JSON Syntax Errors

**Problem**: `JSONDecodeError: Expecting ',' delimiter`
```python
# ❌ Wrong - trailing comma
{"name": "Alice", "age": 25,}

# ✅ Correct
{"name": "Alice", "age": 25}
```

**Solution**: Review Module 1 syntax rules, use online validators.

---

### Key Errors in Nested Data

**Problem**: `KeyError: 'address'` when accessing `data['user']['address']['city']`

**Solution**: Use safe navigation:
```python
# ✅ Safe method
city = data.get('user', {}).get('address', {}).get('city')

# ✅ Or check before accessing
if 'user' in data and 'address' in data['user']:
    city = data['user']['address']['city']
```

---

### API Request Failures

**Problem**: `ConnectionError` or timeout

**Solution**: Always use error handling:
```python
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = response.json()
except requests.Timeout:
    print("Request timed out")
except requests.ConnectionError:
    print("Network connection error")
```

---

### Environment Variable Not Set

**Problem**: `API key not found` error

**Solution**:
```bash
# Mac/Linux
export WEATHER_API_KEY="your-key-here"

# Windows (PowerShell)
$env:WEATHER_API_KEY="your-key-here"

# Verify it's set
echo $WEATHER_API_KEY  # Mac/Linux
echo $env:WEATHER_API_KEY  # Windows PowerShell
```

---

## Assessment & Success Criteria

Students demonstrate mastery by:

### JSON Fundamentals (40%)
- ✅ Correctly identify and fix JSON syntax errors
- ✅ Serialize/deserialize complex Python objects
- ✅ Navigate nested structures without errors

### Data Processing (35%)
- ✅ Filter and query JSON data accurately
- ✅ Transform data structures as specified
- ✅ Validate data against requirements
- ✅ Complete at least 7 of 10 practice problems

### API Integration (25%)
- ✅ Successfully make API requests
- ✅ Parse API responses correctly
- ✅ Handle errors gracefully
- ✅ Complete weather checker with core features

---

## Additional Resources

### Official Documentation
- [Python `json` Module](https://docs.python.org/3/library/json.html)
- [Python `requests` Library](https://requests.readthedocs.io/)
- [JSON Specification](https://www.json.org/)

### Online Tools
- [JSONLint](https://jsonlint.com/) - Validate JSON syntax
- [JSON Formatter](https://jsonformatter.org/) - Format and beautify JSON
- [Postman](https://www.postman.com/) - API testing tool

### Free APIs for Practice
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Fake REST API
- [PokeAPI](https://pokeapi.co/) - Pokemon data
- [REST Countries](https://restcountries.com/) - Country information
- [OpenWeatherMap](https://openweathermap.org/api) - Weather data

### Debugging Tips
1. **Use online validators** for syntax errors
2. **Print intermediate results** when navigating nested data
3. **Test with small data samples** before processing large files
4. **Check API documentation** for response structure examples
5. **Use `json.dumps(data, indent=2)`** to visualize structure

---

## Extension Projects

Once you've mastered the core content, try these projects:

1. **Personal Finance Tracker**
   - Store transactions in JSON
   - Generate spending reports by category
   - Export data to different formats

2. **Recipe Book Manager**
   - JSON-based recipe storage
   - Search by ingredients or cuisine
   - Generate shopping lists

3. **Multi-API Dashboard**
   - Combine weather, news, and stock APIs
   - Display aggregated information
   - Cache responses for performance

4. **Data Migration Tool**
   - Convert between JSON, CSV, and XML
   - Validate data during conversion
   - Handle large files efficiently

---

## Contributing & Feedback

Found an error? Have suggestions? Please:
- Report issues via your course management system
- Share successful enhancement projects with the class
- Contribute example datasets for peer learning

---

**Lab 05 Complete!** You're now equipped to work with JSON data and integrate external APIs—essential skills for modern software development. These competencies will serve you throughout your programming career, from web development to data science to mobile apps.

**Next Steps**: Lab 06 will build on these data skills as you explore more advanced programming concepts!

---

**Course**: Introduction to Programming and Computer Science I
**Lab**: 05 - JSON Mastery and API Integration
**Last Updated**: October 2025
