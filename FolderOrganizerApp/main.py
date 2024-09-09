import os
import shutil
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class FolderOrganizerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(FolderOrganizerApp, self).__init__()
        uic.loadUi('folder_organizer.ui', self)

        # Connect the button to the methods
        self.selectFolderButton.clicked.connect(self.select_folder)
        self.organizeButton.clicked.connect(self.organize_folder)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folderPathLineEdit.setText(folder_path)

    def organize_folder(self):
        folder_path = self.folderPathLineEdit.text()

        if not os.path.isdir(folder_path):
            QMessageBox.warning(self, "Error", "Please select a valid folder.")
            return

        extensions = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv'],
            'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.txt'],
            'Music': ['.mp3', '.wav', '.flac'],
            'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
            'Executables': ['.exe', '.msi'],
        }

        files_moved = False

        # Move files into corresponding folders
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                file_ext = os.path.splitext(item)[1].lower()
                moved = False
                for folder, ext_list in extensions.items():
                    if file_ext in ext_list:
                        folder_dir = os.path.join(folder_path, folder)
                        if not os.path.exists(folder_dir):
                            os.makedirs(folder_dir)
                        shutil.move(item_path, folder_dir)
                        moved = True
                        files_moved = True
                        break
                if not moved:
                    # Move unclassified files to a "Miscellaneous" folder
                    misc_folder = os.path.join(folder_path, 'Miscellaneous')
                    if not os.path.exists(misc_folder):
                        os.makedirs(misc_folder)
                    shutil.move(item_path, misc_folder)
                    files_moved = True

        if files_moved:
            QMessageBox.information(self, "Success", "Folder organized successfully!")
        else:
            QMessageBox.information(self, "No Files",
                                    "No files were organized because there were no matching file types.")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = FolderOrganizerApp()
    window.show()
    app.exec_()
