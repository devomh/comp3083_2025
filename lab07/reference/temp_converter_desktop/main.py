"""
Temperature Converter - Complete Desktop Example

This is a complete, working example demonstrating:
- Loading UI from Qt Designer
- Signal/slot connections
- Input validation
- Error handling
- Separation of business logic
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDoubleSpinBox,
    QComboBox, QPushButton, QLabel
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from logic import convert_temperature


class TempConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file
        ui_file = Path(__file__).parent / "mainwindow.ui"
        file = QFile(str(ui_file))
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(file)  # Load without parent
        file.close()

        self.setCentralWidget(self.ui)
        self.setWindowTitle("Temperature Converter")

        # Access widgets
        self.temp_input = self.ui.findChild(QDoubleSpinBox, 'tempInput')
        self.from_combo = self.ui.findChild(QComboBox, 'fromUnitCombo')
        self.to_combo = self.ui.findChild(QComboBox, 'toUnitCombo')
        self.convert_btn = self.ui.findChild(QPushButton, 'convertButton')
        self.reset_btn = self.ui.findChild(QPushButton, 'resetButton')
        self.result_label = self.ui.findChild(QLabel, 'resultLabel')
        self.status_label = self.ui.findChild(QLabel, 'statusLabel')

        # Connect signals
        self.convert_btn.clicked.connect(self.on_convert)
        self.reset_btn.clicked.connect(self.on_reset)
        self.from_combo.currentTextChanged.connect(self.validate_units)
        self.to_combo.currentTextChanged.connect(self.validate_units)

        # Initial validation
        self.validate_units()

    def validate_units(self):
        """Validate that from and to units are different."""
        from_unit = self.from_combo.currentText()
        to_unit = self.to_combo.currentText()

        if from_unit == to_unit:
            self.convert_btn.setEnabled(False)
            self.status_label.setText("⚠️  Select different units")
            self.status_label.setStyleSheet("color: orange;")
        else:
            self.convert_btn.setEnabled(True)
            self.status_label.setText("Ready to convert")
            self.status_label.setStyleSheet("color: gray;")

    def on_convert(self):
        """Handle convert button click."""
        try:
            value = self.temp_input.value()
            from_unit = self.from_combo.currentText()
            to_unit = self.to_combo.currentText()

            # Use business logic from separate module
            result = convert_temperature(value, from_unit, to_unit)

            # Display result
            self.result_label.setText(f"{result:.2f}° {to_unit}")
            self.result_label.setStyleSheet("font-size: 18pt; font-weight: bold; color: green;")

            self.status_label.setText("✓ Conversion successful")
            self.status_label.setStyleSheet("color: green;")

        except ValueError as e:
            self.result_label.setText(f"Error: {e}")
            self.result_label.setStyleSheet("color: red;")
            self.status_label.setText(f"✗ {e}")
            self.status_label.setStyleSheet("color: red;")

        except Exception as e:
            self.result_label.setText(f"Unexpected error")
            self.result_label.setStyleSheet("color: red;")
            self.status_label.setText(f"✗ Error: {e}")
            self.status_label.setStyleSheet("color: red;")

    def on_reset(self):
        """Reset to defaults."""
        self.temp_input.setValue(0)
        self.from_combo.setCurrentText('Celsius')
        self.to_combo.setCurrentText('Fahrenheit')
        self.result_label.setText("Result will appear here")
        self.result_label.setStyleSheet("")
        self.status_label.setText("Reset to defaults")
        self.status_label.setStyleSheet("color: gray;")


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    window = TempConverterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
