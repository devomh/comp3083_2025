---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: base
    language: python
    name: python3
---

# Module 1: Introduction to ipywidgets

## Your First Interactive UI in Google Colab

**Learning Objectives:**
- Create and display basic widgets in Colab
- Handle user events with `.on_click()` and `.observe()`
- Use the Output widget for displaying results
- Implement basic validation and error handling
- Build a working temperature converter

---

## What Are Widgets?

**Widgets** are interactive UI elements that users can manipulate. Think of them as the building blocks of graphical interfaces:

- **Buttons** - clickable elements that trigger actions
- **Text inputs** - fields where users type information
- **Dropdowns** - menus for selecting from options
- **Sliders** - visual controls for numeric ranges
- **Checkboxes** - toggle switches for yes/no options

In Google Colab, we use the `ipywidgets` library to create these interactive elements.

### Why Start with ipywidgets?

1. **Familiar environment** - You already know Colab
2. **Instant feedback** - See results immediately without setup
3. **Same concepts** - Patterns transfer directly to desktop GUIs
4. **Rapid prototyping** - Test ideas quickly before building desktop apps

---

## Getting Started: Your First Widget

Let's create a simple button that responds to clicks.

```python
import ipywidgets as W
from IPython.display import display

# Create a button widget
button = W.Button(description='Click Me!', button_style='success')

# Create an output area
output = W.Output()

# Define what happens when clicked
def on_button_click(b):
    with output:
        print("Button was clicked!")

# Connect the event handler
button.on_click(on_button_click)

# Display widgets
display(button, output)
```

**Try it!** Run this cell and click the button several times. What do you notice?

### Understanding the Pattern

This demonstrates the fundamental event-driven pattern:

1. **Create widgets** - Define the UI elements
2. **Define handlers** - Write functions that respond to events
3. **Connect them** - Use `.on_click()` to link widgets to handlers
4. **Display** - Show the widgets to the user

---

## Essential Widget Types

### 1. Button Widget

Buttons trigger actions when clicked.

```python
# Different button styles
buttons = [
    W.Button(description='Default'),
    W.Button(description='Primary', button_style='primary'),
    W.Button(description='Success', button_style='success'),
    W.Button(description='Info', button_style='info'),
    W.Button(description='Warning', button_style='warning', icon='exclamation-triangle'),
    W.Button(description='Danger', button_style='danger', icon='danger'),
]

for btn in buttons:
    display(btn)
```

**Attributes:**
- `description` - text displayed on button
- `button_style` - visual style ('success', 'danger', etc.)
- `disabled` - whether button can be clicked
- `icon` - optional icon name (e.g., 'check', 'times')

---

### 2. Text Input Widgets

For entering text or numbers.

```python
# Text input
text_input = W.Text(
    value='',
    placeholder='Enter your name',
    description='Name:',
)

# Integer input with constraints
age_input = W.IntText(
    value=0,
    description='Age:',
    min=0,
    max=120
)

# Float input for decimals
price_input = W.FloatText(
    value=0.0,
    description='Price:',
    step=0.01
)

display(text_input, age_input, price_input)
```

**Try it!** Type in each field. Notice how IntText and FloatText validate input automatically.

---

### 3. Dropdown Widget

For selecting from predefined options.

```python
unit_dropdown = W.Dropdown(
    options=['Celsius', 'Fahrenheit', 'Kelvin'],
    value='Celsius',
    description='Unit:',
)

# Can also use a dictionary for label-value pairs
conversion_dropdown = W.Dropdown(
    options={
        'Celsius to Fahrenheit': 'c_to_f',
        'Fahrenheit to Celsius': 'f_to_c',
        'Celsius to Kelvin': 'c_to_k',
    },
    description='Convert:',
)

display(unit_dropdown, conversion_dropdown)
```

**Key point:** Dropdown prevents invalid input - users can only select valid options.

---

### 4. Slider Widgets

For selecting numeric values visually.

```python
# Integer slider
int_slider = W.IntSlider(
    value=50,
    min=0,
    max=100,
    step=1,
    description='Amount:',
    continuous_update=False  # Only update when released
)

# Float slider with custom formatting
price_slider = W.FloatSlider(
    value=5.0,
    min=0.0,
    max=10.0,
    step=0.1,
    description='Tip $:',
    readout_format='.2f',
)

display(int_slider, price_slider)
```

**Important:** `continuous_update=False` means the value only updates when you release the slider, not while dragging. This is useful when the update triggers expensive operations.

---

### 5. Checkbox Widget

For boolean (yes/no) options.

```python
agree_checkbox = W.Checkbox(
    value=False,
    description='I agree to the terms',
    indent=False
)

show_details = W.Checkbox(
    value=True,
    description='Show details',
)

display(agree_checkbox, show_details)
```

---

### 6. Output Widget

Special widget for displaying results, prints, or plots.

```python
output = W.Output()

# Use 'with output:' to capture prints
with output:
    print("This appears in the output widget")
    print("Not in the regular cell output!")

display(output)

# Clear output
# output.clear_output()
```

**Best practice:** Always use an Output widget for results. It keeps your UI clean and controllable.

---

## Event Handling: Making Widgets Interactive

### The `.on_click()` Method

For buttons, use `.on_click()` to attach a handler function.

```python
counter = 0
count_button = W.Button(description='Count')
count_output = W.Output()

def on_count_click(b):
    global counter # Declare we want to use a global variable
    counter += 1
    with count_output:
        count_output.clear_output()
        print(f"Clicked {counter} times")

count_button.on_click(on_count_click)
display(count_button, count_output)
```

**Note:** The handler function receives the button object as parameter (conventionally named `b`).

---

### The `.observe()` Method

For other widgets (text, sliders, dropdowns), use `.observe()` to watch for value changes.

```python
name_input = W.Text(description='Name:')
greeting_output = W.Output()

def on_name_change(change):
    with greeting_output:
        greeting_output.clear_output()
        new_name = change['new']  # The new value
        if new_name:
            print(f"Hello, {new_name}!")
        else:
            print("Enter your name above")

name_input.observe(on_name_change, names='value')
display(name_input, greeting_output)
```

**Understanding the `change` parameter:**
- `change['new']` - the new value
- `change['old']` - the previous value
- `change['owner']` - the widget that changed

Signature: `widget.observe(handler, names='value', type='change')`
- `handler`: a function that accepts one argument, change (a dict describing the event).
- `names`: which trait(s) to watch. Commonly 'value'. Can be a string or a list like ['value', 'options']. If omitted, all trait changes trigger the handler.
- `type`: event type filter, usually 'change' (the default).

---

## Complete Example: Temperature Converter

Let's build a full application combining multiple widgets.

```python
import ipywidgets as W
from IPython.display import display

# Create widgets
temp_input = W.FloatText(
    value=0,
    description='Temperature:',
    step=0.1
)

conversion_type = W.Dropdown(
    options={
        'Celsius → Fahrenheit': 'c_to_f',
        'Fahrenheit → Celsius': 'f_to_c',
        'Celsius → Kelvin': 'c_to_k',
        'Kelvin → Celsius': 'k_to_c',
    },
    value='c_to_f',
    description='Conversion:',
)

convert_button = W.Button(
    description='Convert',
    button_style='primary',
    icon='calculator'
)

result_output = W.Output()

# Conversion functions
def convert_temperature(value, conversion):
    if conversion == 'c_to_f':
        return (value * 9/5) + 32, 'F'
    elif conversion == 'f_to_c':
        return (value - 32) * 5/9, 'C'
    elif conversion == 'c_to_k':
        return value + 273.15, 'K'
    elif conversion == 'k_to_c':
        return value - 273.15, 'C'

# Event handler
def on_convert_click(b):
    with result_output:
        result_output.clear_output()
        try:
            input_value = temp_input.value
            conversion = conversion_type.value

            result, unit = convert_temperature(input_value, conversion)

            print(f"✓ Result: {result:.2f}° {unit}")

        except Exception as e:
            print(f"✗ Error: {e}")

# Connect and display
convert_button.on_click(on_convert_click)
display(temp_input, conversion_type, convert_button, result_output)
```

**Try it!**
- Convert 0°C to Fahrenheit (should be 32°F)
- Convert 100°C to Kelvin (should be 373.15K)
- Try different conversions

---

## Validation and Error Handling

Good UIs provide clear feedback and prevent errors.

### Example: Validating Input

```python
import ipywidgets as W
from IPython.display import display

age_input = W.IntText(description='Age:', value=0)
submit_button = W.Button(description='Submit', button_style='success')
output = W.Output()

def on_submit(b):
    with output:
        output.clear_output()
        age = age_input.value

        # Validation
        if age <= 0:
            print("✗ Please enter a valid age")
            return
        elif age < 18:
            print(f"Age: {age} - You are a minor")
        elif age < 65:
            print(f"Age: {age} - You are an adult")
        else:
            print(f"Age: {age} - You are a senior")

submit_button.on_click(on_submit)
display(age_input, submit_button, output)
```

### Visual Feedback

You can change widget properties to provide feedback:

```python
import ipywidgets as W
from IPython.display import display

password_input = W.Password(description='Password:', placeholder='Enter password')
check_button = W.Button(description='Check', button_style='info')
output = W.Output()

def on_check(b):
    with output:
        output.clear_output()
        pwd = password_input.value

        if len(pwd) < 8:
            check_button.button_style = 'danger'
            print("✗ Password must be at least 8 characters")
        else:
            check_button.button_style = 'success'
            print("✓ Password is valid")

check_button.on_click(on_check)
display(password_input, check_button, output)
```

---

## Exercise 1: Widget Explorer

**Task:** Create an example of each widget type we've learned:
1. Button with click handler
2. Text input with observe
3. Dropdown with at least 3 options
4. IntSlider with range 0-100
5. Checkbox
6. Output widget to display results

Display all widgets and make them functional.

```python
# Your code here
```

---

## Exercise 2: Event Detective

**Task:** Create a widget that shows information about events.

```python
import ipywidgets as W
from IPython.display import display

# Create a slider
slider = W.IntSlider(description='Value:', min=0, max=100)
output = W.Output()

def on_value_change(change):
    with output:
        # Print BOTH old and new values
        # Print the owner widget's description
        # Add your code here
        pass

slider.observe(on_value_change, names='value')
display(slider, output)
```

---

## Exercise 3: Simple Calculator

**Task:** Build a calculator with:
- Two FloatText inputs for numbers
- Dropdown for operation (+, -, *, /)
- Button to calculate
- Output widget for result
- Proper error handling (division by zero!)

```python
# Your code here
```

---

## Exercise 4: Input Validator

**Task:** Create a form that validates a user's input before submitting:
- Name (must not be empty)
- Email (must contain '@')
- Age (must be between 13 and 120)
- Submit button that only works if all inputs are valid
- Clear feedback about what's wrong

```python
# Your code here
```

---

## Exercise 5: Multi-Widget Interaction

**Task:** Create a tip calculator:
- FloatText for bill amount
- IntSlider for tip percentage (0-30%)
- Checkbox for "Split bill?"
- IntText for number of people (if splitting)
- Button to calculate
- Output showing:
  - Tip amount
  - Total bill
  - Per person amount (if splitting)

```python
# Your code here
```

<!-- #region -->
---

## Key Takeaways

✅ **Widgets are objects** - They have properties (value, description, etc.) and methods (on_click, observe)

✅ **Event-driven pattern** - Create widgets → define handlers → connect → display

✅ **Two event methods:**
   - `.on_click(handler)` for buttons
   - `.observe(handler, names='value')` for value changes

✅ **Output widget** - Use `with output:` to capture prints and keep UI clean

✅ **Validation matters** - Always check user input and provide clear feedback

✅ **Error handling** - Use try/except to gracefully handle invalid inputs

---

## Common Mistakes to Avoid

❌ **Calling the handler instead of passing it**

```python
# Wrong
button.on_click(my_handler())  # Executes immediately!

# Correct
button.on_click(my_handler)  # Passes function reference
```
<!-- #endregion -->
<!-- #region -->
❌ **Forgetting to clear output**

```python
# Results keep appending
with output:
    print("Result")  # New results append

# Use clear_output()
with output:
    output.clear_output()  # Clear old results
    print("Result")
```
<!-- #endregion -->
<!-- #region -->
❌ **Not handling errors**

```python
# Bad - crashes on invalid input
result = int(text_input.value)

# Good - graceful error handling
try:
    result = int(text_input.value)
except ValueError:
    print("Please enter a valid number")
```
<!-- #endregion -->
---

## Next Steps

In **Module 2: Layout and UX Concepts**, you'll learn to:
- Organize widgets with HBox, VBox, and GridBox
- Apply professional UI/UX principles
- Integrate matplotlib for data visualization
- Build a complete data science application

**Before proceeding:**
- Complete all 5 exercises above
- Experiment with different widget combinations
- Think about how these concepts apply to desktop apps

---

## Quick Reference

### Import Statement
```python
import ipywidgets as W
from IPython.display import display
```

### Common Widgets
- `W.Button()` - clickable button
- `W.Text()` - single-line text input
- `W.IntText()` - integer input
- `W.FloatText()` - decimal input
- `W.Dropdown()` - selection menu
- `W.IntSlider()` - integer slider
- `W.FloatSlider()` - decimal slider
- `W.Checkbox()` - boolean toggle
- `W.Output()` - display area

### Event Handling
- `widget.on_click(handler)` - for buttons
- `widget.observe(handler, names='value')` - for value changes
- Use `with output:` for clean result display
- Always use `output.clear_output()` before new results

---

**Module Complete!** You now understand the fundamentals of interactive widgets. Move on to Module 2 to learn professional layout and UX techniques.
