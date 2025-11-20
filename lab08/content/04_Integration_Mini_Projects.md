# Module 4: Integration and Mini-Projects

## Bringing It All Together

**Learning Objectives:**
- Combine ipycanvas graphics with matplotlib visualizations
- Generate synthetic data programmatically for visualization
- Apply design principles to create cohesive projects
- Demonstrate creative and analytical thinking through code

**Estimated Time**: 10 minutes

---

## Integration: Graphics + Data Visualization

You now have two powerful tools:
- **ipycanvas**: For creative graphics and geometric patterns
- **matplotlib**: For data visualization and charts

While these tools serve different purposes, you can use them together in your projects to create rich, multi-faceted visualizations.

---

## Mini-Project Guidelines

Choose **one** of the three project options below. Each project should:

1. **Be complete and functional** - Runs without errors
2. **Demonstrate skills from this lab** - Uses loops, arrays, colors, and customization
3. **Show creativity** - Add your personal touch
4. **Be well-documented** - Include comments explaining your code

**Time Allocation**: Spend about 10 minutes on your chosen project. Don't aim for perfection—aim for a working demonstration of your skills!

---

## Option A: Artistic Visualization

### Project Description
Create a visually appealing geometric pattern or design using ipycanvas. Use arrays to control colors, loops to create repetition, and mathematical calculations to create interesting variations.

### Requirements
- ✅ Use at least 20 graphical elements (shapes)
- ✅ Implement pattern generation using loops
- ✅ Use an array of colors (at least 4 different colors)
- ✅ Include at least two different shape types (circles, rectangles, triangles, etc.)
- ✅ Apply mathematical variation (size, position, or color changes)

### Starter Template

```python
import math
import random
from ipycanvas import Canvas

# Create canvas
canvas = Canvas(width=600, height=600)

# Define color palette
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A',
          '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']

# Your artistic code here
# Example: Spiral of circles with varying colors

center_x = 300
center_y = 300
num_circles = 30
max_radius = 250

for i in range(num_circles):
    angle = i * (2 * math.pi / 10)  # Spiral angle
    radius = (i / num_circles) * max_radius  # Distance from center

    # Calculate position
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    # Choose color
    color_index = i % len(colors)
    canvas.fill_style = colors[color_index]

    # Draw circle with size based on position
    circle_size = 10 + (i * 0.5)
    canvas.fill_arc(x, y, circle_size, 0, 2 * math.pi)

canvas
```

### Ideas for Inspiration
- **Mandala pattern**: Concentric circles with rotational symmetry
- **Geometric tessellation**: Repeating patterns that tile the canvas
- **Color gradient landscape**: Abstract scene using gradients
- **Spiral galaxy**: Circles arranged in a spiral with fading colors
- **Kaleidoscope**: Mirrored patterns in quadrants
- **Abstract art**: Random but aesthetically pleasing arrangement

### Evaluation Criteria
- Visual appeal and creativity
- Effective use of loops and arrays
- Code organization and comments
- Complexity of pattern generation

---

## Option B: Data Dashboard

### Project Description
Generate synthetic (made-up) data using Python, then visualize it using matplotlib. Create multiple related charts that tell a story about your data.

### Requirements
- ✅ Generate data programmatically (using loops, random numbers, or formulas)
- ✅ Create at least 2 different chart types
- ✅ All charts must be properly labeled (titles, axes, legends)
- ✅ Data should be related/tell a coherent story
- ✅ Apply consistent color scheme across charts

### Starter Template

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data
# Example: Student performance data

np.random.seed(42)  # For reproducible results

# Generate data for 30 students
study_hours = np.random.uniform(1, 10, 30)  # 1-10 hours per week
base_score = study_hours * 8 + 20  # Base score based on study time
test_scores = base_score + np.random.normal(0, 5, 30)  # Add randomness
test_scores = np.clip(test_scores, 0, 100)  # Keep in valid range

# Chart 1: Scatter plot showing correlation
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  # First chart in 1×2 grid
plt.scatter(study_hours, test_scores, color='#4ECDC4', s=100, alpha=0.6, edgecolors='black')
plt.xlabel('Study Hours per Week', fontsize=11)
plt.ylabel('Test Score', fontsize=11)
plt.title('Study Time vs. Performance', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Chart 2: Histogram of score distribution
plt.subplot(1, 2, 2)  # Second chart in 1×2 grid
plt.hist(test_scores, bins=10, color='#FF6B6B', edgecolor='black', alpha=0.7)
plt.xlabel('Test Score', fontsize=11)
plt.ylabel('Number of Students', fontsize=11)
plt.title('Score Distribution', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# Optional: Add more charts or statistics
print(f"Average score: {np.mean(test_scores):.1f}")
print(f"Highest score: {np.max(test_scores):.1f}")
print(f"Lowest score: {np.min(test_scores):.1f}")
```

### Dataset Ideas
- **Weather simulation**: Temperature, precipitation, humidity over time
- **Sales data**: Product sales across months/categories
- **Fitness tracker**: Steps, calories, active minutes over weeks
- **Social media analytics**: Likes, comments, shares across posts
- **Game statistics**: Player scores, levels achieved, time played
- **Survey results**: Ratings across different questions/categories

### Suggested Chart Combinations
1. **Line chart + bar chart**: Trends over time + category comparison
2. **Scatter plot + histogram**: Correlation + distribution
3. **Multiple line charts + grouped bars**: Time trends + comparisons
4. **Scatter + trend line + bar**: Relationship + summary statistics

### Evaluation Criteria
- Data generation creativity and realism
- Appropriate chart type selection
- Clear labeling and professional appearance
- Insightful data relationships

---

## Option C: Pattern Generator

### Project Description
Create a configurable pattern generator that creates different geometric patterns based on parameters. Users can adjust variables to create variations.

### Requirements
- ✅ Generate at least 3 different pattern types
- ✅ Use variables to control pattern parameters (size, spacing, colors)
- ✅ Include clear comments explaining each pattern
- ✅ Demonstrate mastery of loops and conditional logic
- ✅ Patterns should be visually distinct from each other

### Starter Template

```python
import math
from ipycanvas import Canvas

# Pattern configuration
pattern_type = 1  # Change this to switch patterns (1, 2, or 3)
canvas = Canvas(width=500, height=500)

# Color palettes for each pattern
palette_1 = ['#FF6B6B', '#4ECDC4', '#45B7D1']
palette_2 = ['#F7DC6F', '#BB8FCE', '#85C1E2']
palette_3 = ['#FF9999', '#99FF99', '#9999FF']

if pattern_type == 1:
    # PATTERN 1: Concentric circles with alternating colors
    print("Pattern 1: Concentric Circles")

    center_x = 250
    center_y = 250
    num_circles = 15

    for i in range(num_circles, 0, -1):  # Draw from outside to inside
        radius = i * 15
        color = palette_1[i % len(palette_1)]
        canvas.fill_style = color
        canvas.fill_arc(center_x, center_y, radius, 0, 2 * math.pi)

elif pattern_type == 2:
    # PATTERN 2: Grid with rotating squares
    print("Pattern 2: Rotated Square Grid")

    rows = 8
    cols = 8
    cell_size = 60

    for row in range(rows):
        for col in range(cols):
            x = 10 + col * cell_size + cell_size / 2
            y = 10 + row * cell_size + cell_size / 2

            color = palette_2[(row + col) % len(palette_2)]
            canvas.fill_style = color

            # Draw rotated square (approximated with rectangle)
            size = 40 if (row + col) % 2 == 0 else 30
            canvas.fill_rect(x - size/2, y - size/2, size, size)

elif pattern_type == 3:
    # PATTERN 3: Radiating lines with circles
    print("Pattern 3: Radiating Lines")

    center_x = 250
    center_y = 250
    num_lines = 24
    line_length = 200

    for i in range(num_lines):
        angle = i * (2 * math.pi / num_lines)

        # Calculate end point
        end_x = center_x + line_length * math.cos(angle)
        end_y = center_y + line_length * math.sin(angle)

        # Draw line
        color = palette_3[i % len(palette_3)]
        canvas.stroke_style = color
        canvas.line_width = 3
        canvas.stroke_line(center_x, center_y, end_x, end_y)

        # Draw circle at end
        canvas.fill_style = color
        canvas.fill_arc(end_x, end_y, 10, 0, 2 * math.pi)

canvas
```

### Pattern Ideas
1. **Checkerboard variations**: Different colors, sizes, or shapes
2. **Spiral patterns**: Archimedean spiral, logarithmic spiral
3. **Wave patterns**: Sine waves with varying amplitude/frequency
4. **Mosaic**: Random colored tiles
5. **Starburst**: Lines radiating from center with gradients
6. **Hexagonal grid**: Tessellating hexagons
7. **Concentric polygons**: Nested squares, triangles, or hexagons

### Evaluation Criteria
- Pattern variety and distinctness
- Clean code with clear configuration variables
- Proper use of mathematical calculations
- Visual quality of patterns

---

## Advanced Integration: Canvas + Matplotlib Side-by-Side

For students who finish early, try displaying both types of visualizations together:

```python
import math
import matplotlib.pyplot as plt
import numpy as np
from ipycanvas import Canvas

# Part 1: Generate data and create matplotlib visualization
np.random.seed(42)
data = np.random.normal(50, 15, 100)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(data, bins=15, color='#4ECDC4', edgecolor='black')
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.boxplot(data, vert=True)
plt.title('Data Summary')
plt.ylabel('Value')

plt.tight_layout()
plt.show()

# Part 2: Create complementary ipycanvas graphic
canvas = Canvas(width=600, height=200)

# Visual representation of data range
min_val = int(np.min(data))
max_val = int(np.max(data))
mean_val = int(np.mean(data))

# Draw range
canvas.fill_style = '#E0E0E0'
canvas.fill_rect(50, 80, 500, 40)

# Draw mean indicator
mean_x = 50 + ((mean_val - min_val) / (max_val - min_val)) * 500
canvas.fill_style = '#FF6B35'
canvas.fill_rect(mean_x - 3, 70, 6, 60)

# Add labels
canvas.fill_style = '#000000'
# Note: ipycanvas doesn't have built-in text, but we show the structure
print(f"Range: {min_val} to {max_val}")
print(f"Mean: {mean_val}")

canvas
```

---

## Reflection Questions

After completing your mini-project, consider these questions:

1. **What was the most challenging part?**
   - Understanding the math?
   - Getting the colors right?
   - Organizing the code?
   - Debugging issues?

2. **What would you improve with more time?**
   - More complexity?
   - Better color schemes?
   - Additional features?
   - Cleaner code?

3. **How could you extend this project?**
   - Make it interactive (with ipywidgets from Lab 07)?
   - Add animation frames?
   - Connect to real data from an API?
   - Create variations with random parameters?

4. **What did you learn about the relationship between code and visuals?**
   - How small code changes affect appearance
   - The power of loops for repetition
   - How math creates visual patterns
   - The importance of color and spacing

---

## Showcasing Your Work

### Save Your Visualizations

```python
# For matplotlib
plt.savefig('my_visualization.png', dpi=300, bbox_inches='tight')

# For ipycanvas: Take a screenshot of the output
# Or use browser dev tools to save the canvas element
```

### Document Your Process

Create a brief markdown cell above your code explaining:
- What you created
- What techniques you used
- Any challenges you overcame
- Ideas for future improvements

**Example**:
```markdown
## My Artistic Spiral Pattern

I created a multi-colored spiral using polar coordinates and the golden ratio
for spacing. The pattern uses 50 circles that gradually change size and color
as they spiral outward from the center.

**Techniques used:**
- Polar coordinate math (cos/sin)
- Color cycling through an array
- Mathematical progressions for sizing

**Challenges:**
- Getting the spacing just right required experimentation with the angle increment
- Choosing a color palette that looked good together

**Future ideas:**
- Add a second spiral going the opposite direction
- Make the colors transition smoothly instead of discrete steps
- Add some randomness for organic variation
```

---

## Extending Beyond the Lab

### Ideas for Personal Projects

1. **Data Visualization Blog**
   - Find interesting datasets online
   - Create visualizations telling their story
   - Practice different chart types

2. **Generative Art Gallery**
   - Create a collection of algorithmic art pieces
   - Experiment with randomness and parameters
   - Share your favorite creations

3. **Interactive Dashboards** (combining with Lab 07)
   - Add sliders to control pattern parameters
   - Create buttons to switch between visualizations
   - Build a mini data exploration tool

4. **Mathematical Explorations**
   - Visualize fractals (Mandelbrot, Julia sets)
   - Plot parametric equations
   - Explore chaos theory with attractors

5. **Real-World Data Projects**
   - Personal fitness data tracker
   - Budget visualization tool
   - Weather pattern analyzer
   - Social media engagement tracker

---

## Resources for Further Learning

### Creative Coding
- [Processing.org](https://processing.org/) - Creative coding platform
- [The Nature of Code](https://natureofcode.com/) - Algorithms and art
- [Creative Coding on YouTube](https://www.youtube.com/c/TheCodingTrain) - Tutorial videos

### Data Visualization
- [Data Viz Project](https://datavizproject.com/) - Chart type reference
- [Flowing Data](https://flowingdata.com/) - Data visualization blog
- [Information is Beautiful](https://informationisbeautiful.net/) - Inspiring visualizations

### Color Theory
- [Coolors.co](https://coolors.co/) - Color palette generator
- [Adobe Color](https://color.adobe.com/) - Color wheel tool
- [Color Hunt](https://colorhunt.co/) - Curated color palettes

### Mathematics for Graphics
- [Better Explained](https://betterexplained.com/) - Intuitive math explanations
- [Khan Academy](https://www.khanacademy.org/) - Trigonometry, algebra
- [3Blue1Brown](https://www.youtube.com/c/3blue1brown) - Visual math on YouTube

---

## Lab Completion Checklist

Before you finish, make sure you've completed:

- ✅ **Module 1**: Understand RGB colors and coordinate systems
- ✅ **Module 2**: Complete all 4 ipycanvas exercises
  - Exercise 1: Simple House
  - Exercise 2: Checkerboard Pattern
  - Exercise 3: Circle Grid
  - Exercise 4: Color Gradient
- ✅ **Module 3**: Complete all 4 matplotlib exercises
  - Exercise 1: Temperature Trends
  - Exercise 2: Grade Distribution
  - Exercise 3: Correlation Scatter Plot
  - Exercise 4: Mathematical Functions
- ✅ **Module 4**: Complete one mini-project
  - Option A: Artistic Visualization
  - Option B: Data Dashboard
  - Option C: Pattern Generator
- ✅ **Documentation**: Add comments explaining your code
- ✅ **Experimentation**: Try variations and explore beyond requirements

---

## Final Thoughts

**Congratulations!** You've learned to create visual output with code—a skill that bridges programming logic with creative expression and analytical thinking.

Remember:
- **Every complex visualization starts simple** - Build incrementally
- **Experimentation is learning** - Try things and see what happens
- **Beauty is in the details** - Small adjustments matter
- **Code is creative** - There's no single "right" answer

The skills you've learned here—loops, arrays, functions, coordinate systems, and visual design—are fundamental to:
- Game development
- Data science
- Web development
- Scientific computing
- Digital art
- User interface design

Keep practicing, keep creating, and most importantly—have fun with code!

---

**End of Lab 08** - Graphics Generation and Data Visualization
