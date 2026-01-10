import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

base_dir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(100,100))
        label = QLabel("hello there")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setPixmap(QPixmap(os.path.join(base_dir, "qpixmap.jpg")))
        label.setScaledContents(True)
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()