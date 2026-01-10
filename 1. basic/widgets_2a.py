import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("hello there")
        #label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setPixmap(QPixmap("qpixmap.jpg"))
        #label.setScaledContents(False)
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()