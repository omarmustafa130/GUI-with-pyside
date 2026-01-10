import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        self.setFixedSize(QSize(400,300))

        button = QPushButton("press me")
        button.setCheckable(True)
        button.clicked.connect(self.button_click)
        button.clicked.connect(self.button_toggled)

        self.setCentralWidget(button)

    
    def button_click(self):
        print("this button is clicked")

    def button_toggled(self, is_checked):
        print("Checked? ", is_checked)
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()