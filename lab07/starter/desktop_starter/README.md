# Lab 07 - Desktop Application Starter

This is a starter template for building your Lab 07 desktop application using PySide6 and Qt Designer.

## Prerequisites

- Python 3.10 or higher
- pip package manager

## Setup

### 1. Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

Test that Qt Designer is available:

**macOS/Linux:**
```bash
pyside6-designer
```

**Windows:**
```bash
.venv\Scripts\pyside6-designer.exe
```

If Qt Designer opens successfully, you're ready to go!

## Development Workflow

### Step 1: Design UI in Qt Designer

1. Launch Qt Designer:
   ```bash
   pyside6-designer
   ```

2. Open `mainwindow.ui`

3. Add your widgets:
   - Drag widgets from the Widget Box (left side)
   - Set object names in Property Editor (right side)
   - Configure properties (text, min/max values, etc.)

4. Apply layouts:
   - Select widgets to layout together
   - Right-click → Lay Out → choose layout type
   - Or use toolbar buttons

5. Save your changes

### Step 2: Connect UI to Python Code

1. Open `main.py` in your editor

2. Find widgets by their object names:
   ```python
   self.my_widget = self.ui.findChild(WidgetType, 'objectName')
   ```

3. Connect signals to handlers:
   ```python
   self.my_button.clicked.connect(self.on_button_click)
   ```

4. Implement event handlers:
   ```python
   def on_button_click(self):
       # Your logic here
       pass
   ```

### Step 3: Run Your Application

```bash
python main.py
```

## File Structure

```
desktop_starter/
├── main.py             # Application code (edit this)
├── mainwindow.ui       # UI definition (edit in Qt Designer)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Common Widget Object Names

Use descriptive object names in Qt Designer:

**Good examples:**
- `tempInput` - temperature input spinbox
- `convertButton` - conversion button
- `resultLabel` - result display label
- `unitCombo` - unit selection dropdown

**Bad examples:**
- `doubleSpinBox` - not descriptive
- `pushButton_1` - numbered default name
- `widget` - too generic

## Debugging Tips

### UI File Not Found

If you get a `FileNotFoundError`:
- Verify `mainwindow.ui` is in the same directory as `main.py`
- Check the file path in code

### Widget Not Found

If `findChild` returns `None`:
- Verify the object name in Qt Designer matches your code exactly
- Object names are case-sensitive!
- Check you're using the correct widget type

### Changes Don't Appear

If UI changes don't show:
- Save the .ui file in Qt Designer
- Restart your Python application
- If using compiled approach, re-compile the UI

## Two Approaches

### Approach 1: Runtime Loading (Default)

**Pros:**
- Changes appear immediately
- Simple to understand
- No build step

**Cons:**
- Slightly more verbose
- No IDE autocomplete for widgets

### Approach 2: Compiled UI

To switch to compiled approach:

1. Compile the UI file:
   ```bash
   pyside6-uic mainwindow.ui -o ui_mainwindow.py
   ```

2. In `main.py`:
   - Uncomment the `CompiledMainWindow` class
   - Uncomment the import
   - Update `main()` to use `CompiledMainWindow`

**Pros:**
- IDE autocomplete for widgets
- Cleaner widget access

**Cons:**
- Must recompile after UI changes
- Extra build step

**Never edit `ui_mainwindow.py`** - it's generated code!

## Getting Help

- Review Module 3 for detailed Qt Designer instructions
- Check PySide6 documentation: https://doc.qt.io/qtforpython-6/
- Ask your instructor or teaching assistant

## Next Steps

1. Design your UI in Qt Designer
2. Set appropriate object names
3. Implement your logic in `main.py`
4. Test thoroughly
5. Submit as Deliverable B

Good luck!
