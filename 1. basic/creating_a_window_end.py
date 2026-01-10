import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        self.setMinimumSize(QSize(200, 100))
        self.setMaximumSize(QSize(600, 400))
        #self.setFixedSize(QSize(400, 300))

        button = QPushButton("Press Me!")
        

        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()