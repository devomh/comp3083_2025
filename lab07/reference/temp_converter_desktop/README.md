# Temperature Converter - Desktop Reference Implementation

This is a complete, working reference implementation of a temperature converter desktop application. Use this as a guide for your own Lab 07 desktop application.

## Features

- ✅ Convert between Celsius, Fahrenheit, and Kelvin
- ✅ Input validation (prevents converting to the same unit)
- ✅ Error handling (absolute zero, invalid inputs)
- ✅ Professional UI designed in Qt Designer
- ✅ Separated business logic from UI code
- ✅ Visual feedback with colors and status messages
- ✅ Reset functionality

## Project Structure

```
temp_converter_desktop/
├── main.py             # Application entry point and UI logic
├── logic.py            # Business logic (temperature conversion)
├── mainwindow.ui       # UI definition from Qt Designer
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Key Design Patterns

### Separation of Concerns

**Business logic** (`logic.py`) is completely separate from UI code (`main.py`):
- `logic.py` can be tested without the UI
- Conversion logic can be reused in other contexts (CLI, web, etc.)
- Changes to UI don't affect logic and vice versa

### UI Design

The UI was designed in Qt Designer (`mainwindow.ui`):
- Visual layout with vertical and horizontal boxes
- Proper spacing and alignment
- Descriptive object names for easy code access
- Professional appearance

### Error Handling

Three levels of error handling:
1. **Prevention**: Validation disables invalid operations
2. **User feedback**: Clear error messages in UI
3. **Robustness**: Try/except blocks for unexpected errors

### Validation

Real-time validation:
- Convert button disabled when from/to units are the same
- Status label updates to guide user
- Visual feedback with colors (green=success, red=error, orange=warning)

## Setup and Run

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

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

### Run the Application

```bash
python main.py
```

### Test the Business Logic

The `logic.py` file includes self-tests:

```bash
python logic.py
```

Expected output:
```
Testing temperature conversions...
✓ 0°C = 32°F
✓ 100°C = 212°F
✓ -273.15°C = 0K
✓ 20°C = 68°F

All tests passed!
```

## Using Qt Designer

To modify the UI:

1. Launch Qt Designer:
   ```bash
   pyside6-designer
   ```

2. Open `mainwindow.ui`

3. Make your changes

4. Save

5. Restart the application to see changes

## Code Walkthrough

### main.py

**Loading the UI:**
```python
ui_file = Path(__file__).parent / "mainwindow.ui"
file = QFile(str(ui_file))
file.open(QFile.ReadOnly)
loader = QUiLoader()
self.ui = loader.load(file)  # Load without parent
```

**Accessing widgets by objectName:**
```python
self.temp_input = self.ui.findChild(QDoubleSpinBox, 'tempInput')
self.from_combo = self.ui.findChild(QComboBox, 'fromUnitCombo')
```

**Connecting signals to slots:**
```python
self.convert_btn.clicked.connect(self.on_convert)
self.from_combo.currentTextChanged.connect(self.validate_units)
```

**Using separated business logic:**
```python
from logic import convert_temperature

# In event handler:
result = convert_temperature(value, from_unit, to_unit)
```

### logic.py

**Pure functions with clear interfaces:**
```python
def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature between units.

    Args:
        value: Temperature value
        from_unit: Source unit
        to_unit: Target unit

    Returns:
        Converted temperature

    Raises:
        ValueError: If inputs are invalid
    """
    # Validation
    # Conversion logic
    # Return result
```

## Learning Points

### 1. Widget Access Pattern

```python
# Bad - hard-coded references
self.temp_input = some_spinbox

# Good - find by objectName
self.temp_input = self.ui.findChild(QDoubleSpinBox, 'tempInput')
```

### 2. Signal/Slot Pattern

```python
# Connect signal to slot method
self.button.clicked.connect(self.on_button_click)

# Slot method
def on_button_click(self):
    # Handle the click
    pass
```

### 3. Validation Pattern

```python
def validate_input(self):
    """Check if inputs are valid"""
    if self.is_valid():
        self.action_button.setEnabled(True)
        self.status.setText("Ready")
    else:
        self.action_button.setEnabled(False)
        self.status.setText("Invalid input")
```

### 4. Error Display Pattern

```python
try:
    result = risky_operation()
    self.result_label.setText(f"Success: {result}")
    self.result_label.setStyleSheet("color: green;")
except ValueError as e:
    self.result_label.setText(f"Error: {e}")
    self.result_label.setStyleSheet("color: red;")
```

## Extending This Example

### Add New Features

1. **History**: Show recent conversions
   - Add QListWidget to UI
   - Store conversions in a list
   - Display in the widget

2. **Favorites**: Save common conversions
   - Add Save/Load buttons
   - Use JSON for persistence
   - Populate from saved data

3. **Copy Result**: Copy to clipboard
   - Add "Copy" button
   - Use `QApplication.clipboard()`

### Apply to Your Project

Use this structure for your own Lab 07 application:

1. Design UI in Qt Designer
2. Create separate logic module
3. Use same loading pattern
4. Apply same validation approach
5. Follow same error handling
6. Maintain same project structure

## Comparison with Colab Version

The Colab notebook (`temp_converter_colab.ipynb`) implements the same functionality but uses ipywidgets instead of PySide6:

| Feature | Colab | Desktop |
|---------|-------|---------|
| Widgets | ipywidgets | PySide6 |
| Layout | HBox/VBox | Qt Layouts |
| Events | .on_click() | .clicked.connect() |
| Output | Output widget | QLabel |
| Design Tool | Code only | Qt Designer |
| Environment | Web browser | Native OS |

**Same concepts, different implementation!**

## Resources

- [PySide6 Documentation](https://doc.qt.io/qtforpython-6/)
- [Qt Designer Manual](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [Qt Widget Gallery](https://doc.qt.io/qt-6/gallery.html)

## Questions?

Review:
- Module 3: Qt Designer and Desktop Apps
- Module 4: Integration and Best Practices

This reference implementation demonstrates all the concepts taught in Lab 07.

---

**Use this as a guide, not a copy-paste!** Understanding the patterns and applying them to your own project is the goal.
