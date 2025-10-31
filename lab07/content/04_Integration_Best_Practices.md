# Module 4: Integration and Best Practices

## Professional Workflows and Patterns

**Learning Objectives:**
- Apply separation of concerns in GUI projects
- Organize desktop applications professionally
- Compare Colab and desktop development workflows
- Version control UI files and resources effectively
- Deploy and distribute desktop applications

---

## Separation of Concerns

### The Problem: Mixing UI and Logic

**Bad Example:**
```python
def on_calculate_click(self):
    # ❌ All logic crammed in the event handler
    value1 = self.ui.input1.value()
    value2 = self.ui.input2.value()

    # Complex calculation mixed with UI code
    if value1 > 0 and value2 > 0:
        result = (value1 * 1.08) + (value2 * 0.92)
        final = result / 2.5
        formatted = f"${final:.2f}"
        self.ui.resultLabel.setText(formatted)
    else:
        self.ui.resultLabel.setText("Error")
```

**Problems:**
- Hard to test (requires UI)
- Can't reuse logic elsewhere
- Difficult to maintain
- Business logic tied to UI implementation

---

### The Solution: Separate Business Logic

**Good Example:**
```python
# business_logic.py
def calculate_price(base_price, quantity, tax_rate=0.08):
    """
    Calculate total price with tax.

    Args:
        base_price: Price per unit
        quantity: Number of units
        tax_rate: Tax rate (default 8%)

    Returns:
        Total price including tax

    Raises:
        ValueError: If inputs are invalid
    """
    if base_price <= 0 or quantity <= 0:
        raise ValueError("Price and quantity must be positive")

    subtotal = base_price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax

    return total

# main.py
from business_logic import calculate_price

class MainWindow(QMainWindow):
    def on_calculate_click(self):
        """Handle calculate button click"""
        try:
            price = self.ui.priceInput.value()
            quantity = self.ui.quantityInput.value()

            # Call separate business logic
            total = calculate_price(price, quantity)

            # Only UI concerns here
            self.ui.resultLabel.setText(f"${total:.2f}")

        except ValueError as e:
            self.ui.resultLabel.setText(f"Error: {e}")
```

**Benefits:**
- ✅ Can test `calculate_price()` without UI
- ✅ Can reuse in web app, API, CLI
- ✅ Clear separation: UI handles display, logic handles computation
- ✅ Easier to maintain and debug

---

## Project Organization

### Small Project Structure

```
temperature_converter/
├── .venv/                  # Virtual environment (not in git)
├── .gitignore             # Ignore .venv, __pycache__, etc.
├── main.py                # Application entry point
├── mainwindow.ui          # UI definition (in git)
├── logic.py               # Business logic
├── requirements.txt       # Dependencies
└── README.md             # Setup and run instructions
```

### Medium Project Structure

```
data_analyzer/
├── .venv/
├── .gitignore
├── main.py               # Entry point
├── ui/
│   ├── mainwindow.ui     # Main UI
│   └── settings.ui       # Settings dialog
├── logic/
│   ├── __init__.py
│   ├── filters.py        # Data filtering logic
│   ├── statistics.py     # Statistical calculations
│   └── visualization.py  # Plot generation logic
├── resources/
│   ├── icons/           # Application icons
│   └── data/            # Sample datasets
├── tests/
│   ├── test_filters.py
│   └── test_statistics.py
├── requirements.txt
└── README.md
```

### What to Version Control

**.gitignore:**
```
# Virtual environment
.venv/
venv/
env/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Compiled UI (if using compiled approach)
ui_*.py
*_rc.py

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# User data
*.db
*.sqlite
user_data/
```

**DO version control:**
- ✅ .ui files (they're XML, merge-friendly)
- ✅ .qrc files (resource definitions)
- ✅ Source Python files
- ✅ requirements.txt
- ✅ README.md
- ✅ License

**DON'T version control:**
- ❌ Compiled UI files (ui_*.py) - regenerate from .ui
- ❌ Virtual environments (.venv)
- ❌ __pycache__ directories
- ❌ User-specific settings

---

## Validation Strategies

### Input Validation Patterns

**1. Validate on Input (Real-Time)**

```python
def __init__(self):
    # ...
    self.ui.emailInput.textChanged.connect(self.validate_email)

def validate_email(self):
    """Validate email as user types"""
    email = self.ui.emailInput.text()

    if not email:
        # Empty is neutral
        self.ui.emailInput.setStyleSheet("")
        self.ui.submitButton.setEnabled(False)
    elif self.is_valid_email(email):
        # Valid - green
        self.ui.emailInput.setStyleSheet("border: 2px solid green;")
        self.ui.submitButton.setEnabled(True)
    else:
        # Invalid - red
        self.ui.emailInput.setStyleSheet("border: 2px solid red;")
        self.ui.submitButton.setEnabled(False)

def is_valid_email(self, email):
    """Simple email validation"""
    return '@' in email and '.' in email.split('@')[-1]
```

**2. Validate on Submit (Form-Level)**

```python
def on_submit(self):
    """Validate all fields before processing"""
    errors = []

    name = self.ui.nameInput.text().strip()
    if not name:
        errors.append("Name is required")

    age = self.ui.ageInput.value()
    if age < 18:
        errors.append("Must be 18 or older")

    email = self.ui.emailInput.text()
    if not self.is_valid_email(email):
        errors.append("Invalid email format")

    if errors:
        # Show all errors
        error_msg = "\n".join(f"• {e}" for e in errors)
        self.ui.errorLabel.setText(error_msg)
        self.ui.errorLabel.setStyleSheet("color: red;")
        return

    # All valid - process
    self.process_form(name, age, email)
```

**3. Use Built-in Validators**

Qt provides validators for common patterns:

```python
from PySide6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

# Integer only
int_validator = QIntValidator(0, 100)  # Range 0-100
self.ui.ageInput.setValidator(int_validator)

# Float with 2 decimals
double_validator = QDoubleValidator(0.00, 9999.99, 2)
self.ui.priceInput.setValidator(double_validator)

# Regex pattern (e.g., phone number)
phone_regex = QRegularExpression(r'\d{3}-\d{3}-\d{4}')
phone_validator = QRegularExpressionValidator(phone_regex)
self.ui.phoneInput.setValidator(phone_validator)
```

---

## Error Handling

### Defensive Programming

```python
def load_data_file(self):
    """Load data with proper error handling"""
    try:
        file_path = self.ui.filePathInput.text()

        if not file_path:
            self.show_error("Please select a file")
            return

        path = Path(file_path)

        if not path.exists():
            self.show_error(f"File not found: {file_path}")
            return

        if path.suffix != '.csv':
            self.show_error("Only CSV files are supported")
            return

        # Attempt to load
        data = pd.read_csv(path)

        if data.empty:
            self.show_warning("File is empty")
            return

        # Success
        self.data = data
        self.show_success(f"Loaded {len(data)} rows")
        self.update_display()

    except pd.errors.EmptyDataError:
        self.show_error("File is empty or corrupted")
    except pd.errors.ParserError:
        self.show_error("File format is invalid")
    except PermissionError:
        self.show_error("Permission denied to read file")
    except Exception as e:
        self.show_error(f"Unexpected error: {e}")

def show_error(self, message):
    """Display error message to user"""
    self.ui.statusLabel.setText(f"❌ {message}")
    self.ui.statusLabel.setStyleSheet("color: red;")

def show_warning(self, message):
    """Display warning message"""
    self.ui.statusLabel.setText(f"⚠️  {message}")
    self.ui.statusLabel.setStyleSheet("color: orange;")

def show_success(self, message):
    """Display success message"""
    self.ui.statusLabel.setText(f"✓ {message}")
    self.ui.statusLabel.setStyleSheet("color: green;")
```

---

## Colab vs Desktop: When to Use Each

### Use Colab (ipywidgets) When:

✅ **Prototyping** - Quick concept validation
✅ **Data exploration** - Interactive analysis in notebooks
✅ **Sharing with non-technical users** - Just share a link
✅ **Teaching** - Students don't need installations
✅ **Collaboration** - Multiple people working together
✅ **Cloud computing** - Need GPU or large datasets

**Limitations:**
- Requires internet
- Limited to browser
- Can't access local files easily
- Performance depends on server

---

### Use Desktop (PySide6) When:

✅ **Production applications** - Stable, professional tools
✅ **Offline use** - No internet required
✅ **Local file access** - Direct filesystem integration
✅ **Performance critical** - Native speed
✅ **Distribution** - Package as standalone .exe
✅ **Professional appearance** - Native OS look and feel
✅ **Advanced features** - Menus, toolbars, multi-window

**Limitations:**
- Requires installation
- More complex deployment
- Platform-specific considerations

---

### Workflow Recommendation

**1. Prototype in Colab**
- Quick iterations
- Test concepts
- Validate with users
- Refine requirements

**2. Transition to Desktop**
- Design UI in Qt Designer
- Implement core logic (can reuse from Colab!)
- Add desktop-specific features
- Package for distribution

---

## Complete Example: Integrated Application

Let's build a complete application following best practices.

### Project: Grade Calculator

**Structure:**
```
grade_calculator/
├── main.py
├── mainwindow.ui
├── logic.py
├── requirements.txt
└── README.md
```

**logic.py:**
```python
"""Business logic for grade calculations."""

def calculate_letter_grade(percentage):
    """
    Convert percentage to letter grade.

    Args:
        percentage: Numeric grade (0-100)

    Returns:
        Letter grade (A, B, C, D, F)

    Raises:
        ValueError: If percentage is outside 0-100
    """
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")

    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def calculate_weighted_average(grades, weights):
    """
    Calculate weighted average of grades.

    Args:
        grades: List of numeric grades
        weights: List of weights (must sum to 1.0)

    Returns:
        Weighted average

    Raises:
        ValueError: If inputs are invalid
    """
    if len(grades) != len(weights):
        raise ValueError("Grades and weights must have same length")

    if not all(0 <= g <= 100 for g in grades):
        raise ValueError("All grades must be between 0 and 100")

    if not abs(sum(weights) - 1.0) < 0.01:  # Allow small floating point error
        raise ValueError("Weights must sum to 1.0")

    weighted_sum = sum(g * w for g, w in zip(grades, weights))
    return weighted_sum

def get_grade_stats(grades):
    """
    Calculate statistics for a list of grades.

    Args:
        grades: List of numeric grades

    Returns:
        Dictionary with mean, median, min, max
    """
    if not grades:
        raise ValueError("Cannot calculate stats for empty list")

    return {
        'mean': sum(grades) / len(grades),
        'median': sorted(grades)[len(grades) // 2],
        'min': min(grades),
        'max': max(grades),
        'count': len(grades)
    }
```

**main.py:**
```python
"""Grade Calculator - Desktop Application"""

import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from logic import (
    calculate_letter_grade,
    calculate_weighted_average,
    get_grade_stats
)

class GradeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        ui_file = Path(__file__).parent / "mainwindow.ui"
        file = QFile(str(ui_file))
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(file)  # Load without parent
        file.close()

        self.setCentralWidget(self.ui)
        self.setWindowTitle("Grade Calculator")

        # Connect signals
        self.ui.calculateButton.clicked.connect(self.calculate_grade)
        self.ui.percentageInput.valueChanged.connect(self.validate_input)

        # Initialize
        self.validate_input()

    def validate_input(self):
        """Enable/disable button based on input validity"""
        percentage = self.ui.percentageInput.value()

        if 0 <= percentage <= 100:
            self.ui.calculateButton.setEnabled(True)
            self.ui.statusLabel.setText("")
        else:
            self.ui.calculateButton.setEnabled(False)
            self.ui.statusLabel.setText("⚠️  Enter a valid percentage (0-100)")

    def calculate_grade(self):
        """Handle calculate button click"""
        try:
            percentage = self.ui.percentageInput.value()

            # Use business logic
            letter = calculate_letter_grade(percentage)

            # Update UI
            self.ui.letterGradeLabel.setText(f"Letter Grade: {letter}")

            # Determine color
            if letter in ('A', 'B'):
                color = "green"
            elif letter == 'C':
                color = "orange"
            else:
                color = "red"

            self.ui.letterGradeLabel.setStyleSheet(f"color: {color}; font-size: 18pt; font-weight: bold;")
            self.ui.statusLabel.setText("✓ Calculated successfully")
            self.ui.statusLabel.setStyleSheet("color: green;")

        except ValueError as e:
            # Show error
            self.ui.statusLabel.setText(f"❌ Error: {e}")
            self.ui.statusLabel.setStyleSheet("color: red;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GradeCalculator()
    window.show()
    sys.exit(app.exec())
```

**requirements.txt:**
```
PySide6>=6.5.0
```

**README.md:**
```markdown
# Grade Calculator

A desktop application for calculating letter grades.

## Features

- Convert percentage to letter grade
- Visual feedback with color coding
- Input validation

## Setup

1. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run

```bash
python main.py
```

## Testing

```bash
python -m pytest tests/
```
```

---

## Exercise 1: Refactor for Separation

**Task:** Take this poorly organized code and refactor it:

```python
# Before: Everything in one file, mixed concerns
class Calculator(QMainWindow):
    def on_calculate(self):
        x = self.ui.input1.value()
        y = self.ui.input2.value()

        # Complex math mixed with UI
        if x > y:
            result = (x**2 + y**2) ** 0.5
        else:
            result = (x + y) / 2

        self.ui.result.setText(str(result))
```

**Your task:**
1. Create a separate `calculations.py` with the math logic
2. Add proper docstrings
3. Add error handling
4. Keep only UI concerns in the main file

---

## Exercise 2: Add Comprehensive Validation

**Task:** Create a registration form with:
- Name (required, min 2 characters)
- Email (required, must contain @ and .)
- Age (required, 13-120)
- Password (required, min 8 characters)
- Confirm Password (must match)

Implement:
- Real-time validation with visual feedback
- Submit button disabled until all valid
- Clear error messages

---

## Exercise 3: Error Handling

**Task:** Create a file loader with robust error handling:
- Handle file not found
- Handle permission errors
- Handle corrupted files
- Handle unsupported formats
- Provide clear user feedback for each case

---

## Exercise 4: Complete Project

**Task:** Build a complete application following best practices:

**Requirements:**
- Separate business logic file
- Proper project structure
- Input validation
- Error handling
- requirements.txt
- README.md with setup instructions
- .gitignore

**Suggested Projects:**
- BMI calculator with history
- Unit converter with favorites
- Simple todo list with persistence
- Data file analyzer

---

## Deployment Considerations

### Packaging Python Desktop Apps

**PyInstaller** - Create standalone executables:

```bash
# Install
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed main.py

# With icon
pyinstaller --onefile --windowed --icon=app.ico main.py
```

**Result:** `dist/main.exe` (Windows) or `dist/main` (macOS/Linux)

### Distribution Checklist

- [ ] Test on clean system (without Python installed)
- [ ] Include necessary .ui files and resources
- [ ] Verify all dependencies are bundled
- [ ] Create installer (optional: Inno Setup for Windows, DMG for macOS)
- [ ] Document system requirements
- [ ] Provide installation instructions

---

## Key Takeaways

✅ **Separate UI from business logic** - Test and reuse easily

✅ **Validate input** - Early and often, with clear feedback

✅ **Handle errors gracefully** - Never crash, always inform

✅ **Organize projects** - Clear structure helps maintenance

✅ **Version control .ui files** - They're merge-friendly XML

✅ **Write README** - Future you will thank you

✅ **Choose the right tool**:
   - Colab: Prototyping, teaching, collaboration
   - Desktop: Production, offline, performance

✅ **Use patterns consistently** - Makes code predictable

---

## Final Deliverables for Lab 07

### Deliverable A: Colab Prototype
A working interactive application in Google Colab:
- Minimum 3 different widget types
- Event handling with validation
- Layout using HBox/VBox
- Error handling
- Professional appearance

**Submit:** Link to Colab notebook

---

### Deliverable B: Desktop Application
A PySide6 desktop application:
- UI designed in Qt Designer (.ui file)
- Python code loading .ui
- Signal/slot connections working
- Same validation logic as Colab version
- Separated business logic
- Complete project structure

**Submit:** GitHub repository with:
- Source code
- .ui file
- requirements.txt
- README.md with setup instructions

---

## Grading Rubric

### Colab Prototype (50 points)
- Functionality (20 pts): All features work correctly
- Validation (10 pts): Input validated with feedback
- Layout (10 pts): Professional organization
- Error Handling (10 pts): Graceful error handling

### Desktop Application (50 points)
- UI Design (15 pts): Well-designed in Qt Designer
- Functionality (15 pts): All features work correctly
- Code Quality (10 pts): Separated concerns, clean code
- Project Organization (10 pts): Proper structure, documentation

---

## Beyond This Lab

### Next Steps in GUI Development

**Advanced Qt Topics:**
- Model/View architecture for data
- Custom widgets
- Multi-window applications
- Threading for long operations
- Database integration
- Styling with QSS (Qt Style Sheets)

**Other Frameworks:**
- **Tkinter** - Python's built-in GUI (simpler but less powerful)
- **Kivy** - Cross-platform, mobile-friendly
- **PyQt** - Similar to PySide6 (different license)
- **wxPython** - Native look on all platforms

**Web-Based Alternatives:**
- **Streamlit** - Data apps in pure Python
- **Dash** - Interactive dashboards
- **Flask/Django** - Full web frameworks

---

## Conclusion

You've learned the complete journey from web-based prototyping to professional desktop applications:

1. **Module 1**: Widget basics and event handling in Colab
2. **Module 2**: Professional layout and UX principles
3. **Module 3**: Qt Designer and desktop development
4. **Module 4**: Integration and best practices

**You can now:**
- ✅ Build interactive UIs in multiple environments
- ✅ Apply event-driven programming patterns
- ✅ Design professional desktop applications
- ✅ Separate concerns for maintainable code
- ✅ Validate input and handle errors gracefully
- ✅ Choose the right tool for the job

**Congratulations on completing Lab 07!**

---

## Additional Resources

### Best Practices
- [PEP 8 - Python Style Guide](https://pep8.org/)
- [Clean Code Principles](https://clean-code-developer.com/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

### Qt Resources
- [Qt Documentation](https://doc.qt.io/)
- [PySide6 Examples](https://doc.qt.io/qtforpython-6/examples/index.html)
- [Qt Forum](https://forum.qt.io/)

### Python GUI Comparisons
- [Python GUI Frameworks Comparison](https://realpython.com/python-gui-frameworks/)

---

**Lab 07 Complete!** You're now equipped to build professional interactive applications.
