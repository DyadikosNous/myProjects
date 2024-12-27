import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
import librosa


class BPMRenamerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layouts
        self.layout = QtWidgets.QVBoxLayout()
        self.dir_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout = QtWidgets.QHBoxLayout()

        # Widgets
        self.label = QtWidgets.QLabel("Select Directory:")
        self.dir_line_edit = QtWidgets.QLineEdit()
        self.browse_button = QtWidgets.QPushButton("Browse")
        self.rename_button = QtWidgets.QPushButton("Rename by BPM")
        self.progress_bar = QtWidgets.QProgressBar()

        # Assemble the UI
        self.dir_layout.addWidget(self.dir_line_edit)
        self.dir_layout.addWidget(self.browse_button)
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.dir_layout)
        self.layout.addWidget(self.rename_button)
        self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)
        self.setWindowTitle("MP3 BPM Renamer")
        self.setGeometry(300, 300, 500, 200)

        # Progress Bar Properties
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)

        # Event Handlers
        self.browse_button.clicked.connect(self.browse_directory)
        self.rename_button.clicked.connect(self.rename_by_bpm)

    def browse_directory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir_path:
            self.dir_line_edit.setText(dir_path)

    def rename_by_bpm(self):
        directory = self.dir_line_edit.text().strip()
        if not directory:
            QMessageBox.warning(self, "Error", "Please select a directory first.")
            return

        if not os.path.exists(directory):
            QMessageBox.warning(self, "Error", "The selected directory does not exist.")
            return

        self.rename_mp3_by_bpm(directory)
        QMessageBox.information(self, "Success", "Files have been renamed by BPM!")

    def rename_mp3_by_bpm(self, source_dir):
        files = [f for f in os.listdir(source_dir) if f.lower().endswith('.mp3')]
        total_files = len(files)

        if total_files == 0:
            QMessageBox.warning(self, "Error", "No MP3 files found in the selected directory.")
            return

        self.progress_bar.setMaximum(total_files)
        self.progress_bar.setValue(0)

        for i, file_name in enumerate(files):
            file_path = os.path.join(source_dir, file_name)

            # Remove existing BPM prefixes (e.g., "151_300 BPM - Metronome.mp3")
            clean_file_name = file_name
            while "_" in clean_file_name and clean_file_name.split("_", 1)[0].isdigit():
                clean_file_name = clean_file_name.split("_", 1)[1]

            clean_file_path = os.path.join(source_dir, clean_file_name)

            # Rename the file to remove existing BPM prefixes
            os.rename(file_path, clean_file_path)

            # Calculate the BPM
            bpm = self.calculate_bpm(clean_file_path)

            if bpm is not None:
                # Round BPM using the custom logic and ensure it's an integer
                rounded_bpm = int(self.round_bpm(bpm))

                # Add new BPM prefix
                new_file_name = f"{rounded_bpm}_{clean_file_name}"
                new_file_path = os.path.join(source_dir, new_file_name)
                os.rename(clean_file_path, new_file_path)
                print(f"Renamed '{clean_file_name}' to '{new_file_name}'")
            else:
                print(f"BPM could not be calculated for '{clean_file_name}', skipping.")

            self.progress_bar.setValue(i + 1)

    def round_bpm(self, bpm):
        """
        Rounds or floors the BPM according to the specified pattern:
        - 191 to 194 -> 190
        - 195 -> 195
        - 196 to 199 -> 200
        """
        # Use integer division to determine the nearest tens range
        base = (bpm // 10) * 10
        remainder = bpm % 10

        if 1 <= remainder <= 4:  # Floor to the base
            return base
        elif 5 <= remainder <= 9:  # Round up to the next multiple of 10
            return base + 10
        else:  # Directly at the multiple of 10
            return bpm

    def calculate_bpm(self, file_path):
        try:
            # Load audio file using librosa
            y, sr = librosa.load(file_path, sr=None)

            # Calculate onset envelope for beat tracking
            onset_env = librosa.onset.onset_strength(y=y, sr=sr)

            # Estimate tempo (BPM)
            tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, aggregate=None)

            # Select the most likely tempo
            estimated_tempo = tempo[0] if len(tempo) > 0 else None

            # If estimated tempo is very low (e.g., <100), assume it's a fraction and adjust
            if estimated_tempo and estimated_tempo < 100:
                estimated_tempo *= 3  # Adjust for high-tempo songs misinterpreted as low

            return estimated_tempo
        except Exception as e:
            print(f"Error calculating BPM for {file_path}: {e}")
            return None


def main():
    app = QtWidgets.QApplication([])
    window = BPMRenamerApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
