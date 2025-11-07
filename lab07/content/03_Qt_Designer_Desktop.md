# Module 3: Qt Designer and Desktop Apps

## From Browser to Desktop

**Learning Objectives:**
- Understand why GUI designers accelerate development
- Use Qt Designer to create desktop UIs visually
- Load .ui files in PySide6 applications
- Connect Qt signals to Python handlers (slots)
- Convert a Colab prototype to a desktop application

---

## Why GUI Designers?

### The Code-First Challenge

Building GUIs in code is powerful but slow:

```python
# Creating a simple form in code takes many lines
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton

app = QApplication([])
window = QWidget()

# Layout
main_layout = QVBoxLayout()

# Name row
name_layout = QHBoxLayout()
name_label = QLabel("Name:")
name_input = QLineEdit()
name_layout.addWidget(name_label)
name_layout.addWidget(name_input)
main_layout.addLayout(name_layout)

# Email row
email_layout = QHBoxLayout()
email_label = QLabel("Email:")
email_input = QLineEdit()
email_layout.addWidget(email_label)
email_layout.addWidget(email_input)
main_layout.addLayout(email_layout)

# Submit button
submit_btn = QPushButton("Submit")
main_layout.addWidget(submit_btn)

window.setLayout(main_layout)
window.show()
app.exec()
```

**Problems:**
- Verbose and repetitive
- Hard to visualize the result
- Time-consuming to iterate
- Mixing UI structure with logic

### The Designer Solution

**GUI Designers** let you:
1. **Build visually** - drag and drop widgets
2. **See immediately** - preview as you design
3. **Iterate quickly** - adjust layouts in seconds
4. **Separate concerns** - UI definition separate from logic
5. **Maintain consistency** - easier to apply design standards

**Popular GUI Designers:**
- **Qt Designer** - for Qt/PySide6 (what we'll use)
- **Glade** - for GTK
- **Visual Studio Designer** - for .NET
- **Interface Builder** - for macOS/iOS

---

## Qt Designer Overview

### Installation and Launch

Qt Designer comes with PySide6:

```bash
# Set up environment
python -m venv .venv

# Activate environment
# source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install PySide6
pip install pyside6

# Launch Qt Designer
pyside6-designer

```

### Designer Interface

When you launch Qt Designer, you'll see:

1. **Widget Box** (left) - all available widgets
2. **Form Editor** (center) - your UI canvas
3. **Object Inspector** (right top) - widget hierarchy
4. **Property Editor** (right bottom) - widget properties

---

## Creating Your First Desktop UI

### Step 1: New Form

1. File → New → Main Window
2. You get a blank window with menu bar

### Step 2: Add Widgets

From the Widget Box, drag widgets onto the form:

**Common Widgets:**
- `QLabel` - display text
- `QLineEdit` - single-line text input
- `QPushButton` - button
- `QComboBox` - dropdown (like Dropdown in ipywidgets)
- `QSpinBox` - integer input (like IntText)
- `QDoubleSpinBox` - float input (like FloatText)
- `QCheckBox` - checkbox
- `QSlider` - slider
- `QTextEdit` - multi-line text

### Step 3: Set Object Names

**CRITICAL**: Object names are how you access widgets in code.

1. Click a widget
2. In Property Editor, find `objectName`
3. Give it a meaningful name (e.g., `tempInput`, `convertButton`)

**Naming Convention:**
- Use camelCase: `tempInput` not `temp_input`
- Be descriptive: `convertButton` not `btn1`
- Match purpose: `resultLabel`, `emailInput`

### Step 4: Set Properties

Configure widget properties:

- `text` - displayed text (labels, buttons)
- `placeholderText` - hint text for inputs
- `minimum` / `maximum` - range for spinboxes/sliders
- `value` - default value

### Step 5: Apply Layouts

**Without layout, widgets won't resize properly!**

1. Arrange widgets roughly where you want them
2. Select widgets that should be in a row
3. Toolbar → "Lay Out Horizontally" (or Ctrl+1)
4. Select widgets that should be in a column
5. Toolbar → "Lay Out Vertically" (or Ctrl+2)
6. Right-click the form background → "Lay Out" → "Lay Out Vertically"

**Layout Types:**
- Horizontal Layout - like HBox
- Vertical Layout - like VBox
- Grid Layout - like GridBox
- Form Layout - label-input pairs

### Step 6: Preview

Form → Preview (Ctrl+R) to see how it looks

### Step 7: Save

File → Save As → `mainwindow.ui`

---

## Tutorial: Temperature Converter Desktop App

Let's recreate the temperature converter from Module 1 as a desktop app.

### Part A: Design the UI

**Create in Qt Designer:**

1. **New Main Window**

2. **Add widgets** (from Widget Box to central widget):
   - QLabel: "Temperature Converter" (top)
   - QDoubleSpinBox: for temperature value
   - QComboBox: for input unit
   - QLabel: "to" (small)
   - QComboBox: for output unit
   - QPushButton: "Convert"
   - QLabel: for result display

3. **Set object names**:
   - `tempInput` (QDoubleSpinBox)
   - `fromUnitCombo` (QComboBox #1)
   - `toUnitCombo` (QComboBox #2)
   - `convertButton` (QPushButton)
   - `resultLabel` (QLabel)

4. **Configure properties**:

   `tempInput`:
   - minimum: -1000
   - maximum: 1000
   - decimals: 2
   - value: 0

   `fromUnitCombo`:
   - items: "Celsius", "Fahrenheit", "Kelvin"

   `toUnitCombo`:
   - items: "Celsius", "Fahrenheit", "Kelvin"
   - currentIndex: 1 (default to Fahrenheit)

   `convertButton`:
   - text: "Convert"

   `resultLabel`:
   - text: "Result will appear here"
   - alignment: AlignCenter

5. **Apply layouts**:
   - Select tempInput and fromUnitCombo → Lay Out Horizontally
   - Select toUnitCombo and the "to" label → Lay Out Horizontally
   - Select all rows vertically → Lay Out Vertically
   - Right-click central widget → Lay Out → Lay Out Vertically

6. **Save** as `temp_converter.ui`

---

### Part B: Load UI in Python

Two approaches to using .ui files:

#### Approach 1: Runtime Loading (Recommended for Learning)

```python
# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from pathlib import Path

class TempConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        ui_file = Path(__file__).parent / "temp_converter.ui"
        file = QFile(str(ui_file))
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(file)  # Load without parent
        file.close()

        self.setCentralWidget(self.ui)

        # Access widgets by objectName
        # Note: findChild returns the widget or None
        self.temp_input = self.ui.findChild(QDoubleSpinBox, 'tempInput')
        self.from_combo = self.ui.findChild(QComboBox, 'fromUnitCombo')
        self.to_combo = self.ui.findChild(QComboBox, 'toUnitCombo')
        self.convert_btn = self.ui.findChild(QPushButton, 'convertButton')
        self.result_label = self.ui.findChild(QLabel, 'resultLabel')

        # Connect signals to slots
        self.convert_btn.clicked.connect(self.convert_temperature)

        self.setWindowTitle("Temperature Converter")

    def convert_temperature(self):
        """Handle the convert button click"""
        try:
            value = self.temp_input.value()
            from_unit = self.from_combo.currentText()
            to_unit = self.to_combo.currentText()

            # Convert to Celsius first
            if from_unit == "Celsius":
                celsius = value
            elif from_unit == "Fahrenheit":
                celsius = (value - 32) * 5/9
            else:  # Kelvin
                celsius = value - 273.15

            # Convert from Celsius to target
            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = (celsius * 9/5) + 32
            else:  # Kelvin
                result = celsius + 273.15

            self.result_label.setText(f"{result:.2f}° {to_unit}")

        except Exception as e:
            self.result_label.setText(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TempConverter()
    window.show()
    sys.exit(app.exec())
```

**Run it:**
```bash
python main.py
```

---

#### Approach 2: Compiled UI

Compile .ui to Python first:

```bash
pyside6-uic temp_converter.ui -o ui_temp_converter.py
```

This creates `ui_temp_converter.py` with a `Ui_MainWindow` class.

**IMPORTANT: Never edit `ui_temp_converter.py`!** It's generated code.

```python
# main.py (compiled approach)
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_temp_converter import Ui_MainWindow

class TempConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up UI from compiled code
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Widgets are directly accessible as self.ui.widgetName
        # Connect signals
        self.ui.convertButton.clicked.connect(self.convert_temperature)

    def convert_temperature(self):
        """Handle the convert button click"""
        try:
            value = self.ui.tempInput.value()
            from_unit = self.ui.fromUnitCombo.currentText()
            to_unit = self.ui.toUnitCombo.currentText()

            # Conversion logic (same as above)
            if from_unit == "Celsius":
                celsius = value
            elif from_unit == "Fahrenheit":
                celsius = (value - 32) * 5/9
            else:
                celsius = value - 273.15

            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = (celsius * 9/5) + 32
            else:
                result = celsius + 273.15

            self.ui.resultLabel.setText(f"{result:.2f}° {to_unit}")

        except Exception as e:
            self.ui.resultLabel.setText(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TempConverter()
    window.show()
    sys.exit(app.exec())
```

---

### Approach Comparison

| Aspect | Runtime Loading | Compiled |
|--------|----------------|----------|
| Setup | Import QUiLoader | Run pyside6-uic |
| Access widgets | `findChild(Type, 'name')` | `self.ui.widgetName` |
| Changes | Just save .ui | Re-compile after changes |
| Pros | See changes instantly | Autocomplete in IDE |
| Cons | More verbose | Extra build step |

**Recommendation:** Start with runtime loading for learning. Use compiled for larger projects.

---

## Signal and Slot Connections

### Understanding Signals and Slots

Qt uses a **signal/slot** mechanism for events:

- **Signal**: An event emitted by a widget (e.g., "clicked", "textChanged")
- **Slot**: A function that responds to the signal

**Pattern:**
```python
widget.signal.connect(slot_function)
```

### Common Signals

**QPushButton:**
- `clicked` - button was clicked
- `pressed` - button was pressed down
- `released` - button was released

**QLineEdit / QTextEdit:**
- `textChanged` - text was modified
- `editingFinished` - user finished editing (Enter or focus lost)

**QComboBox:**
- `currentIndexChanged` - selection changed
- `currentTextChanged` - selected text changed

**QSlider / QSpinBox:**
- `valueChanged` - value changed

**QCheckBox:**
- `stateChanged` - checked/unchecked
- `toggled` - boolean state changed

### Connection Examples

```python
# Button click
self.ui.submitButton.clicked.connect(self.on_submit)

# Text change (continuous)
self.ui.searchInput.textChanged.connect(self.on_search)

# Text change (on Enter/focus loss)
self.ui.nameInput.editingFinished.connect(self.validate_name)

# Dropdown selection
self.ui.categoryCombo.currentTextChanged.connect(self.filter_items)

# Slider value
self.ui.volumeSlider.valueChanged.connect(self.update_volume)

# Checkbox toggle
self.ui.agreeCheckbox.toggled.connect(self.toggle_submit_button)
```

### Passing Parameters

Sometimes you need to pass extra data:

```python
# Using lambda
self.ui.deleteButton.clicked.connect(lambda: self.delete_item(item_id))

# Using functools.partial
from functools import partial
self.ui.editButton.clicked.connect(partial(self.edit_item, item_id))
```

---

## Adding Validation

Let's enhance the temperature converter with validation:

```python
def __init__(self):
    # ... (previous init code)

    # Connect for real-time validation
    self.temp_input.valueChanged.connect(self.validate_input)
    self.from_combo.currentTextChanged.connect(self.validate_input)
    self.to_combo.currentTextChanged.connect(self.validate_input)

    # Initial validation
    self.validate_input()

def validate_input(self):
    """Validate input and enable/disable convert button"""
    from_unit = self.from_combo.currentText()
    to_unit = self.to_combo.currentText()

    # Can't convert to the same unit
    if from_unit == to_unit:
        self.convert_btn.setEnabled(False)
        self.result_label.setText("Select different units")
    else:
        self.convert_btn.setEnabled(True)
        self.result_label.setText("Ready to convert")
```

---

## Exercise 1: Design Your Prototype

**Task:** Take your temperature converter (or another prototype) from Module 1 and recreate it in Qt Designer.

**Steps:**
1. Open Qt Designer
2. Create a new Main Window
3. Add appropriate widgets
4. Set object names
5. Configure properties
6. Apply layouts
7. Save as `my_app.ui`

**Deliverable:** A .ui file that can be previewed (Form → Preview)

---

## Exercise 2: Load and Connect

**Task:** Write Python code to load your .ui file and connect one event.

**Requirements:**
- Use runtime loading approach
- Connect at least one button click
- Display a simple result in a label

```python
# Your code here
```

---

## Exercise 3: Add Validation

**Task:** Add input validation to your app:
- Check for invalid inputs
- Disable action button until valid
- Show appropriate error messages

```python
# Your code here
```

---

## Best Practices

### DO:
✅ Use meaningful object names
✅ Apply layouts to everything
✅ Keep business logic in Python, not in Designer
✅ Version control .ui files (they're XML, git-friendly)
✅ Test with Form → Preview frequently

### DON'T:
❌ Edit generated Python files (if using compiled approach)
❌ Mix layout code and business logic
❌ Forget to apply layouts (widgets won't resize)
❌ Use generic names like `pushButton_1`

---

## Project Structure

Organize your desktop project:

```
my_app/
├── .venv/              # Virtual environment
├── main.py             # Application entry point
├── mainwindow.ui       # UI definition
├── requirements.txt    # PySide6
└── README.md          # Setup instructions
```

**requirements.txt:**
```
PySide6>=6.5.0
```

**README.md example:**
```markdown
# My Desktop App

## Setup

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Run

python main.py
```

---

## Troubleshooting

### Issue: Window appears but widgets are not visible
**Cause:** Passing parent to `loader.load()` creates a parenting conflict
**Solution:** Load without a parent parameter
```python
# ❌ Wrong - causes widgets to not display
self.ui = loader.load(file, self)

# ✅ Correct - widgets display properly
self.ui = loader.load(file)
```
After loading without a parent, `setCentralWidget()` will work correctly.

### Issue: Widgets overlap or don't resize
**Cause:** No layout applied
**Solution:** In Designer, right-click form → Lay Out → choose layout

### Issue: Can't find widget with findChild
**Cause:** Wrong objectName
**Solution:** Check objectName in Designer matches code exactly (case-sensitive!)

### Issue: Signal connection doesn't work
**Cause:** Wrong signal name or not connected
**Solution:** Check Qt docs for correct signal name, verify `.connect()` is called

### Issue: Changes in Designer don't appear
**Cause:** Old compiled file (if using compiled approach)
**Solution:** Re-run `pyside6-uic mainwindow.ui -o ui_mainwindow.py`

---

## Comparison: Colab vs Desktop

| Aspect | ipywidgets (Colab) | PySide6 (Desktop) |
|--------|-------------------|-------------------|
| Environment | Web browser | Native OS |
| Design Tool | Code only | Qt Designer visual tool |
| Layout | HBox, VBox | QHBoxLayout, QVBoxLayout |
| Events | .on_click(), .observe() | .clicked.connect() |
| Output | Output widget | QLabel, QTextEdit |
| Deployment | Share notebook link | Package as .exe/.app |
| Speed | Server-dependent | Native performance |

**Same Concepts:**
- Event-driven programming
- Layout hierarchy
- Validation patterns
- Separation of UI and logic

---

## Next Steps

In **Module 4: Integration and Best Practices**, you'll learn:
- Advanced project organization
- Model-View patterns
- Packaging and distribution
- Comparing Colab and Desktop workflows

**Before proceeding:**
- Complete at least Exercises 1-3
- Get comfortable with Qt Designer
- Successfully load and connect a .ui file
- Understand signal/slot pattern

---

## Additional Resources

### Qt Documentation
- [Qt Designer Manual](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [PySide6 Signals & Slots](https://doc.qt.io/qtforpython-6/overviews/signalsandslots.html)
- [Widget Gallery](https://doc.qt.io/qt-6/gallery.html)

### Tutorials
- [PySide6 Tutorial](https://doc.qt.io/qtforpython-6/tutorials/index.html)
- [Python GUIs](https://www.pythonguis.com/)

### Tools
- [Qt Documentation Browser (Zeal)](https://zealdocs.org/)

---

**Module Complete!** You can now design professional desktop UIs and connect them to Python logic. Proceed to Module 4 for integration best practices.
