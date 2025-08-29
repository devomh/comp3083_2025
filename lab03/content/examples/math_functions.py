import math
from datetime import datetime
import random

def calculate_circle_area(radius):
    """Calculate the area of a circle using math.pi"""
    return math.pi * radius ** 2

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit temperature"""
    return (celsius * 9/5) + 32

def generate_random_number(min_val, max_val):
    """Generate a random number between min and max values"""
    return random.randint(min_val, max_val)

def get_current_timestamp():
    """Get current date and time as a formatted string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Test the functions ---
# The code below will only run when this script is executed directly
if __name__ == "__main__":
    print(f"Circle area (radius=5): {calculate_circle_area(5):.2f}")
    print(f"25°C in Fahrenheit: {convert_celsius_to_fahrenheit(25)}")
    print(f"Random number (1-100): {generate_random_number(1, 100)}")
    print(f"Current time: {get_current_timestamp()}")
