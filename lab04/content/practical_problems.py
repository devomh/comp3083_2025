#!/usr/bin/env python3
"""
Lab 04 - Practical Coding Problems
10 problems applying strings, lists, dictionaries, loops, and functions

Instructions:
- Complete each function according to its description
- Test your solutions using the provided test cases
- Focus on clean, readable code with meaningful variable names
- Use appropriate data structures and control flow
"""

def problem_1_text_analyzer(text):
    """
    Problem 1: Text Analyzer
    
    Analyze a given text string and return statistics about it.
    
    Args:
        text (str): The input text to analyze
    
    Returns:
        dict: A dictionary containing:
            - 'char_count': total number of characters (including spaces)
            - 'word_count': total number of words
            - 'sentence_count': total number of sentences (count periods, exclamation marks, question marks)
            - 'avg_word_length': average length of words (rounded to 2 decimal places)
            - 'longest_word': the longest word in the text
    
    Example:
        text_analyzer("Hello world! How are you?") returns:
        {
            'char_count': 25,
            'word_count': 5, 
            'sentence_count': 2,
            'avg_word_length': 3.6,
            'longest_word': 'Hello'
        }
    """
    # TODO: Implement this function
    pass


def problem_2_grade_calculator(student_grades):
    """
    Problem 2: Grade Calculator
    
    Process a list of student grades and calculate statistics.
    
    Args:
        student_grades (list): List of dictionaries, each containing:
            - 'name': student name (str)
            - 'scores': list of test scores (list of int/float)
    
    Returns:
        dict: A dictionary containing:
            - 'class_average': overall class average (rounded to 2 decimal places)
            - 'highest_average': highest individual student average
            - 'lowest_average': lowest individual student average
            - 'students_above_80': list of student names with averages >= 80
            - 'grade_distribution': dict with letter grades as keys and counts as values
    
    Letter grades: A (>=90), B (80-89), C (70-79), D (60-69), F (<60)
    
    Example:
        Input: [
            {'name': 'Alice', 'scores': [85, 92, 78]},
            {'name': 'Bob', 'scores': [91, 88, 95]}
        ]
    """
    # TODO: Implement this function
    pass


def problem_3_contact_manager(contacts, operation, **kwargs):
    """
    Problem 3: Contact Manager
    
    Manage a contact list with add, search, and update operations.
    
    Args:
        contacts (list): List of contact dictionaries
        operation (str): 'add', 'search', or 'update'
        **kwargs: Additional arguments based on operation
    
    Operations:
        - 'add': Add new contact (requires name, email, phone)
        - 'search': Search contacts by name or email (requires query)
        - 'update': Update existing contact (requires name and fields to update)
    
    Returns:
        For 'add': Updated contacts list
        For 'search': List of matching contacts
        For 'update': Updated contacts list or None if contact not found
    
    Example:
        contacts = [{'name': 'Alice', 'email': 'alice@email.com', 'phone': '555-0101'}]
        contact_manager(contacts, 'search', query='Alice') returns matching contacts
    """
    # TODO: Implement this function
    pass


def problem_4_shopping_list_manager(shopping_list, items_to_add=None, items_to_remove=None):
    """
    Problem 4: Shopping List Manager
    
    Manage a shopping list with quantities and prices.
    
    Args:
        shopping_list (dict): Dictionary with item names as keys and dicts as values
                             Each value dict has 'quantity' and 'price' keys
        items_to_add (dict): Items to add/update {item_name: {'quantity': int, 'price': float}}
        items_to_remove (list): List of item names to remove
    
    Returns:
        dict: Updated shopping list with additional 'total_cost' and 'item_count' keys
    
    Example:
        Input: {'apples': {'quantity': 5, 'price': 1.2}}
        items_to_add: {'bananas': {'quantity': 3, 'price': 0.8}}
        Returns updated list with total cost calculation
    """
    # TODO: Implement this function
    pass


def problem_5_word_frequency_counter(text, min_length=1, case_sensitive=False):
    """
    Problem 5: Word Frequency Counter
    
    Count the frequency of words in a text, with filtering options.
    
    Args:
        text (str): The input text
        min_length (int): Minimum word length to include (default: 1)
        case_sensitive (bool): Whether to consider case (default: False)
    
    Returns:
        dict: Dictionary with words as keys and frequencies as values,
              sorted by frequency (highest first), then alphabetically
    
    Example:
        word_frequency_counter("The quick brown fox jumps over the lazy dog", min_length=3)
        Returns: {'the': 2, 'brown': 1, 'jumps': 1, 'lazy': 1, 'over': 1, 'quick': 1}
    """
    # TODO: Implement this function
    pass


def problem_6_student_database(students, query_type, **criteria):
    """
    Problem 6: Student Database Query System
    
    Query a student database using various criteria.
    
    Args:
        students (list): List of student dictionaries with keys:
                        'id', 'name', 'major', 'year', 'gpa', 'courses'
        query_type (str): 'filter', 'sort', or 'stats'
        **criteria: Query criteria based on query_type
    
    Query Types:
        - 'filter': Filter students (by_major, min_gpa, max_gpa, year, has_course)
        - 'sort': Sort students (by='name'|'gpa'|'year', reverse=False)
        - 'stats': Calculate statistics (returns dict with avg_gpa, total_students, etc.)
    
    Returns:
        list or dict: Filtered/sorted students list or statistics dictionary
    """
    # TODO: Implement this function
    pass


def problem_7_temperature_converter(temperatures, from_unit, to_unit):
    """
    Problem 7: Temperature Converter
    
    Convert temperatures between Celsius, Fahrenheit, and Kelvin.
    
    Args:
        temperatures (list): List of temperature values (numbers)
        from_unit (str): Source unit ('C', 'F', or 'K')
        to_unit (str): Target unit ('C', 'F', or 'K')
    
    Returns:
        list: List of converted temperatures rounded to 2 decimal places
    
    Conversion formulas:
        C to F: (C × 9/5) + 32
        C to K: C + 273.15
        F to C: (F - 32) × 5/9
        F to K: ((F - 32) × 5/9) + 273.15
        K to C: K - 273.15
        K to F: ((K - 273.15) × 9/5) + 32
    
    Example:
        temperature_converter([0, 100], 'C', 'F') returns [32.0, 212.0]
    """
    # TODO: Implement this function
    pass


def problem_8_inventory_manager(inventory, transactions):
    """
    Problem 8: Inventory Management System
    
    Process inventory transactions and update stock levels.
    
    Args:
        inventory (dict): Current inventory {item_name: {'stock': int, 'price': float}}
        transactions (list): List of transaction dictionaries:
                           {'type': 'add'|'sell', 'item': str, 'quantity': int, 'price': float}
    
    Returns:
        dict: Updated inventory with additional summary:
            - 'inventory': updated inventory dict
            - 'total_value': total inventory value
            - 'low_stock': items with stock < 5
            - 'transaction_summary': summary of processed transactions
    
    Rules:
        - 'add' transactions increase stock and may update price
        - 'sell' transactions decrease stock (cannot go below 0)
        - Track which transactions couldn't be completed
    """
    # TODO: Implement this function
    pass


def problem_9_simple_calculator(expression_list):
    """
    Problem 9: Simple Calculator for Lists
    
    Perform mathematical operations on lists of numbers.
    
    Args:
        expression_list (list): List of dictionaries, each containing:
            - 'operation': 'sum', 'average', 'max', 'min', 'range', or 'median'
            - 'numbers': list of numbers to operate on
            - 'label': descriptive label for the calculation
    
    Returns:
        dict: Results dictionary with labels as keys and calculated values as values
    
    Operations:
        - 'sum': Sum of all numbers
        - 'average': Mean of all numbers
        - 'max': Maximum value
        - 'min': Minimum value  
        - 'range': Difference between max and min
        - 'median': Middle value when sorted
    
    Example:
        Input: [{'operation': 'sum', 'numbers': [1, 2, 3], 'label': 'total'}]
        Returns: {'total': 6}
    """
    # TODO: Implement this function
    pass


def problem_10_data_validator(data_list, validation_rules):
    """
    Problem 10: Data Validator
    
    Validate a list of data records against specified rules.
    
    Args:
        data_list (list): List of dictionaries to validate
        validation_rules (dict): Validation rules:
            - 'required_fields': list of required field names
            - 'field_types': dict mapping field names to expected types
            - 'field_ranges': dict with min/max values for numeric fields
            - 'field_patterns': dict with regex patterns for string fields (simplified)
    
    Returns:
        dict: Validation results containing:
            - 'valid_records': list of valid records
            - 'invalid_records': list of invalid records with error details
            - 'summary': dict with counts and error statistics
    
    Example:
        Validate student records for required name, age, and email fields
        with appropriate types and value ranges
    """
    # TODO: Implement this function
    pass


# Test cases for each problem
def test_problems():
    """Test all implemented functions"""
    
    print("Testing Lab 04 Problems...")
    print("=" * 50)
    
    # Test Problem 1
    print("\n1. Text Analyzer Test:")
    text = "Hello world! How are you doing today? Great weather!"
    try:
        result = problem_1_text_analyzer(text)
        print(f"Input: '{text}'")
        print(f"Result: {result}")
    except:
        print("Problem 1 not implemented yet")
    
    # Test Problem 2
    print("\n2. Grade Calculator Test:")
    grades = [
        {'name': 'Alice', 'scores': [85, 92, 78, 90]},
        {'name': 'Bob', 'scores': [91, 88, 95, 87]},
        {'name': 'Charlie', 'scores': [76, 82, 79, 85]}
    ]
    try:
        result = problem_2_grade_calculator(grades)
        print(f"Result: {result}")
    except:
        print("Problem 2 not implemented yet")
    
    # Test Problem 3
    print("\n3. Contact Manager Test:")
    contacts = [
        {'name': 'Alice Johnson', 'email': 'alice@email.com', 'phone': '555-0101'},
        {'name': 'Bob Smith', 'email': 'bob@email.com', 'phone': '555-0102'}
    ]
    try:
        result = problem_3_contact_manager(contacts, 'search', query='Alice')
        print(f"Search result: {result}")
    except:
        print("Problem 3 not implemented yet")
    
    # Test Problem 4
    print("\n4. Shopping List Test:")
    shopping = {
        'apples': {'quantity': 5, 'price': 1.2},
        'bread': {'quantity': 2, 'price': 2.5}
    }
    add_items = {'bananas': {'quantity': 3, 'price': 0.8}}
    try:
        result = problem_4_shopping_list_manager(shopping, items_to_add=add_items)
        print(f"Updated shopping list: {result}")
    except:
        print("Problem 4 not implemented yet")
    
    # Test Problem 5
    print("\n5. Word Frequency Test:")
    text = "the quick brown fox jumps over the lazy brown dog"
    try:
        result = problem_5_word_frequency_counter(text, min_length=3)
        print(f"Word frequencies: {result}")
    except:
        print("Problem 5 not implemented yet")
    
    # Continue with remaining tests...
    print("\n6-10: Implement remaining problems to see their tests")
    
    print("\n" + "=" * 50)
    print("Complete the functions above and run this script to test your solutions!")


if __name__ == "__main__":
    test_problems()