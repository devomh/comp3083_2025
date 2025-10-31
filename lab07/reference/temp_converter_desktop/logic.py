"""
Business logic for temperature conversion.

This module contains the core conversion logic, separated from UI code.
This allows for:
- Easy testing without UI
- Reuse in different contexts (CLI, web, desktop)
- Clear separation of concerns
"""


def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature between different units.

    Args:
        value (float): Temperature value to convert
        from_unit (str): Source unit ('Celsius', 'Fahrenheit', or 'Kelvin')
        to_unit (str): Target unit ('Celsius', 'Fahrenheit', or 'Kelvin')

    Returns:
        float: Converted temperature value

    Raises:
        ValueError: If units are invalid or conversion is invalid

    Examples:
        >>> convert_temperature(0, 'Celsius', 'Fahrenheit')
        32.0
        >>> convert_temperature(100, 'Celsius', 'Kelvin')
        373.15
        >>> convert_temperature(32, 'Fahrenheit', 'Celsius')
        0.0
    """
    valid_units = {'Celsius', 'Fahrenheit', 'Kelvin'}

    # Validate units
    if from_unit not in valid_units:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in valid_units:
        raise ValueError(f"Invalid target unit: {to_unit}")

    # Check for same unit
    if from_unit == to_unit:
        raise ValueError("Source and target units must be different")

    # Validate Kelvin (can't be negative)
    if from_unit == 'Kelvin' and value < 0:
        raise ValueError("Kelvin temperature cannot be negative")

    # Convert to Celsius first (intermediate step)
    if from_unit == 'Celsius':
        celsius = value
    elif from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    else:  # Kelvin
        celsius = value - 273.15

    # Check for below absolute zero
    if celsius < -273.15:
        raise ValueError("Temperature is below absolute zero")

    # Convert from Celsius to target unit
    if to_unit == 'Celsius':
        result = celsius
    elif to_unit == 'Fahrenheit':
        result = (celsius * 9/5) + 32
    else:  # Kelvin
        result = celsius + 273.15

    return result


# Optional: Additional utility functions

def celsius_to_fahrenheit(celsius):
    """Quick conversion: Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Quick conversion: Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """Quick conversion: Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Quick conversion: Kelvin to Celsius."""
    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative")
    return kelvin - 273.15


if __name__ == '__main__':
    # Simple test cases
    print("Testing temperature conversions...")

    # Test 1: Freezing point
    result = convert_temperature(0, 'Celsius', 'Fahrenheit')
    assert result == 32, f"Expected 32, got {result}"
    print("✓ 0°C = 32°F")

    # Test 2: Boiling point
    result = convert_temperature(100, 'Celsius', 'Fahrenheit')
    assert abs(result - 212) < 0.01, f"Expected 212, got {result}"
    print("✓ 100°C = 212°F")

    # Test 3: Absolute zero
    result = convert_temperature(-273.15, 'Celsius', 'Kelvin')
    assert abs(result) < 0.01, f"Expected 0, got {result}"
    print("✓ -273.15°C = 0K")

    # Test 4: Room temperature
    result = convert_temperature(20, 'Celsius', 'Fahrenheit')
    assert abs(result - 68) < 0.01, f"Expected 68, got {result}"
    print("✓ 20°C = 68°F")

    print("\nAll tests passed!")
