# Introduction to Programming and CS I - Lab 07

## Interactive UIs: From Colab Widgets to Desktop Applications

### Overview

Lab 07 represents a critical shift in how you think about user interaction. Up to this point, you've built console applications that use text-based input/output or worked with data programmatically. Now you'll learn to create **interactive user interfaces** that respond to user actions in real-time.

Rather than diving straight into desktop GUI frameworks (which can be overwhelming), we'll build your intuition through **ipywidgets** in Google Colab—a familiar environment where you can experiment rapidly. You'll then apply these concepts to build professional desktop applications using **Qt Designer** and **PySide6**.

**Primary Focus**: Understanding event-driven programming and interactive UI patterns
**Secondary Focus**: Transitioning web-based UIs to desktop applications

**Core Philosophy**: **"Prototype in the browser, productionize on the desktop"** — Validate your UI concepts quickly in Colab before investing in desktop development.

---

## Understanding Event-Driven Programming

Traditional programs you've written follow a **procedural model**: they start at the top, execute line by line, and end. Interactive UIs require a fundamentally different paradigm: **event-driven programming**.

### The Event Loop

In event-driven programs:

```python
# Pseudocode for event-driven flow
while application_is_running:
    event = wait_for_user_action()  # Click, type, select, etc.
    handler = find_handler_for(event)
    handler(event)
```

The program waits for user actions (events) and responds by executing specific functions (event handlers). This is how all modern GUIs work—from web apps to desktop applications to mobile apps.

### Why This Matters for Lab 07

Throughout this lab, you're learning to:
- **Design interactive interfaces** with appropriate widgets for different input types
- **Handle events** by connecting user actions to Python functions
- **Validate and provide feedback** to guide users toward valid inputs
- **Apply layout principles** to create intuitive, professional-looking UIs

This prepares you for modern application development, whether you're building data analysis tools, web applications, or desktop software.

**Key Insight**: Good UI design is about clear communication—the interface should make it obvious what actions are available and what will happen when the user interacts with it.

---

## Learning Objectives

By the end of this lab, students will be able to:

### Conceptual Understanding
- ✅ Explain the event-driven programming paradigm
- ✅ Understand the relationship between widgets, events, and handlers
- ✅ Articulate UI/UX principles: affordances, feedback, validation
- ✅ Distinguish between web-based and desktop UI architectures

### Technical Skills
- ✅ Create interactive interfaces using ipywidgets in Colab
- ✅ Handle user events with `.on_click()` and `.observe()` patterns
- ✅ Apply layout containers (HBox, VBox, GridBox) for organization
- ✅ Design desktop UIs visually using Qt Designer
- ✅ Load and connect Qt Designer `.ui` files in PySide6
- ✅ Implement signal/slot connections for desktop events

### Practical Application
- ✅ Build working prototypes in Colab with validation and feedback
- ✅ Convert Colab prototypes to PySide6 desktop applications
- ✅ Create data visualization widgets with matplotlib integration
- ✅ Apply best practices for separating UI from business logic
- ✅ Version control UI definition files (.ui) appropriately

---

## Lab Structure

### 📚 Core Content Modules

#### **Module 1: Introduction to ipywidgets**
**File**: [01_Introduction_to_Widgets.md](content/01_Introduction_to_Widgets.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab07/content/01_Introduction_to_Widgets.ipynb)

**Your First Interactive UI** — Learn widget basics in a familiar Colab environment.

**Topics Covered:**
- Widget fundamentals: Button, Text, Dropdown, IntSlider, Checkbox
- Output widget for displaying results
- Event handling: `.on_click()` for buttons
- Event observation: `.observe()` for value changes
- Basic validation and error handling

**Key Insights:**
- Widgets maintain state (their current value)
- Events trigger function calls (handlers)
- The Output widget provides a clean feedback mechanism
- Validation prevents errors and guides users

**Embedded Exercises:**
1. Widget Explorer — Create and test each widget type
2. Event Detective — Connect handlers to understand event flow
3. Temperature Converter — Build your first interactive app
4. Validation Practice — Add input checking and error messages
5. Multi-Widget Interaction — Coordinate multiple widgets

---

#### **Module 2: Layout and UX Concepts**
**File**: [02_Layout_and_UX.md](content/02_Layout_and_UX.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devomh/comp3083_2025/blob/main/lab07/content/02_Layout_and_UX.ipynb)

**Making UIs Professional and Usable** — Transform functional widgets into polished interfaces.

**Topics Covered:**
- Layout containers: HBox (horizontal), VBox (vertical), GridBox (grid)
- Visual hierarchy and grouping related controls
- UX principles: affordances, feedback, disabled states
- Integration with matplotlib for data visualization
- Real-time updates and continuous vs. discrete events

**Mental Model**: Layout is about communication—group related controls, provide clear visual hierarchy, and give immediate feedback.

**Embedded Exercises:**
1. Layout Challenge — Reorganize widgets for better UX
2. Data Science Visualizer — Build interactive filter with plots
3. Feedback Patterns — Implement validation with visual cues
4. State Management — Control widget enable/disable states
5. Polish Your UI — Apply professional styling

**Data Science Focus**: Complete working example with 500-sample dataset, statistical calculations, and matplotlib visualization (histogram and box plot).

---

#### **Module 3: Qt Designer and Desktop Apps**
**File**: [03_Qt_Designer_Desktop.md](content/03_Qt_Designer_Desktop.md)

**From Browser to Desktop** — Transition your Colab prototypes to professional desktop applications.

**Topics Covered:**

**1. Why GUI Designers?**
- Visual development vs. code-first approaches
- Separation of UI design from business logic
- Rapid iteration and consistency

**2. Qt Designer Workflow**
- Creating a MainWindow
- Widget palette and property editor
- Setting object names (crucial for code access)
- Applying layouts visually
- Saving .ui files (XML format)

**3. PySide6 Integration**
- Two approaches: runtime loading vs. compiled UI
- Loading .ui files with QUiLoader
- Compiling with pyside6-uic
- Trade-offs and when to use each approach

**4. Signal/Slot Connections**
- Qt's signal/slot mechanism
- Connecting button clicks to Python methods
- Accessing widget values
- Updating display widgets

**Step-by-Step Tutorial**: Convert the temperature converter from Module 1 to a desktop app.

---

#### **Module 4: Integration and Best Practices**
**File**: [04_Integration_Best_Practices.md](content/04_Integration_Best_Practices.md)

**Professional Workflows and Patterns** — Learn industry best practices for GUI development.

**Topics Covered:**

**1. Separation of Concerns**
- Never edit generated files
- Keep business logic separate from UI code
- Model-View pattern basics

**2. Validation Strategies**
- Input validation before processing
- Visual feedback for errors
- Graceful error handling

**3. Project Organization**
- Directory structure for GUI projects
- Versioning .ui files and resources
- Requirements and environment management

**4. Desktop vs. Colab Comparison**
- When to use each approach
- Strengths and limitations
- Deployment considerations

**Integrated Exercise**: Complete working data analysis tool with both Colab and desktop versions.

---

## Prerequisites

### Required Knowledge
- Completion of Labs 01-06
- Python functions and error handling
- Working with lists and dictionaries
- Basic matplotlib plotting (helpful but not required)

### Technical Setup
- **For Colab modules**: Google account
- **For desktop modules**:
  - Python 3.10+ installed locally
  - VS Code with Python extension
  - Ability to install packages via pip
  - Terminal/command line access

---

## Getting Started

### Recommended Learning Path

**Phase 1: Colab Prototyping (Modules 1-2)**
1. Work through Module 1 to understand widget basics
2. Complete all Module 1 exercises in Colab
3. Progress to Module 2 for layout and visualization
4. Build the data science visualizer example
5. **Deliverable A**: Working Colab prototype with validation

**Phase 2: Desktop Development (Modules 3-4)**
6. Set up local Python environment with PySide6
7. Follow Module 3 Qt Designer tutorial
8. Convert your Colab prototype to desktop app
9. Complete Module 4 integration exercises
10. **Deliverable B**: PySide6 desktop application

### Quick Start - Colab

```python
# In a Colab notebook
import ipywidgets as W
from IPython.display import display

button = W.Button(description='Click Me!')
output = W.Output()

def on_click(b):
    with output:
        print("Hello, interactive UIs!")

button.on_click(on_click)
display(button, output)
```

### Quick Start - Desktop

```bash
# Set up environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install PySide6
pip install pyside6

# Launch Qt Designer
pyside6-designer

# Run your app
python main.py
```

---

## Key Programming Concepts

### From Previous Labs
- **Functions** (Lab 02-03): Now used as event handlers
- **Error Handling** (Lab 03): Critical for validating user input
- **Dictionaries** (Lab 04): Useful for mapping options to actions
- **matplotlib** (various): Integration with interactive widgets
- **Object-oriented thinking** (Lab 06): Understanding widget objects and methods

### New Concepts
- **Event-Driven Programming**: Wait for user actions, respond with handlers
- **State Management**: Widgets maintain current values
- **Signal/Slot Pattern**: Qt's mechanism for connecting events to handlers
- **UI/UX Principles**: Affordances, feedback, validation, visual hierarchy
- **Layout Management**: Organizing widgets spatially
- **Generated Code**: Working with auto-generated files appropriately

---

## Common Challenges & Solutions

### Challenge 1: Event Handler Called Immediately

**Problem**: Handler executes when setting up the widget, not when clicked

**Solution**: Pass function reference, not function call
```python
# ❌ Wrong - calls function immediately
button.on_click(my_handler())

# ✅ Correct - passes function reference
button.on_click(my_handler)
```

---

### Challenge 2: Can't Access Widget Values in Handler

**Problem**: `NameError` when trying to read widget values in event handler

**Solution**: Ensure widgets are defined before handlers reference them, or use event parameters
```python
# ✅ Define widgets first
text_input = W.Text(description='Name:')

# ✅ Then define handler that uses them
def on_submit(b):
    name = text_input.value  # Accessible
    print(f"Hello, {name}!")

submit_btn = W.Button(description='Submit')
submit_btn.on_click(on_submit)
```

---

### Challenge 3: Output Widget Shows Old Results

**Problem**: New results append instead of replacing

**Solution**: Clear output before printing
```python
def on_calculate(b):
    with output:
        output.clear_output()  # ✅ Clear old results
        print(f"Result: {calculate()}")
```

---

### Challenge 4: Qt Designer .ui File Won't Load

**Problem**: `FileNotFoundError` when loading .ui file

**Solution**: Check file path and working directory
```python
# ❌ Assumes specific working directory
f = QFile('mainwindow.ui')

# ✅ Use absolute path or pathlib
from pathlib import Path
ui_path = Path(__file__).parent / 'mainwindow.ui'
f = QFile(str(ui_path))
```

---

### Challenge 5: Changes in Qt Designer Don't Appear

**Problem**: Modified .ui file but app looks the same

**Solution**:
- If loading at runtime: restart app (file is re-read)
- If using compiled approach: re-compile with `pyside6-uic`
```bash
# Re-compile after Designer changes
pyside6-uic mainwindow.ui -o ui_mainwindow.py
```

---

## Assessment & Success Criteria

Students demonstrate mastery by:

### Conceptual Understanding (30%)
- ✅ Correctly explain event-driven programming flow
- ✅ Identify appropriate widgets for different input types
- ✅ Apply UX principles to create intuitive interfaces

### Technical Proficiency (40%)
- ✅ Create working interactive UIs in Colab
- ✅ Implement proper event handling and validation
- ✅ Use Qt Designer to build desktop UIs
- ✅ Successfully connect signals to slots in PySide6
- ✅ Organize code with proper separation of concerns

### Practical Application (30%)
- ✅ **Deliverable A**: Working Colab prototype with validation and feedback
- ✅ **Deliverable B**: PySide6 desktop app recreating Colab functionality
- ✅ Code demonstrates best practices (validation, error handling, clean structure)

### Formative Checkpoints
- **Mid-lab**: Button click triggers valid conversion and updates output
- **Exit ticket**: Add input validator that disables action until input is valid

---

## Additional Resources

### Official Documentation
- [ipywidgets Documentation](https://ipywidgets.readthedocs.io/)
- [PySide6 Documentation](https://doc.qt.io/qtforpython/)
- [Qt Designer Manual](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [Qt Signal/Slot Documentation](https://doc.qt.io/qt-6/signalsandslots.html)

### Widget-Specific References
- [ipywidgets Widget List](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)
- [Qt Widget Gallery](https://doc.qt.io/qt-6/gallery.html)
- [matplotlib Widget Integration](https://matplotlib.org/stable/gallery/widgets/index.html)

### Tutorials and Guides
- [Real Python - PyQt/PySide](https://realpython.com/python-pyqt-gui-calculator/)
- [Python GUIs - PySide6 Tutorial](https://www.pythonguis.com/pyside6-tutorial/)
- [ipywidgets Examples](https://github.com/jupyter-widgets/ipywidgets/tree/master/docs/source/examples)

### UI/UX Design Resources
- [Nielsen Norman Group - UI Guidelines](https://www.nngroup.com/)
- [Material Design Principles](https://material.io/design)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Deliverables

### Deliverable A: Colab Prototype
Create a working interactive application in Google Colab that:
- Uses at least 3 different widget types
- Implements proper event handling
- Includes input validation with user feedback
- Applies layout principles (HBox/VBox)
- Handles errors gracefully

**Suggested projects**: Temperature converter, tip calculator, BMI calculator, or the data science visualizer

### Deliverable B: PySide6 Desktop App
Recreate your Colab prototype as a desktop application that:
- Uses Qt Designer to create the UI (.ui file)
- Loads the UI in Python (runtime or compiled approach)
- Connects signals to working event handlers
- Implements the same validation logic
- Follows separation of concerns (logic separate from UI)

**Submission requirements**:
- Source code (main.py)
- UI definition file (mainwindow.ui)
- Requirements file (requirements.txt)
- Brief README with setup/run instructions

---

## Troubleshooting

### Issue: ipywidgets don't display in Colab
**Cause**: Usually notebook needs restart or widgets extension issue
**Solution**: Runtime → Restart runtime, then re-run cells

### Issue: PySide6 installation fails
**Cause**: Python version incompatibility or pip issues
**Solution**:
```bash
# Verify Python version
python --version  # Should be 3.10+

# Upgrade pip first
python -m pip install --upgrade pip

# Then install PySide6
pip install pyside6
```

### Issue: pyside6-designer command not found
**Cause**: Command not in PATH
**Solution**:
```bash
# Find where it's installed
python -c "import PySide6; print(PySide6.__path__)"

# On Windows, might be at:
# .venv\Scripts\pyside6-designer.exe

# On macOS/Linux:
# .venv/bin/pyside6-designer
```

### Issue: Widget layout looks wrong
**Cause**: Missing layout on container
**Solution**: In Qt Designer, right-click the form → Lay Out → choose layout type

---

## Extension Projects

Once you've completed the core modules, try these challenges:

### 1. Resource Management
- Add icons to buttons using Qt resource files (.qrc)
- Compile resources with `pyside6-rcc`
- Use icons in your application

### 2. Persistence
- Save user settings to JSON file
- Load previous settings on app start
- Add "Reset to Defaults" functionality

### 3. Advanced Widgets
- Implement a todo list with QListWidget
- Create a multi-tab interface with QTabWidget
- Add a menu bar and status bar

### 4. Data Analysis Tool
- Build a CSV file loader
- Display data in QTableWidget
- Add filtering and sorting capabilities
- Generate matplotlib plots in the UI

---

**Last Updated**: October 2025
**Course**: Introduction to Programming and Computer Science I
