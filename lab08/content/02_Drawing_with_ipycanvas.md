# Module 2: Drawing Geometric Elements with ipycanvas

## Creative Programming with Shapes and Patterns

**Learning Objectives:**
- Draw circles, lines, and polygons using ipycanvas
- Use paths to create custom shapes
- Apply for loops to create repetitive patterns
- Combine shapes to create complex designs
- Understand how arrays control visual properties

---

## Drawing Basic Shapes

### Rectangles (Review)

You already know rectangles from Module 1:

```python
from ipycanvas import Canvas

canvas = Canvas(width=400, height=300)

# Filled rectangle
canvas.fill_style = '#FF6B35'
canvas.fill_rect(50, 50, 100, 80)

# Outlined rectangle
canvas.stroke_style = '#1E88E5'
canvas.line_width = 3
canvas.stroke_rect(200, 50, 100, 80)

canvas
```

---

### Circles and Arcs

Circles are drawn using the `arc()` method. The syntax is:


`canvas.arc(center_x, center_y, radius, start_angle, end_angle)`


**Important**: Angles are in **radians**, not degrees!
- Full circle = 2π radians ≈ 6.28
- Half circle = π radians ≈ 3.14
- Quarter circle = π/2 radians ≈ 1.57

```python
import math
from ipycanvas import Canvas

canvas = Canvas(width=400, height=300)

# Draw a filled circle
canvas.fill_style = '#4CAF50'
canvas.fill_arc(100, 100, 50, 0, 2 * math.pi)  # Full circle

# Draw a circle outline
canvas.stroke_style = '#F44336'
canvas.line_width = 3
canvas.stroke_arc(250, 100, 50, 0, 2 * math.pi)

# Draw a semi-circle (arc)
canvas.fill_style = '#9C27B0'
canvas.fill_arc(100, 220, 50, 0, math.pi)  # Half circle (0 to π)

canvas
```

**Syntax Breakdown**:
- `fill_arc(x, y, radius, start, end)` - Filled circle/arc
- `stroke_arc(x, y, radius, start, end)` - Outlined circle/arc
- `x, y` - Center position
- `radius` - Distance from center to edge
- `start, end` - Angles in radians (0 to 2π for full circle)

---

### Lines

To draw straight lines:

```python
canvas = Canvas(width=400, height=300)

# Set line color and width
canvas.stroke_style = '#FF5722'
canvas.line_width = 4

# Draw a line from (50, 50) to (350, 250)
canvas.stroke_line(50, 50, 350, 250)

# Draw more lines
canvas.stroke_style = '#2196F3'
canvas.line_width = 2
canvas.stroke_line(50, 250, 350, 50)

canvas
```

**Syntax**: `stroke_line(x1, y1, x2, y2)`
- `(x1, y1)` - Starting point
- `(x2, y2)` - Ending point

---

### Triangles and Polygons Using Paths

For complex shapes, use **paths** - a series of connected lines:

```python
canvas = Canvas(width=400, height=300)

# Draw a triangle
canvas.fill_style = '#FF6B35'
canvas.begin_path()           # Start a new path
canvas.move_to(200, 50)       # Move to first point (don't draw)
canvas.line_to(150, 150)      # Draw line to second point
canvas.line_to(250, 150)      # Draw line to third point
canvas.close_path()           # Connect back to start
canvas.fill()                 # Fill the shape

# Draw a pentagon outline
canvas.stroke_style = '#1E88E5'
canvas.line_width = 3
canvas.begin_path()
canvas.move_to(100, 220)
canvas.line_to(80, 260)
canvas.line_to(100, 290)
canvas.line_to(140, 290)
canvas.line_to(160, 260)
canvas.close_path()
canvas.stroke()               # Draw outline instead of fill

canvas
```

**Path Methods**:
- `begin_path()` - Start a new shape
- `move_to(x, y)` - Move without drawing
- `line_to(x, y)` - Draw line to point
- `close_path()` - Connect back to start
- `fill()` - Fill the shape
- `stroke()` - Draw outline

---

## Patterns with Loops

The real power of programming graphics comes from using **loops** to create patterns!

### Simple Horizontal Line of Circles

```python
import math
canvas = Canvas(width=400, height=300)

canvas.fill_style = '#2196F3'

# Draw 7 circles in a row
for i in range(7):
    x = 40 + i * 50  # Space circles 50 pixels apart
    canvas.fill_arc(x, 150, 20, 0, 2 * math.pi)

canvas
```

**How it works**:
- Loop runs 7 times with i = 0, 1, 2, 3, 4, 5, 6
- Each iteration calculates a different x position
- When i=0: x = 40 + 0*50 = 40
- When i=1: x = 40 + 1*50 = 90
- When i=2: x = 40 + 2*50 = 140
- And so on...

---

### Grid of Circles (Nested Loops)

```python
import math
canvas = Canvas(width=400, height=300)

canvas.fill_style = '#9C27B0'

# Draw a 5×4 grid of circles
for row in range(4):
    for col in range(5):
        x = 50 + col * 70
        y = 50 + row * 70
        canvas.fill_arc(x, y, 20, 0, 2 * math.pi)

canvas
```

**Understanding Nested Loops**:
- Outer loop (row) runs 4 times
- Inner loop (col) runs 5 times for each row
- Total circles drawn: 4 × 5 = 20 circles
- Each position calculated based on row and column index

---

### Varying Colors with Loops

```python
import math
canvas = Canvas(width=400, height=300)

colors = ['#F44336', '#E91E63', '#9C27B0', '#673AB7',
          '#3F51B5', '#2196F3', '#03A9F4', '#00BCD4']

for i, color in enumerate(colors):
    canvas.fill_style = color
    x = 40 + i * 45
    canvas.fill_arc(x, 150, 20, 0, 2 * math.pi)

canvas
```

**Using Arrays for Colors**:
- Store colors in a list
- `enumerate()` gives us both index and value
- Each circle gets a different color from the array

---

### Color Gradient Using Math

```python
canvas = Canvas(width=400, height=300)

# Create a gradient from blue to red
for i in range(20):
    # Calculate color transition
    red = int(i * 255 / 19)      # Increase red: 0 → 255
    blue = int(255 - i * 255 / 19)  # Decrease blue: 255 → 0

    canvas.fill_style = f'rgb({red}, 0, {blue})'
    canvas.fill_rect(i * 20, 100, 20, 100)

canvas
```

**Creating Gradients**:
- Use loop counter to calculate color values
- Gradually increase one component while decreasing another
- `f'rgb({red}, 0, {blue})'` - Python f-string for formatting

---

## Combining Shapes: Drawing a House

Let's combine rectangles, triangles, and circles to draw a house:

```python
import math
canvas = Canvas(width=400, height=400)

# Sky background
canvas.fill_style = '#87CEEB'
canvas.fill_rect(0, 0, 400, 400)

# Grass
canvas.fill_style = '#90EE90'
canvas.fill_rect(0, 300, 400, 100)

# House body (rectangle)
canvas.fill_style = '#DEB887'
canvas.fill_rect(100, 180, 200, 150)

# Roof (triangle using path)
canvas.fill_style = '#8B4513'
canvas.begin_path()
canvas.move_to(200, 100)   # Top peak
canvas.line_to(80, 180)    # Left corner
canvas.line_to(320, 180)   # Right corner
canvas.close_path()
canvas.fill()

# Door
canvas.fill_style = '#654321'
canvas.fill_rect(170, 250, 60, 80)

# Windows
canvas.fill_style = '#87CEEB'
canvas.fill_rect(120, 210, 40, 40)  # Left window
canvas.fill_rect(240, 210, 40, 40)  # Right window

# Window frames
canvas.stroke_style = '#000000'
canvas.line_width = 2
canvas.stroke_rect(120, 210, 40, 40)
canvas.stroke_rect(240, 210, 40, 40)

# Sun
canvas.fill_style = '#FFD700'
canvas.fill_arc(350, 50, 30, 0, 2 * math.pi)

canvas
```

**Design Strategy**:
1. Draw background first (sky, grass)
2. Draw larger shapes next (house body, roof)
3. Add details on top (windows, door)
4. Add decorative elements last (sun)

---

## Exercise 1: Simple House

**Goal**: Draw a simple house using rectangles and a triangle.

**Requirements**:
- House body (rectangle)
- Roof (triangle using path)
- One door on the left side (rectangle)
- One window on the right side (circle)
- Use at least 4 different colors

**Starter Code**:

```python
import math
from ipycanvas import Canvas

canvas = Canvas(width=400, height=400)

# Your code here:
# 1. Draw house body
# 2. Draw roof
# 3. Draw door
# 4. Draw window

canvas
```

---

## Exercise 2: Checkerboard Pattern ♟️

**Goal**: Create an 8×8 checkerboard pattern using nested loops.

**Requirements**:
- 8 rows × 8 columns of squares
- Alternate between two colors (e.g., black and white)
- Each square should be the same size
- Use nested loops and conditional logic

**Hint**: A square should be colored if `(row + col) % 2 == 0`, otherwise use the other color.

**Starter Code**:

```python
from ipycanvas import Canvas

canvas = Canvas(width=400, height=400)

square_size = 50  # Each square is 50×50 pixels

# Your code here:
# Use nested loops to draw the 8×8 checkerboard pattern

canvas
```

---

## Exercise 3: Circle Grid 🎨

**Goal**: Create a grid of colored circles using nested loops and an array of colors.

**Requirements**:
- At least 4 rows and 4 columns of circles
- Use different colors from an array
- Circles should be evenly spaced
- Use the modulo operator (%) to cycle through colors

**Starter Code**:

```python
import math
from ipycanvas import Canvas

canvas = Canvas(width=400, height=400)

# Color palette
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A',
          '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']

rows = 5
cols = 6
spacing = 60  # Space between circle centers
radius = 20

# Your code here:
# Use nested loops to draw the grid of colored circles

canvas
```

---

## Randomness for Organic Patterns

Use Python's `random` module for natural-looking variations:

```python
import math
import random
from ipycanvas import Canvas

canvas = Canvas(width=400, height=300)

# Draw 50 circles at random positions
for i in range(50):
    x = random.randint(20, 380)
    y = random.randint(20, 280)
    radius = random.randint(5, 20)

    # Random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    canvas.fill_style = f'rgb({r}, {g}, {b})'

    canvas.fill_arc(x, y, radius, 0, 2 * math.pi)

canvas
```

**Random Functions**:
- `random.randint(a, b)` - Random integer from a to b (inclusive)
- `random.random()` - Random float from 0.0 to 1.0
- `random.choice(list)` - Random element from a list

---

## Design Tips

### 1. Plan Before Coding
Sketch your design on paper first. Mark coordinates and sizes.

### 2. Use Constants
<!-- #region -->
```python
# ✅ Good - easy to adjust
CIRCLE_RADIUS = 20
SPACING = 50

# ❌ Bad - "magic numbers" scattered throughout code
canvas.fill_arc(x, y, 20, 0, 2 * math.pi)
x = x + 50
```
<!-- #endregion -->

### 3. Build Incrementally
- Start with one shape
- Get positioning right
- Add colors
- Then add loops and complexity

### 4. Comment Your Code
<!-- #region -->
```python
# Draw the roof triangle
canvas.begin_path()
canvas.move_to(200, 100)  # Peak of roof
canvas.line_to(80, 180)   # Left edge
canvas.line_to(320, 180)  # Right edge
canvas.close_path()
canvas.fill()
```
<!-- #endregion -->

---

## Common Challenges

### Challenge: Circles Cut Off at Edge

**Problem**: Circles partially drawn outside canvas

**Solution**: Account for radius in positioning
<!-- #region -->
```python
# ❌ Circle center at edge - half cut off
canvas.fill_arc(400, 200, 30, 0, 2*math.pi)

# ✅ Circle center accounts for radius
canvas.fill_arc(370, 200, 30, 0, 2*math.pi)  # 400 - 30 = 370
```
<!-- #endregion -->

---

### Challenge: Triangle Points Wrong Direction

**Problem**: Triangle doesn't point where expected

**Solution**: Visualize coordinates and adjust order
<!-- #region -->
```python
# For upward-pointing triangle:
canvas.move_to(200, 50)   # Top point (lowest y)
canvas.line_to(150, 150)  # Bottom-left (higher y)
canvas.line_to(250, 150)  # Bottom-right (higher y)

# Remember: Y increases downward!
```
<!-- #endregion -->

---

### Challenge: Pattern Not Aligned

**Problem**: Grid pattern looks uneven

**Solution**: Use consistent spacing calculations
<!-- #region -->
```python
# ✅ Good - consistent formula
for row in range(rows):
    for col in range(cols):
        x = margin + col * (size + gap)
        y = margin + row * (size + gap)
```        
<!-- #endregion -->

---

## Quick Reference

<!-- #region -->
```python
# Circles
canvas.fill_arc(x, y, radius, 0, 2*math.pi)      # Filled circle
canvas.stroke_arc(x, y, radius, 0, 2*math.pi)    # Circle outline

# Lines
canvas.stroke_line(x1, y1, x2, y2)

# Paths (for custom shapes)
canvas.begin_path()
canvas.move_to(x, y)
canvas.line_to(x, y)
canvas.close_path()
canvas.fill()    # or canvas.stroke()

# Colors
canvas.fill_style = '#FF0000'           # Hex
canvas.fill_style = 'rgb(255, 0, 0)'    # RGB string
canvas.stroke_style = '#0000FF'
canvas.line_width = 3

# Math
import math
math.pi        # π ≈ 3.14159
math.cos(angle)  # Cosine
math.sin(angle)  # Sine
```
<!-- #endregion -->

---

## What's Next?

You've learned to create geometric graphics with ipycanvas! In Module 3, you'll learn to visualize data using matplotlib—transforming numbers into meaningful charts and graphs.

**Key Skills Acquired**:
- ✅ Drawing circles, lines, and polygons
- ✅ Using loops to create patterns
- ✅ Manipulating colors mathematically
- ✅ Combining shapes into complex designs

---

**Next Module**: [Visualizing Data with Matplotlib](03_Visualizing_Data_matplotlib.md)
