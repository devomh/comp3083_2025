# Module 3: Visualizing Data with Matplotlib

## Transforming Numbers into Visual Stories

**Learning Objectives:**
- Create line charts to show trends over time
- Build bar charts for categorical comparisons
- Generate scatter plots to reveal correlations
- Customize charts with titles, labels, colors, and legends
- Choose appropriate chart types for different data
- Work with NumPy arrays for data generation

---

## Why Visualize Data?

Numbers alone can be hard to understand. A table of 100 values tells us little at a glance, but a chart can reveal patterns instantly:

- **Trends**: Is this value increasing or decreasing over time?
- **Comparisons**: Which category has the highest value?
- **Relationships**: Do these two variables correlate?
- **Outliers**: Are there any unusual data points?

**Key Principle**: A good visualization makes complex data instantly comprehensible.

---

## Introduction to Matplotlib

**Matplotlib** is Python's most popular data visualization library. It follows a simple pattern:

```python
import matplotlib.pyplot as plt

# 1. Prepare your data
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

# 2. Create the plot
plt.plot(x_data, y_data)

# 3. Customize (labels, title, etc.)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('My Chart')

# 4. Display
plt.show()
```

---

## Line Charts: Showing Trends

**Use line charts when**: You want to show how values change over time or across a continuous range.

### Basic Line Chart

```python
import matplotlib.pyplot as plt

# Days of the week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# Temperature in Celsius
temperatures = [22, 24, 23, 25, 27, 26, 24]

plt.plot(days, temperatures)
plt.xlabel('Day of Week')
plt.ylabel('Temperature (°C)')
plt.title('Weekly Temperature')
plt.grid(True, alpha=0.3)  # Add grid for readability
plt.show()
```

---

### Customizing Line Appearance

```python
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 23, 25, 27, 26, 24]

plt.plot(days, temperatures,
         color='#FF6B35',      # Custom color
         linewidth=2,          # Thicker line
         marker='o',           # Add markers at data points
         markersize=8,         # Marker size
         linestyle='-')        # Line style: '-', '--', '-.', ':'

plt.xlabel('Day of Week')
plt.ylabel('Temperature (°C)')
plt.title('Weekly Temperature Trend')
plt.grid(True, alpha=0.3)
plt.show()
```

**Line Style Options**:
- `'-'` - Solid line
- `'--'` - Dashed line
- `'-.'` - Dash-dot line
- `':'` - Dotted line

**Marker Options**: `'o'` (circle), `'s'` (square), `'^'` (triangle), `'*'` (star), `'D'` (diamond)

---

### Multiple Lines on One Chart

```python
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
city_a_temp = [22, 24, 23, 25, 27, 26, 24]
city_b_temp = [18, 19, 21, 20, 22, 23, 21]

plt.plot(days, city_a_temp, marker='o', label='City A', color='#FF6B35')
plt.plot(days, city_b_temp, marker='s', label='City B', color='#4ECDC4')

plt.xlabel('Day of Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Comparison')
plt.legend()  # Show legend with labels
plt.grid(True, alpha=0.3)
plt.show()
```

**Key Addition**: `label` parameter + `plt.legend()` shows which line is which.

---

## Bar Charts: Comparing Categories

**Use bar charts when**: You want to compare values across different categories.

### Basic Bar Chart

```python
import matplotlib.pyplot as plt

# Grade distribution
grades = ['A', 'B', 'C', 'D', 'F']
counts = [8, 15, 12, 5, 2]

plt.bar(grades, counts, color='#4ECDC4')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('Grade Distribution')
plt.show()
```

---

### Customizing Bars

```python
import matplotlib.pyplot as plt

grades = ['A', 'B', 'C', 'D', 'F']
counts = [8, 15, 12, 5, 2]

# Custom colors for each bar
colors = ['#4CAF50', '#8BC34A', '#FFC107', '#FF9800', '#F44336']

plt.bar(grades, counts, color=colors, edgecolor='black', linewidth=1.5)
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.title('Class Grade Distribution', fontsize=14, fontweight='bold')
plt.ylim(0, 20)  # Set y-axis range
plt.show()
```

**Customization Options**:
- `color` - Fill color(s)
- `edgecolor` - Border color
- `linewidth` - Border thickness
- `width` - Bar width (default 0.8)
- `alpha` - Transparency (0.0 to 1.0)

---

### Horizontal Bar Charts

For long category names, horizontal bars work better:

```python
import matplotlib.pyplot as plt

subjects = ['Mathematics', 'Science', 'History', 'English', 'Art']
scores = [85, 92, 78, 88, 95]

plt.barh(subjects, scores, color='#9C27B0')  # barh = horizontal bar
plt.xlabel('Average Score')
plt.ylabel('Subject')
plt.title('Subject Performance')
plt.xlim(0, 100)
plt.show()
```

---

### Grouped Bar Charts

Compare multiple categories side by side:

```python
import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Science', 'English']
class_a = [85, 78, 92]
class_b = [88, 82, 89]

x = np.arange(len(subjects))  # Position for bars
width = 0.35  # Bar width

plt.bar(x - width/2, class_a, width, label='Class A', color='#FF6B35')
plt.bar(x + width/2, class_b, width, label='Class B', color='#4ECDC4')

plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.title('Class Comparison')
plt.xticks(x, subjects)  # Set x-axis labels
plt.legend()
plt.show()
```

---

## Scatter Plots: Finding Relationships

**Use scatter plots when**: You want to see if two variables are related (correlation).

### Basic Scatter Plot

```python
import matplotlib.pyplot as plt

# Study hours vs. test scores
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [45, 55, 60, 65, 75, 80, 85, 90]

plt.scatter(study_hours, test_scores, color='#2196F3', s=100)  # s = size
plt.xlabel('Study Hours')
plt.ylabel('Test Score')
plt.title('Study Time vs. Test Performance')
plt.grid(True, alpha=0.3)
plt.show()
```

**Interpretation**: This shows a positive correlation—more study hours tend to lead to higher scores.

---

### Customizing Scatter Plots

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [45, 55, 60, 65, 75, 80, 85, 90]

plt.scatter(study_hours, test_scores,
            color='#FF6B35',      # Point color
            s=150,                # Size
            alpha=0.6,            # Transparency
            edgecolors='black',   # Border color
            linewidths=2)         # Border width

plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Test Score', fontsize=12)
plt.title('Study Time vs. Performance', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.show()
```

---

### Scatter Plot with Varying Sizes and Colors

```python
import matplotlib.pyplot as plt
import numpy as np

# Student data
study_hours = [2, 3, 4, 5, 6, 7, 8, 9]
test_scores = [60, 65, 70, 75, 80, 85, 88, 92]
attendance = [70, 75, 85, 90, 88, 95, 98, 100]
sizes = [a * 5 for a in attendance]  # Scale sizes for visibility

plt.scatter(study_hours, test_scores,
            s=sizes,                  # Size based on attendance
            c=attendance,             # Color based on attendance
            cmap='viridis',           # Color map
            alpha=0.6,
            edgecolors='black')

plt.colorbar(label='Attendance %')  # Show color scale
plt.xlabel('Study Hours')
plt.ylabel('Test Score')
plt.title('Study, Performance, and Attendance')
plt.show()
```

**Advanced Features**:
- `c` - Array of values for color mapping
- `cmap` - Color scheme ('viridis', 'plasma', 'coolwarm', etc.)
- `plt.colorbar()` - Shows what colors represent

---

## Working with NumPy for Data

NumPy makes it easy to generate data for visualization:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate evenly spaced values
x = np.linspace(0, 10, 50)  # 50 values from 0 to 10

# Generate y values using mathematical operations
y = x ** 2  # Square each x value

plt.plot(x, y, color='#9C27B0', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y = X²')
plt.title('Quadratic Function')
plt.grid(True, alpha=0.3)
plt.show()
```

**NumPy Functions**:
- `np.linspace(start, end, num)` - Create evenly spaced values
- `np.arange(start, end, step)` - Create range with step size
- `np.random.rand(n)` - Random values between 0 and 1
- `np.sin()`, `np.cos()`, `np.exp()` - Mathematical functions

---

## Exercise 1: Temperature Trends 📈

**Goal**: Create a line chart showing weekly temperature data.

**Requirements**:
- Plot temperature data for 7 days
- Add markers to show individual data points
- Include proper labels and title
- Add a grid for easier reading
- Customize line color and style

**Starter Code**:

```python
import matplotlib.pyplot as plt

# Temperature (°C) data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [18, 20, 19, 22, 24, 23, 21]  # Temperatures in Celsius

# Your code here


plt.tight_layout()  # Adjust spacing
plt.show()
```

---

## Exercise 2: Grade Distribution 📊

**Goal**: Create a bar chart showing how many students received each grade.

**Requirements**:
- Display grades A through F on x-axis
- Show student counts on y-axis
- Use different colors for each bar
- Include labels and title
- Make bars visually distinct with borders

**Starter Code**:

```python
import matplotlib.pyplot as plt

# Grade data
grades = ['A', 'B', 'C', 'D', 'F']
student_counts = [12, 18, 15, 8, 3]

# Color scheme (green for good, red for poor)
colors = ['#4CAF50', '#8BC34A', '#FFC107', '#FF9800', '#F44336']

# Your code here

plt.show()
```

---

## Advanced: Mathematical Functions 📉

**Goal**: Plot sine and cosine functions on the same chart to show their relationship.

**Requirements**:
- Use NumPy to generate x values from 0 to 2π
- Plot both sin(x) and cos(x)
- Use different colors and styles for each function
- Add a legend to distinguish the functions
- Include proper labels and grid

**Starter Code**:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)  # 100 points for smooth curves

# Calculate y values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot both functions
plt.plot(x, y_sin, color='#FF6B35', linewidth=2, label='sin(x)')
plt.plot(x, y_cos, color='#4ECDC4', linewidth=2, linestyle='--', label='cos(x)')

# Customize chart
plt.xlabel('x (radians)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Sine and Cosine Functions', fontsize=14, fontweight='bold')
plt.axhline(y=0, color='black', linewidth=0.5)  # Add x-axis line
plt.axvline(x=0, color='black', linewidth=0.5)  # Add y-axis line
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)

# Display
plt.show()
```

**Hint for Subplots**:
```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.plot(x, y_sin, color='#FF6B35')
ax1.set_title('Sine')
ax2.plot(x, y_cos, color='#4ECDC4')
ax2.set_title('Cosine')
plt.tight_layout()
plt.show()
```

---

## Advanced: Subplots for Multiple Charts

Display multiple charts in one figure:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create 2×2 grid of subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

# Data
x = np.linspace(0, 10, 50)

# Subplot 1: Line chart
ax1.plot(x, x**2, color='#FF6B35')
ax1.set_title('Quadratic')
ax1.grid(True, alpha=0.3)

# Subplot 2: Bar chart
ax2.bar(['A', 'B', 'C'], [3, 7, 5], color='#4ECDC4')
ax2.set_title('Bar Chart')

# Subplot 3: Scatter
ax3.scatter(x, np.sin(x), color='#9C27B0', s=50)
ax3.set_title('Scatter')
ax3.grid(True, alpha=0.3)

# Subplot 4: Multiple lines
ax4.plot(x, np.sin(x), label='sin')
ax4.plot(x, np.cos(x), label='cos')
ax4.set_title('Trig Functions')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()  # Prevent overlap
plt.show()
```

---

## Saving Charts

Save your charts as image files:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.title('My Chart')

# Save as PNG
plt.savefig('my_chart.png', dpi=300, bbox_inches='tight')

# Save as PDF (vector format - scales without quality loss)
plt.savefig('my_chart.pdf', bbox_inches='tight')

plt.show()
```

**Parameters**:
- `dpi` - Resolution (dots per inch), 300 is publication quality
- `bbox_inches='tight'` - Remove extra whitespace
- Formats: `.png`, `.jpg`, `.pdf`, `.svg`

---

## Choosing the Right Chart Type

| Data Type | Best Chart | When to Use |
|-----------|-----------|-------------|
| **Time series** | Line chart | Show trends over time |
| **Categories** | Bar chart | Compare different groups |
| **Correlation** | Scatter plot | Show relationship between variables |
| **Distribution** | Histogram | Show frequency of values |
| **Proportions** | Pie chart | Show parts of a whole |
| **Comparison** | Grouped bar | Compare multiple categories across groups |

---

## Design Principles

### 1. Clarity Over Decoration
- Every element should serve a purpose
- Remove unnecessary decorations
- Focus on the data

### 2. Appropriate Scale
- Start y-axis at zero for bar charts (unless there's good reason)
- Choose ranges that show variation clearly
- Don't exaggerate differences

### 3. Readable Labels
- Use clear, descriptive axis labels
- Include units (°C, %, $, etc.)
- Title should explain what's shown

### 4. Color with Purpose
- Use color to highlight important data
- Ensure colors are distinguishable
- Consider colorblind-friendly palettes
- Be consistent across related charts

### 5. Simplify
- Remove chart junk (unnecessary gridlines, 3D effects)
- Use white space effectively
- One main message per chart

---

## Common Mistakes

### ❌ Mistake 1: Missing plt.show()
```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('My Chart')
# Chart created but not displayed
```

### ✅ Solution: Always Call plt.show()
```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('My Chart')
plt.show()  # Display the chart
```

---

### ❌ Mistake 2: Overlapping Plots
```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
plt.plot([1, 2, 3], [2, 5, 10])  # New data
plt.show()  # Creates separate chart
```

### ✅ Solution: Plot Together or Clear Between
```python
# Option 1: Plot together
plt.plot([1, 2, 3], [1, 4, 9], label='Series 1')
plt.plot([1, 2, 3], [2, 5, 10], label='Series 2')
plt.legend()
plt.show()

# Option 2: Clear between plots
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
plt.clf()  # Clear figure
plt.plot([1, 2, 3], [2, 5, 10])
plt.show()
```

---

### ❌ Mistake 3: Unreadable Labels
```python
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
plt.bar(days, [1, 2, 3, 4, 5])
# Labels overlap and can't be read
```

### ✅ Solution: Rotate or Shorten Labels
```python
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
plt.bar(days, [1, 2, 3, 4, 5])
plt.xticks(rotation=45)  # Rotate labels
plt.tight_layout()  # Adjust spacing
```

---

## Quick Reference

<!-- #region -->
```python
import matplotlib.pyplot as plt
import numpy as np

# Line chart
plt.plot(x, y, color='red', marker='o', linestyle='--', linewidth=2, label='My Line')

# Bar chart
plt.bar(categories, values, color='blue', edgecolor='black', width=0.8)
plt.barh(categories, values)  # Horizontal bars

# Scatter plot
plt.scatter(x, y, s=100, c=colors, alpha=0.6, edgecolors='black')

# Customization
plt.xlabel('X Label', fontsize=12)
plt.ylabel('Y Label', fontsize=12)
plt.title('Chart Title', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 10)  # Set x-axis range
plt.ylim(0, 100)  # Set y-axis range

# Display
plt.tight_layout()
plt.show()

# Save
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
```
<!-- #endregion -->

---

## What's Next?

You've mastered data visualization with matplotlib! In Module 4, you'll combine ipycanvas and matplotlib to create integrated projects that showcase both creative graphics and data visualization.

**Key Skills Acquired**:
- ✅ Creating line, bar, and scatter plots
- ✅ Customizing colors, labels, and styles
- ✅ Choosing appropriate visualizations for data
- ✅ Using NumPy for data generation
- ✅ Applying design principles for clarity

---

**Next Module**: [Integration and Mini-Projects](04_Integration_Mini_Projects.md)
