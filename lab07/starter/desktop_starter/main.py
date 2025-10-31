"""
Lab 07 - Desktop Application Starter Template

This template demonstrates both approaches to loading Qt Designer .ui files:
1. Runtime loading (recommended for learning)
2. Compiled approach (uncomment to use)

Choose one approach and implement your application logic.
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QComboBox, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# ===== APPROACH 1: Runtime Loading (Default) =====

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file at runtime
        ui_file = Path(__file__).parent / "mainwindow.ui"
        file = QFile(str(ui_file))
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(file)  # Load without parent
        file.close()

        self.setCentralWidget(self.ui)
        self.setWindowTitle("My Application")

        # Access widgets by objectName (set in Qt Designer)
        # Examples - replace with your actual widget names:
        # self.input_widget = self.ui.findChild(QDoubleSpinBox, 'inputSpinBox')
        # self.dropdown = self.ui.findChild(QComboBox, 'optionCombo')
        # self.action_button = self.ui.findChild(QPushButton, 'actionButton')
        # self.result_label = self.ui.findChild(QLabel, 'resultLabel')

        # Connect signals to slots
        # Example:
        # self.action_button.clicked.connect(self.on_action_clicked)

        # Initial validation
        # self.validate_input()

    def on_action_clicked(self):
        """
        Handle action button click.

        TODO: Implement your logic here:
        1. Get values from input widgets
        2. Validate inputs
        3. Perform calculations
        4. Update output widgets
        5. Handle errors gracefully
        """
        try:
            # Example - replace with your logic:
            # value = self.input_widget.value()
            # option = self.dropdown.currentText()

            # Validation
            # if value < 0:
            #     self.result_label.setText("✗ Invalid input")
            #     return

            # Calculation
            # result = value * 2  # Replace with actual logic

            # Display result
            # self.result_label.setText(f"Result: {result:.2f}")

            pass

        except Exception as e:
            # Handle errors gracefully
            # self.result_label.setText(f"✗ Error: {e}")
            print(f"Error: {e}")

    def validate_input(self):
        """
        Validate input and enable/disable action button.

        TODO: Add validation logic
        """
        # Example:
        # value = self.input_widget.value()
        # if value >= 0:
        #     self.action_button.setEnabled(True)
        # else:
        #     self.action_button.setEnabled(False)
        pass


# ===== APPROACH 2: Compiled UI (Alternative) =====
#
# To use this approach:
# 1. Compile your .ui file:
#    pyside6-uic mainwindow.ui -o ui_mainwindow.py
# 2. Uncomment the import and class below
# 3. Comment out the runtime loading class above
# 4. Update main() to use CompiledMainWindow

# from ui_mainwindow import Ui_MainWindow
#
# class CompiledMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.setWindowTitle("My Application")
#
#         # Widgets are directly accessible as self.ui.widgetName
#         # Connect signals
#         # self.ui.actionButton.clicked.connect(self.on_action_clicked)
#
#         # Initial validation
#         # self.validate_input()
#
#     def on_action_clicked(self):
#         """Handle button click"""
#         try:
#             # Get values
#             # value = self.ui.inputSpinBox.value()
#             # option = self.ui.optionCombo.currentText()
#
#             # Process and display
#             # result = value * 2
#             # self.ui.resultLabel.setText(f"Result: {result:.2f}")
#
#             pass
#         except Exception as e:
#             # self.ui.resultLabel.setText(f"Error: {e}")
#             print(f"Error: {e}")
#
#     def validate_input(self):
#         """Validate input"""
#         pass


# ===== Application Entry Point =====

def main():
    """Start the application"""
    app = QApplication(sys.argv)

    # Use runtime loading (default)
    window = MainWindow()

    # Or use compiled approach (uncomment if using Approach 2)
    # window = CompiledMainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
