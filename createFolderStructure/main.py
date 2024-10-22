import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate


class FolderStructureApp(QWidget):
    def __init__(self):
        super().__init__()
        # Load the UI from the .ui file
        loadUi("folder_structure.ui", self)

        # Set current date in the date input field
        self.dateInput.setDate(QDate.currentDate())

        # Connect button click to the function
        self.selectButton.clicked.connect(self.select_folder)

    def select_folder(self):
        # Get folder path from user
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')

        # Get values from name and date inputs
        name = self.nameInput.text()
        date = self.dateInput.date().toString('yyyy-MM-dd')

        # Check if the name is empty and show an error message if it is
        if not name:
            self.show_error_message("Error", "Please enter a name before proceeding!")
            return

        # Create the root folder name from name and date
        root_folder_name = f"{name}_{date}"

        # Create the folder structure
        if folder_path:
            root_folder_path = os.path.join(folder_path, root_folder_name)
            os.makedirs(root_folder_path, exist_ok=True)
            self.create_folder_structure(root_folder_path)

            # Show success message
            self.show_success_message("Success", "Folder structure created successfully!")

    def create_folder_structure(self, root_folder_path):
        # Define the correct folder structure
        structure = [
            "φωτογραφιες/raw αρχεια",
            "φωτογραφιες/ετοιμες/επιλογες για αλμπουμ/γονεις",
            "φωτογραφιες/ετοιμες/επιλογες για αλμπουμ/νονος",
            "φωτογραφιες/ετοιμες/εκτυπωσεις/10x15",
            "φωτογραφιες/ετοιμες/εκτυπωσεις/13x18",
            "φωτογραφιες/ετοιμες/εκτυπωσεις/καμβας/20x30",
            "φωτογραφιες/ετοιμες/εκτυπωσεις/καμβας/40x60",
            "φωτογραφιες/ετοιμες/εκτυπωσεις/καμβας/50x70",
            "φωτογραφιες/ετοιμες/φουλ αναλυση",
            "φωτογραφιες/ετοιμες/δειγμα φωτογραφιων",
            "βιντεο/ετοιμο βιντεο",
            "βιντεο/ναος μυστήριο/nikon z5",
            "βιντεο/ναος μυστήριο/gopro",
            "βιντεο/drone/ναος",
            "βιντεο/drone/next day",
        ]

        # Create folders
        for folder in structure:
            try:
                os.makedirs(os.path.join(root_folder_path, folder), exist_ok=True)
            except OSError as e:
                print(f"Error creating folder {folder}: {e}")

    def show_success_message(self, title, message):
        # Display a success message box when done
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def show_error_message(self, title, message):
        # Display an error message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FolderStructureApp()
    window.show()
    sys.exit(app.exec_())
