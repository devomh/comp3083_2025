# GUI Builder Lesson Options (Python, 3 hours)

Here are three solid outline options tailored for a 3-hour session, Python-first, with Google Colab and VS Code in mind. Each covers: standard widgets, a GUI designer intro, viewing generated code, and supplemental files.

## Option 1: PySide6 + Qt Designer (VS Code‑centric)

- 0:00–0:15 Motivation + Widgets
  - Why GUIs vs console; event-driven basics.
  - Standard widgets: labels, buttons, line edits, text edits, checkboxes, radio buttons, combo boxes, list/table views, sliders/progress, spin boxes, date/time, containers (tabs, stacked), dialogs, layouts.
- 0:15–0:35 Tour of Qt Designer
  - Create a MainWindow; add widgets; set object names; apply vertical/horizontal/grid layouts.
  - Save as `mainwindow.ui`; discuss `.ui` XML role.
- 0:35–1:00 Generated Code: Two Approaches
  - Approach A: Compile UI to Python with `pyside6-uic` → `ui_mainwindow.py`. Inspect `Ui_MainWindow`, `setupUi`, “don’t edit generated file” pattern.
  - Approach B: Load `.ui` at runtime to avoid generated code churn. Note trade-offs.
- 1:00–1:35 Wire Events in Your Code
  - Create `main.py`; subclass `QMainWindow`; call `Ui_MainWindow.setupUi(self)`.
  - Connect signals to slots (`clicked.connect(self.on_convert)`); keep logic separate from generated UI.
- 1:35–2:35 Guided Build: Unit Converter App
  - Inputs: `QLineEdit`, `QComboBox`, `QPushButton`, `QLabel` result.
  - Add icons via a `.qrc` (resources file) and compile with `pyside6-rcc` → `resources_rc.py`.
  - Run, test, iterate; show validation and disabled/enabled states.
- 2:35–3:00 Wrap‑Up
  - Review: widgets, designer workflow, generated files (`.ui`, compiled `*_ui.py`, `*_rc.py`), separation of concerns.
  - Quick challenge: add a “Reset” action and a status bar message.

Notes
- Supplemental files: `.ui` (UI spec), `.qrc` (resources), generated `*_ui.py` and `*_rc.py`.
- Emphasize: never hand-edit `*_ui.py`; keep logic in your app code.

Commands (for student machines)

```bash
# Create venv
python -m venv .venv
# Activate
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Install
pip install pyside6

# Launch Designer
pyside6-designer

# Compile UI
pyside6-uic mainwindow.ui -o ui_mainwindow.py

# Compile resources
pyside6-rcc resources.qrc -o resources_rc.py
```

## Option 2: Colab Widgets + VS Code Designer Hand‑Off

- 0:00–0:35 Widgets in Colab (no desktop GUI)
  - Use `ipywidgets`: `Button`, `Text`, `Dropdown`, `IntSlider`, `Checkbox`, `Output`.
  - Event handling: `.on_click`, trait changes, basic validation.
  - Focus: what widgets are and how events flow.
- 0:35–0:55 Layout + UX Concepts
  - Grouping, alignment, affordances, feedback; map these to desktop widget equivalents.
- 0:55–1:05 Transition: Why a GUI Designer
  - Faster iteration; layout constraints; auto-generated code and how to work around it.
- 1:05–1:35 Qt Designer Demo (instructor)
  - Build same UI designed in Colab but as a desktop app; save `mainwindow.ui`.
- 1:35–2:25 Student Practice in VS Code
  - Teams convert their Colab prototype into PySide6 desktop UI using Designer.
  - Load or compile `.ui`; connect signals; test logic.
- 2:25–3:00 Debrief
  - Compare notebook vs desktop flow; pros/cons.
  - Inspect generated files; discuss versioning of `.ui` and images.

Notes
- Colab portion covers widgets and events where students already work.
- VS Code portion introduces designer, code structure, and runtime.

## Option 3: Tkinter Focus + Designer Alternative (PAGE)

- 0:00–0:25 Tkinter Basics
  - Widgets: `Label`, `Button`, `Entry`, `Text`, `Checkbutton`, `Radiobutton`, `Listbox`, `ttk.Combobox`, `Scale`, `Progressbar`, `Spinbox`, `Treeview`, `Notebook`, dialogs.
  - Geometry managers: `pack`, `grid`; event binding `.bind`, command callbacks.
- 0:25–0:50 Build by Hand
  - Small app (Tip Calculator) with validation and layout; show modularization.
- 0:50–1:10 Why Use a Designer
  - Speed, consistency, but generated code caveats; separation between UI and logic.
- 1:10–1:50 Designer Demo (PAGE)
  - Create UI visually; export Python code.
  - Inspect generated code: highlight init code, widget references, event stubs.
- 1:50–2:40 Student Practice
  - Extend the generated UI with event logic in a separate module; avoid editing generated file.
- 2:40–3:00 Compare + Next Steps
  - Tkinter ecosystem vs Qt; portability; choosing tools.

Notes
- PAGE is a community tool for Tkinter; availability/setup vary by OS. Have a backup plan (hand-coding) if installation hiccups arise.
- Supplemental artifacts typically just the generated `.py` plus assets; fewer formal resource files than Qt.

## Pre‑Class Setup

- VS Code: Python extension; ensure `python`/`pip` on PATH.
- For Qt route: install `pyside6` on student machines; verify `pyside6-designer` runs; pre-create a sample `mainwindow.ui`.
- Optional assets: a small icon set to showcase `.qrc` resources.
- Colab: prepare a notebook with `ipywidgets` examples and starter cells.

## Suggested Mini‑Projects

- Unit Converter (length/temperature): dropdowns, input, output label, error handling.
- To‑Do List: `QListWidget`/`Treeview`, add/remove, persistence optional.
- Tip Calculator: inputs, radio buttons/slider for tip %, formatted output.

## Assessment Ideas

- Formative: checkpoint where a button triggers a valid conversion and updates a label.
- Summative (exit ticket): add an input validator and disabled state until valid.

## Why Choose Which Option

- Option 1: Best balance of professional tooling and approachability; clean generated artifacts to inspect.
- Option 2: Leverages Colab familiarity for concepts, then applies them in a desktop designer.
- Option 3: If curriculum emphasizes Tkinter, shows both code-first and designer-first paths.

---

If you pick one, I can draft a slide outline, a VS Code starter repo (`main.py`, `mainwindow.ui`, `resources.qrc`), and a Colab notebook with widget labs.

