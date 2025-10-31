# Module 2: Layout and UX Concepts

## Making UIs Professional and Usable

**Learning Objectives:**
- Organize widgets using layout containers (HBox, VBox, GridBox)
- Apply UX principles for intuitive interfaces
- Implement validation with visual feedback
- Integrate matplotlib for data visualization
- Build a complete data science application

---

## The Problem: Vertical Soup

In Module 1, we used `display()` to show widgets. The result? Everything stacks vertically:

```python
import ipywidgets as W
from IPython.display import display

# This creates a long vertical list
display(W.Text(description='Name:'))
display(W.IntText(description='Age:'))
display(W.Dropdown(description='Country:'))
display(W.Button(description='Submit'))
display(W.Output())
```

This works, but it's not professional or organized. **Solution: Layout containers.**

---

## Layout Containers

### HBox: Horizontal Layout

Arrange widgets side-by-side.

```python
import ipywidgets as W
from IPython.display import display

first_name = W.Text(description='First:')
last_name = W.Text(description='Last:')

# Put them in a horizontal box
name_row = W.HBox([first_name, last_name])
display(name_row)
```

**Use HBox when:** Related inputs should be on the same line (first/last name, city/state, etc.)

---

### VBox: Vertical Layout

Arrange widgets top-to-bottom (explicit vertical stacking).

```python
import ipywidgets as W
from IPython.display import display

title = W.HTML('<h3>Contact Form</h3>')
name = W.Text(description='Name:')
email = W.Text(description='Email:')
submit = W.Button(description='Submit', button_style='success')

# Put them in a vertical box
form = W.VBox([title, name, email, submit])
display(form)
```

**Use VBox when:** You want explicit control over vertical spacing and grouping.

---

### Nesting Layouts: The Real Power

Combine HBox and VBox to create complex layouts.

```python
import ipywidgets as W
from IPython.display import display

# Title section
title = W.HTML('<h3>Temperature Converter</h3>')

# Input row (horizontal)
temp_input = W.FloatText(description='Value:', value=0)
unit_input = W.Dropdown(
    options=['Celsius', 'Fahrenheit', 'Kelvin'],
    description='From:'
)
input_row = W.HBox([temp_input, unit_input])

# Output selection row (horizontal)
unit_output = W.Dropdown(
    options=['Celsius', 'Fahrenheit', 'Kelvin'],
    description='To:',
    value='Fahrenheit'
)
convert_btn = W.Button(description='Convert', button_style='primary')
output_row = W.HBox([unit_output, convert_btn])

# Result area
result = W.Output()

# Combine everything vertically
app = W.VBox([title, input_row, output_row, result])

# Event handler
def on_convert(b):
    with result:
        result.clear_output()
        # Add conversion logic here
        print(f"Converting {temp_input.value} {unit_input.value} to {unit_output.value}")

convert_btn.on_click(on_convert)

display(app)
```

**Pattern:** Related inputs → HBox. Sections/steps → VBox.

---

### GridBox: Grid Layout

For more complex arrangements.

```python
import ipywidgets as W
from IPython.display import display

# Create a calculator layout
buttons = [
    [W.Button(description='7'), W.Button(description='8'), W.Button(description='9'), W.Button(description='/')],
    [W.Button(description='4'), W.Button(description='5'), W.Button(description='6'), W.Button(description='*')],
    [W.Button(description='1'), W.Button(description='2'), W.Button(description='3'), W.Button(description='-')],
    [W.Button(description='0'), W.Button(description='.'), W.Button(description='='), W.Button(description='+')],
]

# Flatten for GridBox
flat_buttons = [btn for row in buttons for btn in row]

grid = W.GridBox(
    flat_buttons,
    layout=W.Layout(grid_template_columns='repeat(4, 120px)')
)

display(W.VBox([
    W.Text(description='Display:', disabled=True),
    grid
]))
```

---

## UX Principles for Better Interfaces

### 1. Grouping and Visual Hierarchy

**Principle:** Related items should be visually grouped.

**Bad Example:**
```python
# Everything mixed together
display(W.Text(description='First Name:'))
display(W.Text(description='Email:'))
display(W.Text(description='Last Name:'))
display(W.Text(description='Phone:'))
```

**Good Example:**
```python
# Grouped logically
name_section = W.HBox([
    W.Text(description='First Name:'),
    W.Text(description='Last Name:')
])

contact_section = W.HBox([
    W.Text(description='Email:'),
    W.Text(description='Phone:')
])

form = W.VBox([
    W.HTML('<b>Personal Information</b>'),
    name_section,
    W.HTML('<b>Contact Information</b>'),
    contact_section
])

display(form)
```

---

### 2. Affordances: Making Actions Obvious

**Principle:** Users should know what's clickable and what's not.

```python
import ipywidgets as W

# Good: Clear button styles indicate purpose
save_btn = W.Button(description='Save', button_style='success', icon='check')
cancel_btn = W.Button(description='Cancel', button_style='danger', icon='times')
reset_btn = W.Button(description='Reset', button_style='warning', icon='refresh')

display(W.HBox([save_btn, cancel_btn, reset_btn]))
```

**Use button styles consistently:**
- `success` (green) - positive actions (save, submit, confirm)
- `danger` (red) - destructive actions (delete, remove)
- `warning` (orange) - caution actions (reset, clear)
- `info` (blue) - informational actions (help, details)
- `primary` (blue) - main action

---

### 3. Feedback: Confirm User Actions

**Principle:** Always let users know what happened.

```python
import ipywidgets as W
from IPython.display import display
import time

submit_btn = W.Button(description='Submit', button_style='primary')
feedback = W.HTML()

def on_submit(b):
    # Show processing
    submit_btn.disabled = True
    submit_btn.description = 'Processing...'

    # Simulate work
    time.sleep(1)

    # Show success
    submit_btn.description = 'Submitted!'
    submit_btn.button_style = 'success'
    feedback.value = '<p style="color: green;">✓ Form submitted successfully!</p>'

    # Reset after delay
    time.sleep(2)
    submit_btn.disabled = False
    submit_btn.description = 'Submit'
    submit_btn.button_style = 'primary'
    feedback.value = ''

submit_btn.on_click(on_submit)
display(submit_btn, feedback)
```

---

### 4. Validation: Prevent and Guide

**Principle:** Prevent errors before they happen. Guide users to correct input.

```python
import ipywidgets as W
from IPython.display import display

email_input = W.Text(description='Email:', placeholder='user@example.com')
validation_msg = W.HTML()
submit_btn = W.Button(description='Submit', button_style='success', disabled=True)

def validate_email(change):
    email = change['new']
    if '@' in email and '.' in email:
        validation_msg.value = '<p style="color: green;">✓ Valid email</p>'
        submit_btn.disabled = False
    elif email == '':
        validation_msg.value = ''
        submit_btn.disabled = True
    else:
        validation_msg.value = '<p style="color: red;">✗ Invalid email format</p>'
        submit_btn.disabled = True

email_input.observe(validate_email, names='value')
display(email_input, validation_msg, submit_btn)
```

**Key pattern:** Disable action buttons until input is valid.

---

### 5. Continuous vs. Discrete Updates

**Principle:** Choose update timing based on operation cost.

```python
import ipywidgets as W
from IPython.display import display

# Continuous: updates while dragging (cheap operations)
slider_continuous = W.IntSlider(
    description='Continuous:',
    continuous_update=True,  # Default
    min=0, max=100
)

# Discrete: updates only when released (expensive operations)
slider_discrete = W.IntSlider(
    description='Discrete:',
    continuous_update=False,  # Only on release
    min=0, max=100
)

output = W.Output()

def show_value(change):
    with output:
        output.clear_output()
        print(f"Continuous: {slider_continuous.value}, Discrete: {slider_discrete.value}")

slider_continuous.observe(show_value, names='value')
slider_discrete.observe(show_value, names='value')

display(slider_continuous, slider_discrete, output)
```

**Use `continuous_update=False` when:**
- Calculating statistics on large datasets
- Making API calls
- Generating plots
- Any expensive operation

---

## Data Science Example: Interactive Data Filter & Visualizer

Let's build a complete data science tool that combines everything we've learned.

```python
import ipywidgets as W
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset (500 samples for realistic distributions)
np.random.seed(42)
n_samples = 500

data = pd.DataFrame({
    'age': np.random.normal(35, 12, n_samples).clip(18, 70),
    'income': np.random.gamma(5, 10000, n_samples).clip(20000, 150000),
    'score': np.random.beta(5, 2, n_samples) * 100,
    'experience': np.random.exponential(5, n_samples).clip(0, 30)
})

# Widgets
column_select = W.Dropdown(
    options=list(data.columns),
    value='age',
    description='Variable:'
)

stat_select = W.Dropdown(
    options=['Mean', 'Median', 'Std Dev', 'Min', 'Max', 'Count'],
    value='Mean',
    description='Statistic:'
)

min_slider = W.IntSlider(
    min=0, max=100, value=0,
    description='Min %ile:',
    continuous_update=False  # Don't update while dragging
)

max_slider = W.IntSlider(
    min=0, max=100, value=100,
    description='Max %ile:',
    continuous_update=False
)

plot_type = W.ToggleButtons(
    options=['Histogram', 'Box Plot', 'Both'],
    value='Histogram',
    description='View:',
    button_style='info'
)

calculate_btn = W.Button(
    description='Update',
    button_style='success',
    icon='refresh'
)

reset_btn = W.Button(
    description='Reset',
    button_style='warning'
)

output = W.Output()
info = W.HTML(value=f"<b>Dataset:</b> {len(data)} samples, {len(data.columns)} variables")

# Event handler with plotting
def on_calculate(_):
    with output:
        output.clear_output(wait=True)

        try:
            col = column_select.value
            stat = stat_select.value

            # Filter by percentile range
            p_min = np.percentile(data[col], min_slider.value)
            p_max = np.percentile(data[col], max_slider.value)
            filtered = data[(data[col] >= p_min) & (data[col] <= p_max)]

            # Calculate statistic
            stat_funcs = {
                'Mean': lambda x: x.mean(),
                'Median': lambda x: x.median(),
                'Std Dev': lambda x: x.std(),
                'Min': lambda x: x.min(),
                'Max': lambda x: x.max(),
                'Count': lambda x: len(x)
            }
            result = stat_funcs[stat](filtered[col])

            # Create visualization
            if plot_type.value == 'Both':
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
            else:
                fig, ax1 = plt.subplots(1, 1, figsize=(8, 4))
                ax2 = None

            # Histogram
            if plot_type.value in ['Histogram', 'Both']:
                ax1.hist(data[col], bins=30, alpha=0.5, label='All data',
                        color='lightblue', edgecolor='black')
                ax1.hist(filtered[col], bins=30, alpha=0.7, label='Filtered',
                        color='orange', edgecolor='black')
                ax1.axvline(result, color='red', linestyle='--', linewidth=2,
                           label=f'{stat}: {result:.2f}')
                ax1.set_xlabel(col.capitalize())
                ax1.set_ylabel('Frequency')
                ax1.set_title(f'Distribution of {col.capitalize()}')
                ax1.legend()
                ax1.grid(True, alpha=0.3)

            # Box plot
            if plot_type.value in ['Box Plot', 'Both']:
                ax_box = ax2 if ax2 else ax1
                box_data = [data[col], filtered[col]]
                bp = ax_box.boxplot(box_data, labels=['All Data', 'Filtered'],
                                    patch_artist=True)
                bp['boxes'][0].set_facecolor('lightblue')
                bp['boxes'][1].set_facecolor('orange')
                ax_box.set_ylabel(col.capitalize())
                ax_box.set_title(f'Box Plot: {col.capitalize()}')
                ax_box.grid(True, alpha=0.3, axis='y')

            plt.tight_layout()
            plt.show()

            # Print statistics
            print(f"📊 Statistics Summary")
            print(f"─" * 40)
            print(f"Filtered: {len(filtered)}/{len(data)} samples ({len(filtered)/len(data)*100:.1f}%)")
            print(f"{stat}: {result:.2f}")
            print(f"Range: [{p_min:.2f}, {p_max:.2f}]")

            if len(filtered) < 10:
                print(f"\n⚠️  Warning: Only {len(filtered)} samples in range")

        except Exception as e:
            print(f"❌ Error: {e}")

def on_reset(_):
    min_slider.value = 0
    max_slider.value = 100
    column_select.value = 'age'
    stat_select.value = 'Mean'
    plot_type.value = 'Histogram'
    with output:
        output.clear_output()

calculate_btn.on_click(on_calculate)
reset_btn.on_click(on_reset)

# Layout - organized and professional
controls_row1 = W.HBox([column_select, stat_select])
controls_row2 = W.HBox([min_slider, max_slider])
controls_row3 = plot_type
controls_row4 = W.HBox([calculate_btn, reset_btn])

controls = W.VBox([controls_row1, controls_row2, controls_row3, controls_row4])

ui = W.VBox([info, controls, output])
display(ui)

# Show initial plot
on_calculate(None)
```

<!-- #region -->
**Try it!**
- Change the variable and see different distributions
- Adjust percentile sliders to filter data
- Switch between visualization types
- Notice how the orange (filtered) data changes

---

## Understanding the Data Science Example

### Why This Example is Effective

1. **Realistic Data**: 500 samples with different statistical distributions
   - Age: Normal distribution (bell curve)
   - Income: Gamma distribution (skewed right)
   - Score: Beta distribution (skewed left)
   - Experience: Exponential distribution

2. **Visual Feedback**: Immediately see the impact of filtering
   - Blue histogram: all data
   - Orange histogram: filtered subset
   - Red line: calculated statistic

3. **Multiple Views**: Histogram shows distribution, box plot shows quartiles

4. **Statistical Learning**: Understand percentiles, distributions, and summary statistics

5. **Professional Layout**: Organized controls, clear hierarchy, good UX

---

## Layout Best Practices from the Example

```python
# ✅ Group related controls horizontally
controls_row1 = W.HBox([column_select, stat_select])

# ✅ Separate sections vertically
controls = W.VBox([controls_row1, controls_row2, controls_row3, controls_row4])

# ✅ Info at top, controls in middle, output at bottom
ui = W.VBox([info, controls, output])
```
<!-- #endregion -->

**Hierarchy:**
1. Dataset info (context)
2. Controls (grouped logically)
3. Output (results)

---

## Exercise 1: Improve a Layout

**Task:** Take this poorly organized interface and improve it using HBox/VBox:

```python
# Current (bad) layout
display(W.HTML('<h3>Order Form</h3>'))
display(W.Text(description='Product:'))
display(W.IntText(description='Quantity:'))
display(W.FloatText(description='Price:'))
display(W.Dropdown(description='Shipping:', options=['Standard', 'Express']))
display(W.Checkbox(description='Gift wrap'))
display(W.Button(description='Calculate Total'))
display(W.Output())

# Your improved layout here using HBox and VBox
```

---

## Exercise 2: Add Validation

**Task:** Enhance the order form with validation:
- Quantity must be > 0
- Price must be > 0
- Calculate button disabled until valid
- Show validation messages

```python
# Your code here
```

---

## Exercise 3: BMI Calculator with Visualization

**Task:** Build a BMI calculator that:
- Has inputs for weight (kg) and height (cm)
- Uses sliders for input (realistic ranges)
- Calculates BMI on button click
- Shows result with color coding:
  - Underweight (< 18.5): blue
  - Normal (18.5-25): green
  - Overweight (25-30): orange
  - Obese (> 30): red

```python
# Your code here
```

---

## Exercise 4: Multi-Step Form

**Task:** Create a multi-step form using layout:
1. Step 1: Personal info (name, age)
2. Step 2: Contact (email, phone)
3. Step 3: Preferences (notifications checkbox, theme dropdown)
4. "Next" buttons that validate before proceeding
5. "Back" buttons to return to previous step
6. Final "Submit" shows all collected data

**Hint:** Use a variable to track current step and update the displayed VBox.

```python
# Your code here
```

<!-- #region -->
---

## Key Takeaways

✅ **HBox for horizontal**, **VBox for vertical**, **GridBox for grid**

✅ **Nest layouts** to create complex, organized interfaces

✅ **Group related controls** - visually and logically

✅ **Use button styles** consistently to communicate purpose

✅ **Provide feedback** - users should always know what's happening

✅ **Validate early** - disable actions until input is valid

✅ **Choose update timing** - continuous vs discrete based on cost

✅ **Visual hierarchy** - important info at top, actions at bottom

---

## Common Layout Patterns

### Form Pattern

```python
W.VBox([
    W.HTML('<h3>Title</h3>'),
    W.HBox([field1, field2]),  # Related inputs
    W.HBox([field3, field4]),
    W.HBox([submit_btn, cancel_btn]),  # Actions
    W.Output()  # Results
])
```
<!-- #endregion -->
<!-- #region -->
### Dashboard Pattern
```python
W.VBox([
    W.HTML('<h2>Dashboard</h2>'),
    W.HBox([metric1, metric2, metric3]),  # Metrics row
    W.HBox([chart1, chart2]),  # Charts row
    controls  # Control panel
])
```
<!-- #endregion -->
<!-- #region -->
### Filter-Results Pattern

```python
W.VBox([
    W.HBox([filter1, filter2, apply_btn]),  # Filters
    W.Output()  # Filtered results
])
```
<!-- #endregion -->
---

## Desktop UI Connection

These layout concepts map directly to desktop frameworks:

| Colab | Qt Designer | Concept |
|-------|-------------|---------|
| HBox | Horizontal Layout | Side-by-side widgets |
| VBox | Vertical Layout | Stacked widgets |
| GridBox | Grid Layout | Grid arrangement |
| nested layouts | Layout within layout | Complex hierarchies |

**In Module 3**, you'll apply these exact same patterns using Qt Designer's visual layout tools!

---

**Module Complete!** You now understand professional UI layout and UX principles. You're ready to transition to desktop development in Module 3.
