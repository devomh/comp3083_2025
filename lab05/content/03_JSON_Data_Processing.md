# JSON Data Processing and Manipulation

## Overview

You've learned JSON syntax and how to convert between Python and JSON. Now it's time to master the real-world skill: **processing and manipulating JSON data**. This module covers navigating nested structures, querying data, transforming JSON objects, and building practical data processing pipelines.

### Prerequisites
- JSON syntax fundamentals (Module 1)
- Python JSON serialization (Module 2)
- Python dictionaries, lists, and comprehensions (Lab 04)

## Navigating Nested JSON Structures

Real-world JSON is rarely flat—it contains nested objects and arrays. Mastering navigation is essential.

### Example: E-Commerce Order

```python
import json

order_json = '''
{
  "order_id": "ORD-2025-001",
  "customer": {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "membership": "gold"
  },
  "items": [
    {
      "product_id": "P001",
      "name": "Laptop",
      "price": 999.99,
      "quantity": 1
    },
    {
      "product_id": "P042",
      "name": "Wireless Mouse",
      "price": 29.99,
      "quantity": 2
    }
  ],
  "shipping": {
    "address": {
      "street": "123 Main St",
      "city": "Springfield",
      "state": "IL",
      "zip": "62701"
    },
    "method": "express"
  },
  "total": 1059.97
}
'''

order = json.loads(order_json)
```

### Safe Navigation Techniques

```python
# 1. Direct access (can raise KeyError if key missing)
customer_name = order['customer']['name']
print(f"Customer: {customer_name}")

# 2. Safe access with .get() (returns None if key missing)
membership = order.get('customer', {}).get('membership', 'standard')
print(f"Membership: {membership}")

# 3. Check before accessing
if 'shipping' in order and 'address' in order['shipping']:
    city = order['shipping']['address']['city']
    print(f"Shipping to: {city}")

# 4. Accessing array elements
first_item = order['items'][0]
print(f"First item: {first_item['name']} (${first_item['price']})")

# 5. Iterating through arrays
print("\nAll items:")
for item in order['items']:
    subtotal = item['price'] * item['quantity']
    print(f"  - {item['name']}: {item['quantity']} × ${item['price']} = ${subtotal}")
```

**Output:**
```
Customer: Alice Johnson
Membership: gold
Shipping to: Springfield
First item: Laptop ($999.99)

All items:
  - Laptop: 1 × $999.99 = $999.99
  - Wireless Mouse: 2 × $29.99 = $59.98
```

---

## Querying and Filtering JSON Data

Often you need to search, filter, or extract specific data from JSON structures.

### Example: Student Database

```python
import json

students_json = '''
{
  "university": "Springfield University",
  "students": [
    {"id": "S001", "name": "Alice Johnson", "major": "CS", "gpa": 3.8, "year": 3},
    {"id": "S002", "name": "Bob Smith", "major": "Math", "gpa": 3.6, "year": 2},
    {"id": "S003", "name": "Charlie Davis", "major": "CS", "gpa": 3.9, "year": 4},
    {"id": "S004", "name": "Diana Lee", "major": "Physics", "gpa": 3.5, "year": 3},
    {"id": "S005", "name": "Eve Wilson", "major": "CS", "gpa": 3.75, "year": 2},
    {"id": "S006", "name": "Frank Brown", "major": "Math", "gpa": 3.95, "year": 4}
  ]
}
'''

data = json.loads(students_json)
students = data['students']
```

### Query 1: Find by Criteria

```python
# Find all Computer Science majors
cs_students = [s for s in students if s['major'] == 'CS']
print(f"CS Students: {len(cs_students)}")
for student in cs_students:
    print(f"  - {student['name']} (GPA: {student['gpa']})")
```

### Query 2: Filter by Multiple Conditions

```python
# Find senior CS students with GPA > 3.7
senior_high_achievers = [
    s for s in students
    if s['major'] == 'CS' and s['year'] == 4 and s['gpa'] > 3.7
]

print(f"\nSenior CS students with GPA > 3.7:")
for student in senior_high_achievers:
    print(f"  - {student['name']}: {student['gpa']}")
```

### Query 3: Search by Name

```python
def find_student_by_name(students, name):
    """Find a student by exact name match."""
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None

# Search example
result = find_student_by_name(students, "diana lee")
if result:
    print(f"\nFound: {result['name']} - {result['major']}, Year {result['year']}")
else:
    print("Student not found")
```

### Query 4: Aggregate Statistics

```python
# Calculate various statistics
total_students = len(students)
avg_gpa = sum(s['gpa'] for s in students) / total_students

# GPA by major
majors = {}
for student in students:
    major = student['major']
    if major not in majors:
        majors[major] = []
    majors[major].append(student['gpa'])

print(f"\n--- Statistics ---")
print(f"Total students: {total_students}")
print(f"Average GPA: {avg_gpa:.2f}")
print(f"\nAverage GPA by major:")
for major, gpas in majors.items():
    avg = sum(gpas) / len(gpas)
    print(f"  {major}: {avg:.2f} ({len(gpas)} students)")
```

---

## Transforming JSON Data

Often you need to restructure, modify, or merge JSON data.

### Transform 1: Extracting Subset of Fields

```python
# Extract just names and GPAs
simplified = [
    {"name": s['name'], "gpa": s['gpa']}
    for s in students
]

print(json.dumps(simplified, indent=2))
```

**Output:**
```json
[
  {"name": "Alice Johnson", "gpa": 3.8},
  {"name": "Bob Smith", "gpa": 3.6},
  ...
]
```

### Transform 2: Adding Computed Fields

```python
# Add honor roll status (GPA >= 3.7)
for student in students:
    student['honor_roll'] = student['gpa'] >= 3.7

honor_students = [s['name'] for s in students if s['honor_roll']]
print(f"Honor Roll Students: {', '.join(honor_students)}")
```

### Transform 3: Grouping Data

```python
# Group students by year
by_year = {}
for student in students:
    year = student['year']
    if year not in by_year:
        by_year[year] = []
    by_year[year].append(student)

print("\nStudents by year:")
for year in sorted(by_year.keys()):
    print(f"  Year {year}: {len(by_year[year])} students")
```

### Transform 4: Restructuring for Lookup

```python
# Convert list to dictionary indexed by ID for fast lookup
students_by_id = {s['id']: s for s in students}

# Fast lookup
student = students_by_id.get('S003')
if student:
    print(f"\nQuick lookup - S003: {student['name']}")
```

---

## Merging JSON Objects

Combining multiple JSON sources is a common task.

### Example: Configuration Override

```python
import json

# Base configuration
base_config = {
    "app_name": "Student Portal",
    "version": "1.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "students"
    },
    "features": {
        "dark_mode": False,
        "notifications": True
    }
}

# User overrides
user_config = {
    "database": {
        "host": "prod-db.example.com"  # Override host only
    },
    "features": {
        "dark_mode": True  # Enable dark mode
    }
}

# Shallow merge (only top-level keys)
shallow_merged = {**base_config, **user_config}
print("Shallow merge:")
print(json.dumps(shallow_merged, indent=2))
# Problem: Nested dicts are replaced, not merged!
```

**Output shows problem:**
```json
{
  ...
  "database": {
    "host": "prod-db.example.com"
    // Lost port and name!
  }
}
```

### Deep Merge Function

```python
def deep_merge(base, override):
    """
    Recursively merge two dictionaries.
    Override values take precedence.
    """
    result = base.copy()

    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # Both are dicts, merge recursively
            result[key] = deep_merge(result[key], value)
        else:
            # Override the value
            result[key] = value

    return result

# Proper deep merge
final_config = deep_merge(base_config, user_config)
print("\nDeep merge:")
print(json.dumps(final_config, indent=2))
```

**Output:**
```json
{
  "app_name": "Student Portal",
  "version": "1.0",
  "database": {
    "host": "prod-db.example.com",
    "port": 5432,
    "name": "students"
  },
  "features": {
    "dark_mode": true,
    "notifications": true
  }
}
```

---

## Validating JSON Data

Before processing JSON, especially from external sources, validate its structure.

### Basic Validation

```python
def validate_student_record(student):
    """
    Validate that a student record has all required fields.
    Returns (is_valid, error_message)
    """
    required_fields = ['id', 'name', 'major', 'gpa', 'year']

    # Check all required fields exist
    for field in required_fields:
        if field not in student:
            return False, f"Missing required field: {field}"

    # Validate data types
    if not isinstance(student['name'], str):
        return False, "Name must be a string"

    if not isinstance(student['gpa'], (int, float)):
        return False, "GPA must be a number"

    if not isinstance(student['year'], int):
        return False, "Year must be an integer"

    # Validate ranges
    if not (0.0 <= student['gpa'] <= 4.0):
        return False, f"GPA {student['gpa']} out of valid range (0.0-4.0)"

    if not (1 <= student['year'] <= 4):
        return False, f"Year {student['year']} out of valid range (1-4)"

    return True, "Valid"

# Test validation
test_student = {
    "id": "S999",
    "name": "Test Student",
    "major": "CS",
    "gpa": 3.5,
    "year": 2
}

is_valid, message = validate_student_record(test_student)
print(f"Validation: {message}")

# Test with invalid data
invalid_student = {
    "id": "S888",
    "name": "Invalid Student",
    "major": "Math",
    "gpa": 5.0,  # Invalid!
    "year": 3
}

is_valid, message = validate_student_record(invalid_student)
print(f"Validation: {message}")
```

---

## Practical Example: Movie Database

Let's build a complete movie database processor.

```python
import json

movies_json = '''
{
  "movies": [
    {
      "id": 1,
      "title": "The Matrix",
      "year": 1999,
      "director": "Wachowski Sisters",
      "genres": ["Sci-Fi", "Action"],
      "rating": 8.7,
      "revenue": 463.5
    },
    {
      "id": 2,
      "title": "Inception",
      "year": 2010,
      "director": "Christopher Nolan",
      "genres": ["Sci-Fi", "Thriller"],
      "rating": 8.8,
      "revenue": 829.9
    },
    {
      "id": 3,
      "title": "The Shawshank Redemption",
      "year": 1994,
      "director": "Frank Darabont",
      "genres": ["Drama"],
      "rating": 9.3,
      "revenue": 28.3
    },
    {
      "id": 4,
      "title": "Pulp Fiction",
      "year": 1994,
      "director": "Quentin Tarantino",
      "genres": ["Crime", "Drama"],
      "rating": 8.9,
      "revenue": 213.9
    },
    {
      "id": 5,
      "title": "The Dark Knight",
      "year": 2008,
      "director": "Christopher Nolan",
      "genres": ["Action", "Crime", "Drama"],
      "rating": 9.0,
      "revenue": 1005.0
    }
  ]
}
'''

data = json.loads(movies_json)
movies = data['movies']

class MovieDatabase:
    """Movie database with query and analysis capabilities."""

    def __init__(self, movies):
        self.movies = movies

    def find_by_title(self, title):
        """Search for a movie by title (case-insensitive)."""
        title_lower = title.lower()
        for movie in self.movies:
            if title_lower in movie['title'].lower():
                return movie
        return None

    def filter_by_genre(self, genre):
        """Get all movies of a specific genre."""
        return [m for m in self.movies if genre in m['genres']]

    def filter_by_year_range(self, start_year, end_year):
        """Get movies released within a year range."""
        return [
            m for m in self.movies
            if start_year <= m['year'] <= end_year
        ]

    def top_rated(self, n=5):
        """Get top N highest-rated movies."""
        sorted_movies = sorted(self.movies, key=lambda m: m['rating'], reverse=True)
        return sorted_movies[:n]

    def by_director(self, director):
        """Get all movies by a specific director."""
        return [m for m in self.movies if m['director'] == director]

    def statistics(self):
        """Calculate database statistics."""
        total = len(self.movies)
        avg_rating = sum(m['rating'] for m in self.movies) / total
        total_revenue = sum(m['revenue'] for m in self.movies)

        # Genre count
        genre_count = {}
        for movie in self.movies:
            for genre in movie['genres']:
                genre_count[genre] = genre_count.get(genre, 0) + 1

        return {
            "total_movies": total,
            "average_rating": round(avg_rating, 2),
            "total_revenue_millions": round(total_revenue, 1),
            "genres": genre_count
        }

# Create database and run queries
db = MovieDatabase(movies)

# Query 1: Find a movie
matrix = db.find_by_title("matrix")
if matrix:
    print(f"Found: {matrix['title']} ({matrix['year']}) - Rating: {matrix['rating']}")

# Query 2: Sci-Fi movies
scifi_movies = db.filter_by_genre("Sci-Fi")
print(f"\nSci-Fi movies: {len(scifi_movies)}")
for movie in scifi_movies:
    print(f"  - {movie['title']} ({movie['year']})")

# Query 3: Christopher Nolan films
nolan_films = db.by_director("Christopher Nolan")
print(f"\nChristopher Nolan films:")
for movie in nolan_films:
    print(f"  - {movie['title']}: ${movie['revenue']}M revenue")

# Query 4: Top rated
print(f"\nTop 3 rated movies:")
for i, movie in enumerate(db.top_rated(3), 1):
    print(f"  {i}. {movie['title']}: {movie['rating']}/10")

# Statistics
stats = db.statistics()
print(f"\n--- Database Statistics ---")
print(f"Total movies: {stats['total_movies']}")
print(f"Average rating: {stats['average_rating']}/10")
print(f"Total revenue: ${stats['total_revenue_millions']}M")
print(f"Genres: {stats['genres']}")
```

---

## Exercises

### Exercise 1: Extract Product Information

Given this JSON, extract all product names and their prices:

```python
catalog_json = '''
{
  "store": "Tech Emporium",
  "products": [
    {"id": "P001", "name": "Laptop", "price": 999.99, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 29.99, "stock": 50},
    {"id": "P003", "name": "Keyboard", "price": 79.99, "stock": 30},
    {"id": "P004", "name": "Monitor", "price": 349.99, "stock": 12}
  ]
}
'''
```

Print: `"Laptop: $999.99"` for each product.

<details>
<summary>Solution</summary>

```python
import json

catalog = json.loads(catalog_json)

for product in catalog['products']:
    print(f"{product['name']}: ${product['price']}")
```
</details>

### Exercise 2: Filter and Calculate

Using the catalog above, find:
1. All products under $100
2. Total value of inventory (price × stock for each item)

<details>
<summary>Solution</summary>

```python
import json

catalog = json.loads(catalog_json)
products = catalog['products']

# Products under $100
affordable = [p for p in products if p['price'] < 100]
print("Products under $100:")
for p in affordable:
    print(f"  - {p['name']}: ${p['price']}")

# Total inventory value
total_value = sum(p['price'] * p['stock'] for p in products)
print(f"\nTotal inventory value: ${total_value:,.2f}")
```
</details>

### Exercise 3: Merge Student Records

You have two JSON files: one with basic info, one with contact info. Merge them by student ID.

```python
basic_info = '''
{
  "students": [
    {"id": "S001", "name": "Alice", "major": "CS"},
    {"id": "S002", "name": "Bob", "major": "Math"}
  ]
}
'''

contact_info = '''
{
  "contacts": [
    {"id": "S001", "email": "alice@example.com", "phone": "555-0001"},
    {"id": "S002", "email": "bob@example.com", "phone": "555-0002"}
  ]
}
'''
```

Create a merged structure with all information.

<details>
<summary>Solution</summary>

```python
import json

basic = json.loads(basic_info)
contacts = json.loads(contact_info)

# Create contact lookup by ID
contact_lookup = {c['id']: c for c in contacts['contacts']}

# Merge
merged_students = []
for student in basic['students']:
    student_id = student['id']
    # Merge contact info if available
    if student_id in contact_lookup:
        contact = contact_lookup[student_id]
        merged = {
            **student,
            "email": contact['email'],
            "phone": contact['phone']
        }
        merged_students.append(merged)

print(json.dumps(merged_students, indent=2))
```
</details>

### Exercise 4: Nested Data Extraction

Extract the city names from this nested shipping data:

```python
orders = '''
{
  "orders": [
    {"id": 1, "shipping": {"address": {"city": "Miami", "state": "FL"}}},
    {"id": 2, "shipping": {"address": {"city": "Boston", "state": "MA"}}},
    {"id": 3, "shipping": {"address": {"city": "Seattle", "state": "WA"}}}
  ]
}
'''
```

<details>
<summary>Solution</summary>

```python
import json

data = json.loads(orders)

cities = [order['shipping']['address']['city'] for order in data['orders']]
print(f"Cities: {', '.join(cities)}")
```
</details>

### Exercise 5: Build a Search Function

Create a function `search_movies(movies, **criteria)` that can filter by any combination of year, genre, or minimum rating.

Example usage:
```python
results = search_movies(movies, year=1994, min_rating=8.5)
results = search_movies(movies, genre="Sci-Fi")
```

<details>
<summary>Solution</summary>

```python
def search_movies(movies, **criteria):
    """
    Search movies by flexible criteria.
    Supported: year, genre, min_rating, director
    """
    results = movies

    if 'year' in criteria:
        results = [m for m in results if m['year'] == criteria['year']]

    if 'genre' in criteria:
        results = [m for m in results if criteria['genre'] in m['genres']]

    if 'min_rating' in criteria:
        results = [m for m in results if m['rating'] >= criteria['min_rating']]

    if 'director' in criteria:
        results = [m for m in results if m['director'] == criteria['director']]

    return results

# Test
movies_data = json.loads(movies_json)['movies']

results = search_movies(movies_data, year=1994, min_rating=8.5)
print("1994 movies with rating >= 8.5:")
for movie in results:
    print(f"  - {movie['title']}: {movie['rating']}")

results = search_movies(movies_data, genre="Sci-Fi", min_rating=8.7)
print("\nSci-Fi movies with rating >= 8.7:")
for movie in results:
    print(f"  - {movie['title']}: {movie['rating']}")
```
</details>

---

## Key Takeaways

1. **Safe navigation**: Use `.get()` to avoid KeyErrors
2. **List comprehensions**: Perfect for filtering and transforming JSON arrays
3. **Deep merge**: Needed for nested configuration overrides
4. **Validation**: Always validate external JSON before processing
5. **Restructuring**: Convert lists to dicts for fast lookups
6. **Statistics**: Use `sum()`, `len()`, and comprehensions for aggregation
7. **Modular design**: Create classes/functions for complex operations

**Next Module**: [JSON Practice Problems](04_JSON_Practice_Problems.py)
