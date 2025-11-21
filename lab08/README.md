# Introduction to Programming and CS I - Lab 08

## Graphics Generation and Data Visualization

### Overview

Lab 08 introduces you to the exciting world of **graphics generation** and **data visualization**. You'll learn how computers create visual output—from basic geometric shapes to sophisticated data charts. This lab emphasizes the creative intersection of programming logic and visual design.

Rather than building complex applications, we'll focus on mastering two complementary approaches: **programmatic drawing** with ipycanvas for creative graphics, and **data visualization** with matplotlib for analytical charts. You'll discover how loops, arrays, and functions can create stunning visual patterns.

**Primary Focus**: Understanding digital graphics fundamentals and creating visual output
**Secondary Focus**: Transforming data into meaningful visual representations

**Core Philosophy**: **"Code is visual"** — Every program you write produces visual output, whether text, graphics, or charts. Understanding graphics deepens your appreciation of how computers communicate information visually.

---

## Understanding Digital Graphics

Digital graphics are fundamentally about controlling pixels—individual points of colored light on your screen. Every image you see is a matrix of pixels, each with its own color value.

### The RGB Color Model

Colors are represented using three components:

```python
# RGB values range from 0 to 255
red = (255, 0, 0)      # Maximum red, no green or blue
green = (0, 255, 0)    # Maximum green
blue = (0, 0, 255)     # Maximum blue
white = (255, 255, 255)  # All colors at maximum
black = (0, 0, 0)      # No light at all
purple = (128, 0, 128) # Mix of red and blue
```

### The Coordinate System

Computer graphics use a coordinate system where:
- **Origin (0,0)** is typically at the top-left corner
- **X-axis** increases moving right
- **Y-axis** increases moving down (opposite of math class!)

Understanding these fundamentals is essential for positioning graphics and understanding how visualization libraries work.

---

## Learning Objectives

By the end of this lab, students will be able to:

### Conceptual Understanding
- ✅ Explain how colors are represented using RGB values (0-255)
- ✅ Describe pixels and canvas as a matrix of coordinate points
- ✅ Understand coordinate systems for positioning graphical elements
- ✅ Distinguish between creative graphics and data visualization

### Technical Skills
- ✅ Create and configure a drawing canvas using ipycanvas
- ✅ Draw basic geometric shapes (rectangles, circles, lines, triangles)
- ✅ Apply colors, fills, and styling to graphical elements
- ✅ Use loops and arrays to create repetitive patterns
- ✅ Create data visualizations with matplotlib (line, bar, scatter plots)
- ✅ Customize charts with labels, titles, colors, and legends

### Practical Application
- ✅ Generate geometric patterns using loops and conditionals
- ✅ Create color gradients using arrays and mathematical sequences
- ✅ Transform numerical data into visual charts
- ✅ Integrate programming concepts (loops, arrays, functions) with graphics
- ✅ Design visually appealing and informative visualizations

---

## Lab Structure

**Total Duration**: 90 minutes (one class session)

### 📚 Core Content Modules

#### **Module 1: Introduction and Graphics Fundamentals**
**File**: [01_Introduction_Graphics_Fundamentals.md](content/01_Introduction_Graphics_Fundamentals.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab08/content/01_Introduction_Graphics_Fundamentals.ipynb)

**Foundation Concepts** — Understanding how computers represent and display graphics.

**Topics Covered:**
- RGB color model and hexadecimal color codes
- Pixel matrix and coordinate systems
- Canvas setup and configuration
- First drawing: "Hello, Graphics!"

**Key Concepts:**
- Colors as numerical values (0-255 per channel)
- Canvas as a drawable surface
- Coordinate system orientation
- Basic drawing commands

**Estimated Time**: 15 minutes

---

#### **Module 2: Drawing Geometric Elements with ipycanvas**
**File**: [02_Drawing_with_ipycanvas.md](content/02_Drawing_with_ipycanvas.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab08/content/02_Drawing_with_ipycanvas.ipynb)

**Creative Programming** — Use code to create geometric art and patterns.

**Topics Covered:**

**1. Basic Shapes**
- Rectangles: `fill_rect()`, `stroke_rect()`
- Circles and arcs: `arc()`, `fill_arc()`
- Lines: `stroke_line()`, `begin_path()`
- Polygons and triangles using paths

**2. Patterns with Loops**
- Grid patterns using nested loops
- Checkerboard patterns with conditionals
- Circular arrangements with trigonometry
- Color gradients using array manipulation

**3. Creative Techniques**
- Layering shapes for complex designs
- Random variations for organic patterns
- Color schemes and palettes
- Drawing compound shapes (houses, faces, etc.)

**Embedded Exercises:**
1. 🎨 **Simple House** — Draw a house using rectangles and triangles
2. 🔲 **Checkerboard Pattern** — Create an 8×8 checkerboard using loops
3. 🎨 **Circle Grid** — Generate a grid of colored circles

**Estimated Time**: 35 minutes

---

#### **Module 3: Visualizing Data with Matplotlib**
**File**: [03_Visualizing_Data_matplotlib.md](content/03_Visualizing_Data_matplotlib.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab08/content/03_Visualizing_Data_matplotlib.ipynb)

**Data Storytelling** — Transform numbers into meaningful visual narratives.

**Topics Covered:**

**1. Basic Chart Types**
- Line charts: `plt.plot()` for trends over time
- Bar charts: `plt.bar()` for categorical comparisons
- Scatter plots: `plt.scatter()` for correlations
- Choosing the right chart type for your data

**2. Customization**
- Titles, labels, and legends
- Colors and markers
- Grid lines and axes configuration
- Multiple plots with subplots

**3. Data Integration**
- Creating data with NumPy arrays
- Plotting mathematical functions
- Visualizing real-world datasets
- Statistical visualizations

**Embedded Exercises:**
1. 📈 **Temperature Trends** — Plot weekly temperature data as a line chart
2. 📊 **Grade Distribution** — Create a bar chart showing grade frequencies

**Estimated Time**: 30 minutes

---

#### **Module 4: Integration and Mini-Projects**
**File**: [04_Integration_Mini_Projects.md](content/04_Integration_Mini_Projects.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab08/content/04_Integration_Mini_Projects.ipynb)

**Synthesis and Application** — Combine concepts to create complete visualizations.

**Topics Covered:**
- Combining ipycanvas and matplotlib
- Generating synthetic data for visualization
- Design principles for effective graphics
- Creative coding techniques

**Mini-Project Options:**
- **Option A**: Artistic Visualization — Create geometric art with array-based colors
- **Option B**: Data Dashboard — Generate and visualize synthetic dataset
- **Option C**: Pattern Generator — Build configurable pattern system

**Estimated Time**: 10 minutes

---

## Prerequisites

### Required Knowledge
- Completion of Labs 01-07
- Python loops (for, while) and conditionals
- Lists and list comprehensions
- Basic functions
- Understanding of arrays/lists

### Installation (will be covered in lab)
```python
# In Google Colab, run this at the start:
!pip install ipycanvas
import numpy as np
import matplotlib.pyplot as plt
```

---

## Getting Started

### Recommended Learning Path

**Phase 1: Fundamentals (15 min)**
1. Read Module 1 to understand graphics basics
2. Set up your Colab environment
3. Create your first canvas and draw simple shapes

**Phase 2: Creative Graphics (35 min)**
4. Work through Module 2 on ipycanvas
5. Complete all 4 drawing exercises
6. Experiment with patterns and colors

**Phase 3: Data Visualization (30 min)**
7. Progress to Module 3 on matplotlib
8. Complete all 4 visualization exercises
9. Practice customizing charts

**Phase 4: Integration (10 min)**
10. Choose and complete a mini-project from Module 4
11. Experiment with combining techniques

### Quick Start

```python
# Open a new Google Colab notebook
# Cell 1: Install ipycanvas
!pip install ipycanvas

# Cell 2: Import libraries
from ipycanvas import Canvas
import numpy as np
import matplotlib.pyplot as plt

# Cell 3: Create your first canvas
canvas = Canvas(width=400, height=300)
canvas.fill_style = '#2196F3'  # Blue color
canvas.fill_rect(50, 50, 200, 100)  # Draw a rectangle
canvas  # Display the canvas
```

---

## Key Programming Concepts

### From Previous Labs
- **Loops** (Lab 02-03): Now used to create repetitive patterns
- **Lists** (Lab 04): Store coordinate points and color values
- **Functions** (Lab 02-03): Encapsulate drawing routines
- **Objects and Methods** (Lab 06): Canvas and plot objects with methods
- **NumPy basics** (if covered): Array operations for data

### New Concepts
- **RGB Color Model**: Representing colors as (R, G, B) tuples
- **Coordinate Systems**: Positioning elements in 2D space
- **Canvas API**: Methods for drawing shapes and paths
- **Matplotlib API**: Methods for creating charts and plots
- **Visual Design**: Principles for creating effective graphics
- **Data Encoding**: Mapping data values to visual properties

---

## Common Challenges & Solutions

### Challenge 1: Canvas Doesn't Display

**Problem**: Canvas object created but nothing appears

**Solution**: Make sure the canvas object is the last line in the cell
```python
# ❌ Wrong - canvas not displayed
canvas = Canvas(width=400, height=300)
canvas.fill_rect(0, 0, 100, 100)
print("Done")

# ✅ Correct - canvas is last expression
canvas = Canvas(width=400, height=300)
canvas.fill_rect(0, 0, 100, 100)
canvas  # This line displays the canvas
```

---

### Challenge 2: Colors Look Wrong

**Problem**: Colors appear different than expected

**Solution**: Ensure RGB values are integers 0-255 or use hex strings
```python
# ❌ Wrong - values out of range
canvas.fill_style = 'rgb(300, 100, 50)'  # 300 is invalid

# ✅ Correct - valid RGB values
canvas.fill_style = 'rgb(255, 100, 50)'

# ✅ Also correct - hex color code
canvas.fill_style = '#FF6432'
```

---

### Challenge 3: Shapes Overlap Incorrectly

**Problem**: Later shapes hide earlier ones

**Solution**: Remember that drawing order matters (painter's algorithm)
```python
# Shapes are drawn in order, later ones appear on top
canvas.fill_style = 'red'
canvas.fill_rect(50, 50, 100, 100)  # Drawn first (behind)

canvas.fill_style = 'blue'
canvas.fill_rect(75, 75, 100, 100)  # Drawn second (on top)
```

---

### Challenge 4: Plot Doesn't Appear

**Problem**: `plt.plot()` runs but no chart appears

**Solution**: Call `plt.show()` to display the plot
```python
# ❌ Wrong - missing show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# ✅ Correct - explicitly show the plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('My Chart')
plt.show()
```

---

### Challenge 5: Loop Creates Unexpected Pattern

**Problem**: Nested loop doesn't create expected grid

**Solution**: Check loop ranges and variable usage
```python
# ❌ Wrong - using same variable
for i in range(5):
    for i in range(5):  # This shadows outer i!
        canvas.fill_rect(i*50, i*50, 40, 40)

# ✅ Correct - distinct loop variables
for row in range(5):
    for col in range(5):
        canvas.fill_rect(col*50, row*50, 40, 40)
```

---

## Additional Resources

### Official Documentation
- [ipycanvas Documentation](https://ipycanvas.readthedocs.io/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [HTML Color Picker](https://www.w3schools.com/colors/colors_picker.asp)

### Graphics Concepts
- [RGB Color Model Explained](https://en.wikipedia.org/wiki/RGB_color_model)
- [Computer Graphics Coordinate Systems](https://www.cs.uic.edu/~jbell/CourseNotes/ComputerGraphics/Coordinates.html)
- [Canvas API (Web Standard)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

### Data Visualization Resources
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Data Visualization Best Practices](https://www.tableau.com/learn/articles/data-visualization)
- [Choosing the Right Chart Type](https://chartio.com/learn/charts/how-to-choose-data-visualization/)

### Creative Coding
- [Processing (Creative Coding Framework)](https://processing.org/)
- [Generative Art Examples](https://www.artnome.com/news/2018/8/8/generative-art-finds-its-prodigy)
- [Math for Game Developers](https://www.youtube.com/playlist?list=PLW3Zl3wyJwWOpdhYedlD-yCB7WQoHf-My)

### Practice and Inspiration
- [Python Graph Gallery](https://www.python-graph-gallery.com/)
- [From Data to Viz](https://www.data-to-viz.com/)
- [Creative Coding Challenges](https://www.reddit.com/r/creativecoding/)

---

**Last Updated**: November 2025
**Course**: Introduction to Programming and Computer Science I
**Lab Duration**: 90 minutes
