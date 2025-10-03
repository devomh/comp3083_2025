"""
JSON Practice Problems - Lab 05
Introduction to Programming and Computer Science I

This file contains 10 progressive JSON manipulation problems
designed to build mastery of JSON processing in Python.

Instructions:
1. Read each problem description carefully
2. Implement the solution in the provided function
3. Test your solution using the test code at the bottom
4. Solutions are provided but try solving on your own first!

Topics covered:
- JSON serialization and deserialization
- Nested structure navigation
- Data filtering and transformation
- File I/O with JSON
- Data validation
- Merging and restructuring
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
# PROBLEM 4: Inventory Tracker with Persistence
# ==============================================================================
class InventoryTracker:
    """
    Manages product inventory with JSON persistence.

    The inventory is stored as:
    {
      "products": {
        "P001": {"name": "Laptop", "quantity": 10, "price": 999.99},
        "P002": {"name": "Mouse", "quantity": 50, "price": 29.99},
        ...
      }
    }
    """

    def __init__(self, filename):
        """Initialize with a JSON file. Create if doesn't exist."""
        self.filename = filename
        self.inventory = {"products": {}}
        # TODO: Load existing inventory or create new file
        pass

    def add_product(self, product_id, name, quantity, price):
        """Add a new product or update existing."""
        # TODO: Implement
        pass

    def update_quantity(self, product_id, quantity_change):
        """
        Update product quantity (can be positive or negative).
        Returns True if successful, False if product doesn't exist.
        """
        # TODO: Implement
        pass

    def get_product(self, product_id):
        """Get product info. Returns None if not found."""
        # TODO: Implement
        pass

    def total_inventory_value(self):
        """Calculate total value of all inventory (price × quantity)."""
        # TODO: Implement
        pass

    def save(self):
        """Save current inventory to JSON file."""
        # TODO: Implement with error handling
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
    print("\n--- Problem 4: Inventory Tracker ---")
    try:
        tracker = InventoryTracker("test_inventory.json")
        print("Inventory tracker initialized")
        # Add tests here after implementation
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


# ==============================================================================
# SOLUTIONS (Scroll down to see solutions)
# ==============================================================================


"""
SOLUTIONS - Try implementing on your own first!

--------------------------------------------------------------------------------
SOLUTION 1: Contact Card Creator
--------------------------------------------------------------------------------
def create_contact_card(name, email, phone, hobbies):
    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "hobbies": hobbies
    }
    return json.dumps(contact, indent=2)


--------------------------------------------------------------------------------
SOLUTION 2: Course Catalog Builder
--------------------------------------------------------------------------------
def build_course_catalog(courses_list):
    catalog = {
        "courses": [
            {
                "code": code,
                "title": title,
                "credits": credits,
                "prerequisites": prereqs
            }
            for code, title, credits, prereqs in courses_list
        ]
    }
    return json.dumps(catalog, indent=2)


--------------------------------------------------------------------------------
SOLUTION 3: Student GPA Calculator
--------------------------------------------------------------------------------
def calculate_student_gpas(json_file_path):
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        students = data['students']
        gpas = [s['gpa'] for s in students]

        return {
            "total_students": len(students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "highest_gpa": max(gpas),
            "lowest_gpa": min(gpas)
        }
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return None


--------------------------------------------------------------------------------
SOLUTION 4: Inventory Tracker
--------------------------------------------------------------------------------
class InventoryTracker:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, 'r') as f:
                self.inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.inventory = {"products": {}}
            self.save()

    def add_product(self, product_id, name, quantity, price):
        self.inventory['products'][product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.save()

    def update_quantity(self, product_id, quantity_change):
        if product_id in self.inventory['products']:
            self.inventory['products'][product_id]['quantity'] += quantity_change
            self.save()
            return True
        return False

    def get_product(self, product_id):
        return self.inventory['products'].get(product_id)

    def total_inventory_value(self):
        return sum(
            p['price'] * p['quantity']
            for p in self.inventory['products'].values()
        )

    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.inventory, f, indent=2)
        except IOError as e:
            print(f"Error saving inventory: {e}")


--------------------------------------------------------------------------------
SOLUTION 5: Configuration Validator
--------------------------------------------------------------------------------
def validate_config(json_string):
    errors = []

    # Parse JSON
    try:
        config = json.loads(json_string)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]

    # Check app_name
    if 'app_name' not in config:
        errors.append("Missing required field: app_name")
    elif not isinstance(config['app_name'], str):
        errors.append("app_name must be a string")

    # Check version
    if 'version' not in config:
        errors.append("Missing required field: version")
    elif not isinstance(config['version'], str):
        errors.append("version must be a string")
    else:
        parts = config['version'].split('.')
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            errors.append("version must be in format 'X.Y' where X and Y are numbers")

    # Check debug
    if 'debug' not in config:
        errors.append("Missing required field: debug")
    elif not isinstance(config['debug'], bool):
        errors.append("debug must be a boolean")

    # Check database
    if 'database' not in config:
        errors.append("Missing required field: database")
    elif not isinstance(config['database'], dict):
        errors.append("database must be an object")
    else:
        db = config['database']
        if 'host' not in db:
            errors.append("database.host is required")
        elif not isinstance(db['host'], str):
            errors.append("database.host must be a string")

        if 'port' not in db:
            errors.append("database.port is required")
        elif not isinstance(db['port'], int):
            errors.append("database.port must be an integer")
        elif not (1 <= db['port'] <= 65535):
            errors.append("database.port must be between 1 and 65535")

        if 'name' not in db:
            errors.append("database.name is required")
        elif not isinstance(db['name'], str):
            errors.append("database.name must be a string")

    return (len(errors) == 0, errors)


--------------------------------------------------------------------------------
SOLUTION 6: JSON Data Merger
--------------------------------------------------------------------------------
def merge_json_files(file1_path, file2_path, output_path):
    try:
        with open(file1_path, 'r') as f:
            data1 = json.load(f)
        with open(file2_path, 'r') as f:
            data2 = json.load(f)

        # Create lookup by ID
        merged_dict = {r['id']: r for r in data1['records']}

        # Override/add from file2
        for record in data2['records']:
            merged_dict[record['id']] = record

        # Convert back to list
        merged = {"records": list(merged_dict.values())}

        with open(output_path, 'w') as f:
            json.dump(merged, f, indent=2)

        return len(merged['records'])

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return -1


--------------------------------------------------------------------------------
SOLUTION 7: Nested Data Extractor
--------------------------------------------------------------------------------
def extract_nested_field(data, field_path):
    keys = field_path.split('.')
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
            if current is None:
                return None
        else:
            return None

    return current


--------------------------------------------------------------------------------
SOLUTION 8: JSON-Based Search Engine
--------------------------------------------------------------------------------
def search_records(json_file_path, **search_criteria):
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        records = data['records']

        # Filter by all criteria
        results = []
        for record in records:
            match = True
            for key, value in search_criteria.items():
                if key not in record or record[key] != value:
                    match = False
                    break
            if match:
                results.append(record)

        return results

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return []


--------------------------------------------------------------------------------
SOLUTION 9: Data Format Converter
--------------------------------------------------------------------------------
def convert_csv_to_json(csv_string, output_file):
    try:
        lines = csv_string.strip().split('\n')
        if len(lines) < 2:
            return False

        headers = lines[0].split(',')
        records = []

        for line in lines[1:]:
            values = line.split(',')
            record = {headers[i]: values[i] for i in range(len(headers))}
            records.append(record)

        output = {"records": records}

        with open(output_file, 'w') as f:
            json.dump(output, f, indent=2)

        return True

    except Exception:
        return False


--------------------------------------------------------------------------------
SOLUTION 10: JSON Schema Validator
--------------------------------------------------------------------------------
def validate_json_schema(data, schema):
    errors = []

    for field_name, rules in schema.items():
        # Check required
        if rules.get('required', False) and field_name not in data:
            errors.append(f"Missing required field: {field_name}")
            continue

        # If field exists, validate type
        if field_name in data:
            value = data[field_name]
            expected_type = rules['type']

            type_map = {
                'string': str,
                'number': (int, float),
                'boolean': bool,
                'object': dict,
                'array': list
            }

            if not isinstance(value, type_map[expected_type]):
                errors.append(f"{field_name} must be of type {expected_type}")
                continue

            # Check ranges for numbers
            if expected_type == 'number':
                if 'min' in rules and value < rules['min']:
                    errors.append(f"{field_name} must be >= {rules['min']}")
                if 'max' in rules and value > rules['max']:
                    errors.append(f"{field_name} must be <= {rules['max']}")

    return (len(errors) == 0, errors)
"""
