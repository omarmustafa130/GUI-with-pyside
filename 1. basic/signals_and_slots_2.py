import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        self.setFixedSize(QSize(400,300))

        self.button = QPushButton("Press Here")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText("Already clicked!")
        self.setWindowTitle("A new window title")
        self.button.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()