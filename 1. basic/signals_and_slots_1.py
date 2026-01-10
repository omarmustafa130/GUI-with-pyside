import sys
from PySide6.QtCore import QSize

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        self.setFixedSize(QSize(400,300))

        button = QPushButton("Press Me")

        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("buttong was clicked!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()