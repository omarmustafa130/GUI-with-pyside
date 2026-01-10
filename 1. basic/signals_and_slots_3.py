import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    "My App",
    "Still My App",
    "What on earth",
    "This is surprising",
    "Something went wrong",
]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        self.setFixedSize(QSize(400,300))

        self.button = QPushButton("Press Here")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print('Clicked')
        new_title = choice(window_titles)
        print(f"Setting window title: {new_title}")
        self.setWindowTitle(new_title)

    def the_window_title_changed(self, window_title):
        print(f"window title changed!: {window_title}")

        if window_title == "Something went wrong":
            self.button.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()