import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import uic  # Used to load .ui files at runtime
from PIL import Image
import os

class ImageConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file dynamically
        uic.loadUi('image_converter.ui', self)

        # Add items to the "from" and "to" ComboBoxes
        supported_formats = ["JPEG", "PNG", "BMP", "GIF", "TIFF", "ICO", "WEBP", "AVIF"]
        self.comboBox_from.addItems(supported_formats)
        self.comboBox_to.addItems(supported_formats)

        # Apply a modern stylesheet
        self.apply_stylesheet()

        # Connect buttons to functions
        self.pushButton_select.clicked.connect(self.select_images)
        self.pushButton_convert.clicked.connect(self.convert_images)

        # Initialize image_files list
        self.image_files = []

    def apply_stylesheet(self):
        # QSS stylesheet with modern styling
        stylesheet = """
        QWidget {
            background-color: #f5f5f5;
            font-family: 'Roboto', sans-serif;
            color: #333;
        }

        QComboBox {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 4px;
            padding: 5px;
            font-size: 14px;
            color: #333;
        }

        QPushButton {
            background-color: #5cb85c;
            border: none;
            color: white;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            transition-duration: 0.4s;
        }

        QPushButton:hover {
            background-color: #4cae4c;
        }

        QPushButton:pressed {
            background-color: #4caf50;
        }

        QLabel {
            font-size: 16px;
            margin-bottom: 5px;
            color: #333;
        }

        QPushButton#pushButton_select {
            background-color: #0275d8;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px;
            color: white;
        }

        QPushButton#pushButton_select:hover {
            background-color: #025aa5;
        }

        QPushButton#pushButton_convert {
            background-color: #d9534f;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px;
            color: white;
        }

        QPushButton#pushButton_convert:hover {
            background-color: #c9302c;
        }
        """
        self.setStyleSheet(stylesheet)

    def select_images(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.image_files, _ = QFileDialog.getOpenFileNames(self, "Select Images", "",
        "All Files (*);;JPEG (*.jpg);;PNG (*.png);;BMP (*.bmp);;GIF (*.gif);;TIFF (*.tiff);;ICO (*.ico);;WEBP (*.webp);;AVIF (*.avif)",
        options=options)
        if self.image_files:
            QMessageBox.information(self, "Images Selected", f"Selected {len(self.image_files)} images")

    def convert_images(self):
        if not self.image_files:
            QMessageBox.warning(self, "No Images", "Please select some images first!")
            return

        from_format = self.comboBox_from.currentText().lower()
        to_format = self.comboBox_to.currentText().lower()

        for file_path in self.image_files:
            if file_path.lower().endswith(from_format):
                try:
                    img = Image.open(file_path)

                    # Check if the target format is JPEG and the image has an alpha channel (RGBA)
                    if img.mode == 'RGBA' and to_format == 'jpeg':
                        img = img.convert('RGB')  # Remove the alpha channel by converting to RGB

                    # Save the converted image
                    new_file_path = os.path.splitext(file_path)[0] + f"_converted.{to_format}"
                    img.save(new_file_path, to_format.upper())
                    QMessageBox.information(self, "Success", f"Successfully converted {file_path} to {new_file_path}")

                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Could not convert {file_path}: {str(e)}")
            else:
                QMessageBox.warning(self, "Format Mismatch", f"Selected file {file_path} does not match the 'from' format")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ImageConverter()
    converter.show()
    sys.exit(app.exec_())
