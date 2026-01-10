import sys
from PySide6.QtCore import Qt #for alignments
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")

        font = widget.font()

        #font.setPointSize(30)
        font.setBold(True)
        widget.setFont(font)

        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()