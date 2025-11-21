# Module 1: Introduction and Graphics Fundamentals

## Understanding How Computers Create Visual Output

**Learning Objectives:**
- Understand RGB color representation and hexadecimal codes
- Learn coordinate systems for positioning graphics
- Set up ipycanvas and matplotlib in Google Colab
- Create your first canvas and draw basic shapes
- Recognize the relationship between code and visual output

---

## What Are Digital Graphics?

Every image you see on a screen is composed of **pixels**—tiny colored dots arranged in a grid. When you write graphics code, you're telling the computer which pixels to light up and what color to make them.

Think of a canvas as a piece of graph paper where:
- Each square is a pixel
- You specify locations using (x, y) coordinates
- You specify colors using numbers

**Key Insight**: Graphics programming is fundamentally about **positioning** (where to draw) and **coloring** (what color to use).

---

## Setup: Installing Required Libraries

```python
# Install ipycanvas for drawing graphics
!pip install ipycanvas
```

Then import the libraries we'll use throughout this lab:

```python
# For drawing graphics
from ipycanvas import Canvas

# For data visualization
import matplotlib.pyplot as plt
import numpy as np
```

**Note**: You only need to install ipycanvas once per Colab session, but you must import libraries in each notebook.

---

## The RGB Color Model

### Understanding RGB

Colors on screens are created by mixing three primary colors of light:
- **R**ed
- **G**reen
- **B**lue

Each component ranges from **0** (none) to **255** (maximum intensity).

<!-- #region -->
```python
# RGB examples - tuple format (red, green, blue)
pure_red = (255, 0, 0)      # All red, no green or blue
pure_green = (0, 255, 0)    # All green
pure_blue = (0, 0, 255)     # All blue

white = (255, 255, 255)     # All colors at maximum
black = (0, 0, 0)           # All colors at minimum

yellow = (255, 255, 0)      # Red + Green = Yellow
cyan = (0, 255, 255)        # Green + Blue = Cyan
magenta = (255, 0, 255)     # Red + Blue = Magenta

gray = (128, 128, 128)      # Equal amounts of all three
```
<!-- #endregion -->

### Hexadecimal Color Codes

Colors can also be written in **hexadecimal** (base-16) format, commonly used in web development:

<!-- #region -->
```python
# Hexadecimal format: #RRGGBB
# Each pair is a hex number from 00 (0) to FF (255)

'#FF0000'  # Red:     FF=255, 00=0,   00=0
'#00FF00'  # Green:   00=0,   FF=255, 00=0
'#0000FF'  # Blue:    00=0,   00=0,   FF=255
'#FFFFFF'  # White:   FF=255, FF=255, FF=255
'#000000'  # Black:   00=0,   00=0,   00=0
'#FF6B35'  # Orange:  FF=255, 6B=107, 35=53
```
<!-- #endregion -->

**Quick Reference**:
- `00` = 0
- `80` = 128
- `FF` = 255

**Try it yourself**: Use an [online color picker](https://www.google.com/search?q=color+picker) to see RGB and hex values for any color!

---

## The Coordinate System

Computer graphics use a coordinate system where:

```
(0,0) ────────── X increases ────────→
  │
  │
  │  Your drawing area (canvas)
  │
  │
  Y increases
  │
  ↓
```

**Important**: Unlike math class, the Y-axis goes **downward**!

- **Origin (0, 0)** is at the top-left corner
- **X increases** moving right
- **Y increases** moving down

### Example Positions

On a 400×300 canvas:

<!-- #region -->
```python
(0, 0)       # Top-left corner
(400, 0)     # Top-right corner
(0, 300)     # Bottom-left corner
(400, 300)   # Bottom-right corner
(200, 150)   # Center of canvas
```
<!-- #endregion -->

---

## Your First Canvas

Let's create a canvas and draw something!

```python
# Create a canvas 400 pixels wide and 300 pixels tall
canvas = Canvas(width=400, height=300)

# Set the fill color to blue
canvas.fill_style = '#2196F3'

# Draw a filled rectangle
# Syntax: fill_rect(x, y, width, height)
canvas.fill_rect(10, 10, 200, 100)

# Display the canvas
canvas
```

**What's happening here?**
1. `Canvas(width=400, height=300)` creates a blank 400×300 pixel canvas
2. `fill_style` sets the color for filled shapes
3. `fill_rect(50, 50, 200, 100)` draws a rectangle:
   - Starts at position (50, 50)
   - Has width of 200 pixels
   - Has height of 100 pixels
4. `canvas` at the end displays the canvas in Colab

---

## Drawing Multiple Shapes

You can draw multiple shapes on the same canvas:

```python
canvas = Canvas(width=400, height=300)

# Draw a blue rectangle
canvas.fill_style = '#2196F3'
canvas.fill_rect(50, 50, 100, 100)

# Draw a red rectangle
canvas.fill_style = '#F44336'
canvas.fill_rect(200, 50, 100, 100)

# Draw a green rectangle
canvas.fill_style = '#4CAF50'
canvas.fill_rect(125, 175, 100, 100)

canvas
```

**Key Observation**: Shapes are drawn in order. Later shapes appear on top of earlier ones (like painting layers).

---

## Outline vs. Filled Shapes

ipycanvas offers two ways to draw shapes:

```python
canvas = Canvas(width=400, height=300)

# Filled shapes use fill_style and fill_* methods
canvas.fill_style = '#FF6B35'
canvas.fill_rect(50, 50, 100, 100)

# Outline shapes use stroke_style and stroke_* methods
canvas.stroke_style = '#1E88E5'
canvas.line_width = 3  # Make outline thicker
canvas.stroke_rect(200, 50, 100, 100)

canvas
```

---

## Working with matplotlib

While ipycanvas is great for drawing graphics, **matplotlib** is the standard for data visualization. Here's a simple example:

```python
# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y, color='blue', marker='o')

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('My First Plot')

# Add a grid for readability
plt.grid(True, alpha=0.3)

# Display the plot
plt.show()
```

**Components of a Good Chart**:
1. **Title** - What the chart shows
2. **Axis Labels** - What each axis represents
3. **Data** - The actual information being visualized
4. **Styling** - Colors, markers, and grid for clarity

---

## Try It Yourself: Hello, Graphics!

Create a canvas that draws your initials or a simple design using rectangles. Use at least three different colors!

```python
# Your code here
canvas = Canvas(width=400, height=300)

# Example: Drawing the letter "H"
canvas.fill_style = '#9C27B0'
canvas.fill_rect(50, 50, 40, 200)   # Left vertical bar
canvas.fill_rect(200, 50, 40, 200)  # Right vertical bar
canvas.fill_rect(50, 130, 190, 40)  # Horizontal bar

canvas
```

---

## Key Concepts Summary

### Colors
- **RGB Format**: `(red, green, blue)` with values 0-255
- **Hex Format**: `#RRGGBB` using hexadecimal (00-FF)
- Mix colors by adjusting component values

### Coordinates
- **Origin (0,0)** at top-left
- **X-axis** increases to the right
- **Y-axis** increases downward
- Position format: `(x, y)`

### Canvas Basics
- Create: `Canvas(width=pixels, height=pixels)`
- Fill color: `canvas.fill_style = color`
- Outline color: `canvas.stroke_style = color`
- Draw rectangle: `canvas.fill_rect(x, y, width, height)`

### Plotting Basics
- Create plot: `plt.plot(x_data, y_data)`
- Customize: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`
- Display: `plt.show()`

---

## Common Beginner Mistakes

### ❌ Mistake 1: Canvas Not Displaying
```python
canvas = Canvas(width=400, height=300)
canvas.fill_rect(0, 0, 100, 100)
print("Done")  # Canvas won't show because print() is the last statement
```

### ✅ Solution: Canvas Must Be Last Expression
```python
canvas = Canvas(width=400, height=300)
canvas.fill_rect(0, 0, 100, 100)
canvas  # This line displays the canvas
```

---

### ❌ Mistake 2: Coordinates Outside Canvas
```python
canvas = Canvas(width=400, height=300)
canvas.fill_rect(500, 500, 100, 100)  # Drawn outside visible area!
canvas
```

### ✅ Solution: Keep Coordinates Within Canvas Bounds
```python
canvas = Canvas(width=400, height=300)
canvas.fill_rect(50, 50, 100, 100)  # Starts at (50,50), well within canvas
canvas
```

---

### ❌ Mistake 3: Invalid Color Values
```python
canvas.fill_style = 'rgb(300, 100, 50)'  # 300 exceeds maximum (255)
```

### ✅ Solution: RGB Values Must Be 0-255
```python
canvas.fill_style = 'rgb(255, 100, 50)'  # Valid
# Or use hex
canvas.fill_style = '#FF6432'
```

<!-- #region -->
---

## Quick Reference Card

```python
# ==================== SETUP ====================
from ipycanvas import Canvas
import matplotlib.pyplot as plt
import numpy as np

# ==================== CANVAS ====================
canvas = Canvas(width=400, height=300)

# Set colors
canvas.fill_style = '#FF0000'      # Hex color
canvas.fill_style = 'rgb(255,0,0)' # RGB color
canvas.stroke_style = '#0000FF'
canvas.line_width = 2

# Draw filled rectangle
canvas.fill_rect(x, y, width, height)

# Draw rectangle outline
canvas.stroke_rect(x, y, width, height)

# Display canvas
canvas

# ==================== MATPLOTLIB ====================
plt.plot(x_data, y_data, color='blue', marker='o')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Chart Title')
plt.grid(True)
plt.show()
```
<!-- #endregion -->

---

## What's Next?

Now that you understand the fundamentals of digital graphics, you're ready to:

1. **Module 2**: Draw circles, lines, triangles, and create patterns with loops
2. **Module 3**: Visualize data with different chart types

**Remember**: Every complex graphic starts with these simple building blocks!

---

## Additional Resources

- [RGB Color Picker](https://www.google.com/search?q=color+picker)
- [Hex to RGB Converter](https://www.rapidtables.com/convert/color/hex-to-rgb.html)
- [ipycanvas Documentation](https://ipycanvas.readthedocs.io/)
- [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [Color Theory for Programmers](https://programmingdesignsystems.com/color/color-models-and-color-spaces/)

---

**Next Module**: [Drawing Geometric Elements with ipycanvas](02_Drawing_with_ipycanvas.md)
