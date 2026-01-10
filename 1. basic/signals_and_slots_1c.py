import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = False
        self.setWindowTitle("My APP")
        self.setFixedSize(QSize(400,300))

        button = QPushButton("press me")
        button.setCheckable(True)
        button.clicked.connect(self.button_click)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    
    def button_click(self, is_checked):
        print("this button is clicked")
        self.button_is_checked = is_checked
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()