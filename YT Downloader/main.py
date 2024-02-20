from pytube import YouTube
import sys
from PyQt5 import QtWidgets, uic


class YTDownloader(QtWidgets.QMainWindow):
    def __init__(self):
        super(YTDownloader, self).__init__()
        uic.loadUi('YTD.ui', self)
        self.downloadButton.clicked.connect(self.download_video)

    def download_video(self):
        link = self.lineEdit.text()
        yt = YouTube(link)
        downloader = yt.streams.get_highest_resolution()
        downloader.download(filename="Video Download.mp4")
        self.textBrowser.append("Download Complete!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = YTDownloader()
    window.show()
    sys.exit(app.exec_())