"""
JSON Practice Problems - Lab 05
Introduction to Programming and Computer Science I

⭐ COMPLETE THESE AFTER FINISHING MODULES 1-3 TO TEST YOUR MASTERY ⭐

This file contains 10 progressive JSON manipulation problems
designed to build mastery of JSON processing in Python.

Instructions:
1. Read each problem description carefully
2. Implement the solution in the provided function
3. Test your solution using the test code at the bottom
4. Solutions are provided but try solving on your own first!

Topics covered:
- JSON serialization and deserialization (Modules 1-2)
- Nested structure navigation (Module 3)
- Data filtering and transformation (Module 3)
- File I/O with JSON (Module 2)
- Data validation (Advanced)
- Merging and restructuring (Module 3)

Problem difficulty progression:
- Problems 1-3: Reinforce Modules 1-2 concepts
- Problems 4-7: Extend Module 3 concepts
- Problems 8-10: Challenge problems with new techniques
"""

import json


# ==============================================================================
# PROBLEM 1: Contact Card Creator
# ==============================================================================
def create_contact_card(name, email, phone, hobbies):
    """
    Create a contact card dictionary and return it as a JSON string.

    Args:
        name (str): Person's full name
        email (str): Email address
        phone (str): Phone number
        hobbies (list): List of hobbies

    Returns:
        str: JSON string with pretty formatting (indent=2)

    Example:
        >>> json_str = create_contact_card("Alice", "alice@example.com", "555-0100", ["reading", "coding"])
        >>> print(json_str)
        {
          "name": "Alice",
          "email": "alice@example.com",
          "phone": "555-0100",
          "hobbies": [
            "reading",
            "coding"
          ]
        }
    """
    # TODO: Implement this function
    pass


# ==============================================================================
# PROBLEM 2: Course Catalog Builder
# ==============================================================================
def build_course_catalog(courses_list):
    """
    Build a course catalog from a list of course tuples.

    Args:
        courses_list: List of tuples (code, title, credits, prerequisites)
                     prerequisites is a list of course codes

    Returns:
        str: JSON string representing the catalog

    Example:
        >>> courses = [
        ...     ("COMP1001", "Intro to Computing", 3, []),
        ...     ("COMP2050", "Data Structures", 4, ["COMP1001"])
        ... ]
        >>> catalog = build_course_catalog(courses)
    """
    # TODO: Build a dictionary with structure:
    # {
    #   "courses": [
    #     {"code": "...", "title": "...", "credits": ..., "prerequisites": [...]},
    #     ...
    #   ]
    # }
    # Return as JSON string with indent=2
    pass


# ==============================================================================
# PROBLEM 3: Student GPA Calculator
# ==============================================================================
def calculate_student_gpas(json_file_path):
    """
    Read student records from a JSON file and calculate average GPA.

    The JSON file contains:
    {
      "students": [
        {"name": "Alice", "gpa": 3.8},
        {"name": "Bob", "gpa": 3.6},
        ...
      ]
    }

    Args:
        json_file_path (str): Path to the JSON file

    Returns:
        dict: {
            "total_students": int,
            "average_gpa": float (rounded to 2 decimals),
            "highest_gpa": float,
            "lowest_gpa": float
        }

    Returns None if file not found or invalid JSON.
    """
    # TODO: Implement with proper error handling
    pass


# ==============================================================================
# PROBLEM 4: Inventory Manager with Persistence (Functional Approach)
# ==============================================================================
def load_inventory(filename):
    """
    Load inventory from JSON file. Create new if doesn't exist.

    The inventory is stored as:
    {
      "products": {
        "P001": {"name": "Laptop", "quantity": 10, "price": 999.99},
        "P002": {"name": "Mouse", "quantity": 50, "price": 29.99},
        ...
      }
    }

    Args:
        filename (str): Path to JSON inventory file

    Returns:
        dict: Inventory dictionary with "products" key
    """
    # TODO: Try to load from file, create new structure if file doesn't exist
    # Hint: Use try/except for FileNotFoundError and json.JSONDecodeError
    pass


def save_inventory(inventory, filename):
    """
    Save inventory dictionary to JSON file.

    Args:
        inventory (dict): Inventory dictionary to save
        filename (str): Path to save JSON file

    Returns:
        bool: True if successful, False if error occurred
    """
    # TODO: Save with proper error handling
    # Hint: Use try/except for IOError
    pass


def add_product(inventory, product_id, name, quantity, price):
    """
    Add a new product or update existing product in inventory.

    Args:
        inventory (dict): Inventory dictionary (modified in place)
        product_id (str): Unique product ID
        name (str): Product name
        quantity (int): Product quantity
        price (float): Product price
    """
    # TODO: Add/update product in inventory['products']
    pass


def update_quantity(inventory, product_id, quantity_change):
    """
    Update product quantity (can be positive or negative).

    Args:
        inventory (dict): Inventory dictionary
        product_id (str): Product ID to update
        quantity_change (int): Amount to add (positive) or subtract (negative)

    Returns:
        bool: True if successful, False if product doesn't exist
    """
    # TODO: Check if product exists, update quantity, return True/False
    pass


def get_product(inventory, product_id):
    """
    Get product information.

    Args:
        inventory (dict): Inventory dictionary
        product_id (str): Product ID to retrieve

    Returns:
        dict: Product info dict, or None if not found
    """
    # TODO: Return product or None
    pass


def calculate_total_value(inventory):
    """
    Calculate total value of all inventory (price × quantity for all products).

    Args:
        inventory (dict): Inventory dictionary

    Returns:
        float: Total inventory value
    """
    # TODO: Calculate sum of (price * quantity) for all products
    pass


# ==============================================================================
# PROBLEM 5: Configuration File Validator
# ==============================================================================
def validate_config(json_string):
    """
    Validate a configuration JSON string against required schema.

    Required fields:
    - app_name (string)
    - version (string in format "X.Y" where X and Y are numbers)
    - debug (boolean)
    - database (object with required fields: host, port, name)
      - host (string)
      - port (integer, 1-65535)
      - name (string)

    Args:
        json_string (str): JSON configuration string

    Returns:
        tuple: (is_valid: bool, errors: list of error messages)

    Example:
        >>> valid, errors = validate_config('{"app_name": "MyApp", ...}')
        >>> if valid:
        ...     print("Configuration is valid!")
        ... else:
        ...     for error in errors:
        ...         print(f"  - {error}")
    """
    errors = []

    # TODO: Implement validation logic
    # 1. Try to parse JSON (catch JSONDecodeError)
    # 2. Check all required fields exist
    # 3. Validate data types
    # 4. Validate ranges (port number)
    # 5. Validate version format (regex or split by '.')

    pass


# ==============================================================================
# PROBLEM 6: JSON Data Merger
# ==============================================================================
def merge_json_files(file1_path, file2_path, output_path):
    """
    Merge two JSON files containing lists of records.

    Both files have structure: {"records": [{...}, {...}, ...]}
    Records are merged by "id" field. If same ID appears in both files,
    file2's record takes precedence.

    Args:
        file1_path (str): Path to first JSON file
        file2_path (str): Path to second JSON file
        output_path (str): Path to save merged JSON

    Returns:
        int: Number of records in merged file, or -1 if error

    Example files:
        file1: {"records": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]}
        file2: {"records": [{"id": 2, "name": "B-updated"}, {"id": 3, "name": "C"}]}
        output: {"records": [{"id": 1, "name": "A"}, {"id": 2, "name": "B-updated"}, {"id": 3, "name": "C"}]}
    """
    # TODO: Implement with proper error handling
    pass


# ==============================================================================
# PROBLEM 7: Nested Data Extractor
# ==============================================================================
def extract_nested_field(data, field_path):
    """
    Extract a value from nested JSON using a dot-separated path.

    Args:
        data (dict): Python dictionary (parsed JSON)
        field_path (str): Dot-separated path (e.g., "user.address.city")

    Returns:
        The value at the path, or None if path doesn't exist

    Example:
        >>> data = {"user": {"address": {"city": "Miami", "zip": "33101"}}}
        >>> extract_nested_field(data, "user.address.city")
        'Miami'
        >>> extract_nested_field(data, "user.address.country")
        None
    """
    # TODO: Implement
    # Hint: Split the path by '.' and navigate step by step
    # Use .get() to safely access keys
    pass


# ==============================================================================
# PROBLEM 8: JSON-Based Search Engine
# ==============================================================================
def search_records(json_file_path, **search_criteria):
    """
    Search records in a JSON file by multiple criteria.

    The JSON file contains: {"records": [{...}, {...}, ...]}
    Each record is a dictionary.

    Args:
        json_file_path (str): Path to JSON file
        **search_criteria: Keyword arguments for search
                          (e.g., name="Alice", age=25)

    Returns:
        list: Matching records (empty list if none match or error)

    Example:
        >>> matches = search_records("students.json", major="CS", gpa=3.8)
        >>> # Returns all records where major=="CS" AND gpa==3.8
    """
    # TODO: Implement
    # 1. Load JSON file
    # 2. Filter records matching ALL criteria
    # 3. Handle errors gracefully
    pass


# ==============================================================================
# PROBLEM 9: Data Format Converter
# ==============================================================================
def convert_csv_to_json(csv_string, output_file):
    """
    Convert CSV data (as string) to JSON format.

    CSV format:
        First row is headers
        Subsequent rows are data

    JSON format:
        {"records": [{"header1": "value", "header2": "value", ...}, ...]}

    Args:
        csv_string (str): CSV data as string
        output_file (str): Path to save JSON output

    Returns:
        bool: True if successful, False otherwise

    Example CSV:
        name,age,city
        Alice,25,Miami
        Bob,30,Boston

    Output JSON:
        {
          "records": [
            {"name": "Alice", "age": "25", "city": "Miami"},
            {"name": "Bob", "age": "30", "city": "Boston"}
          ]
        }
    """
    # TODO: Implement
    # Hint: Split by newlines, then by commas
    # First line is headers, rest are data rows
    pass


# ==============================================================================
# PROBLEM 10: JSON Schema Validator (Advanced)
# ==============================================================================
def validate_json_schema(data, schema):
    """
    Validate a Python dict against a simple schema definition.

    Schema format:
    {
      "field_name": {
        "type": "string" | "number" | "boolean" | "object" | "array",
        "required": True | False,
        "min": <number> (for numbers only),
        "max": <number> (for numbers only)
      },
      ...
    }

    Args:
        data (dict): Data to validate
        schema (dict): Schema definition

    Returns:
        tuple: (is_valid: bool, errors: list)

    Example:
        >>> schema = {
        ...     "name": {"type": "string", "required": True},
        ...     "age": {"type": "number", "required": True, "min": 0, "max": 150}
        ... }
        >>> valid, errors = validate_json_schema({"name": "Alice", "age": 25}, schema)
    """
    errors = []

    # TODO: Implement validation logic
    # 1. Check required fields
    # 2. Check types
    # 3. Check ranges for numbers
    # Return (True, []) if valid, (False, [errors]) if invalid

    pass


# ==============================================================================
# TEST CODE
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("JSON Practice Problems - Test Suite")
    print("=" * 70)

    # Test Problem 1
    print("\n--- Problem 1: Contact Card Creator ---")
    try:
        card = create_contact_card("Alice Johnson", "alice@example.com", "555-0100", ["reading", "coding"])
        if card:
            print(card)
        else:
            print("Not implemented yet")
    except Exception as e:
        print(f"Error: {e}")

    # Test Problem 2
    print("\n--- Problem 2: Course Catalog Builder ---")
    try:
        courses = [
            ("COMP1001", "Intro to Computing", 3, []),
            ("COMP2050", "Data Structures", 4, ["COMP1001"]),
            ("COMP3083", "Intro to Programming", 3, ["COMP1001"])
        ]
        catalog = build_course_catalog(courses)
        if catalog:
            print(catalog)
        else:
            print("Not implemented yet")
    except Exception as e:
        print(f"Error: {e}")

    # Test Problem 3
    print("\n--- Problem 3: Student GPA Calculator ---")
    print("(Requires test data file - see solution for details)")

    # Test Problem 4
    print("\n--- Problem 4: Inventory Manager ---")
    try:
        # Load or create inventory
        inventory = load_inventory("test_inventory.json")
        if inventory:
            print("✓ Inventory loaded/created successfully")

            # Test adding a product
            add_product(inventory, "P001", "Laptop", 5, 999.99)
            print("✓ Added product P001")

            # Test saving
            if save_inventory(inventory, "test_inventory.json"):
                print("✓ Inventory saved successfully")

            # Test calculating total value
            total = calculate_total_value(inventory)
            if total is not None:
                print(f"✓ Total inventory value: ${total:.2f}")
        else:
            print("Not implemented yet")
    except Exception as e:
        print(f"Error: {e}")

    # Test Problem 5
    print("\n--- Problem 5: Configuration Validator ---")
    test_config = '''
    {
      "app_name": "TestApp",
      "version": "1.0",
      "debug": true,
      "database": {
        "host": "localhost",
        "port": 5432,
        "name": "testdb"
      }
    }
    '''
    try:
        valid, errors = validate_config(test_config)
        if valid is not None:
            if valid:
                print("✓ Configuration is valid!")
            else:
                print("❌ Configuration errors:")
                for error in errors:
                    print(f"  - {error}")
        else:
            print("Not implemented yet")
    except Exception as e:
        print(f"Error: {e}")

    # Test Problem 7
    print("\n--- Problem 7: Nested Data Extractor ---")
    try:
        test_data = {
            "user": {
                "profile": {
                    "name": "Alice",
                    "address": {
                        "city": "Miami",
                        "zip": "33101"
                    }
                }
            }
        }
        city = extract_nested_field(test_data, "user.profile.address.city")
        if city:
            print(f"Extracted city: {city}")
        else:
            print("Not implemented yet or not found")
    except Exception as e:
        print(f"Error: {e}")

    print("\n" + "=" * 70)
    print("Test suite complete!")
    print("=" * 70)

