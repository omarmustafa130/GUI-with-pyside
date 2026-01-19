import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolbar")
        self.setFixedSize(400,300)
        label = QLabel("Hello toolbars!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Main toolbar!")
        toolbar.toggleViewAction().setEnabled(False)
        self.addToolBar(toolbar)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()