import sys
import os
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StatusBar")
        #self.setFixedSize(400,300)
        
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        base_dir = os.path.dirname(__file__)
        button_action = QAction(
                                QIcon(os.path.join(base_dir, "bug.png")),
                                "Your button", 
                                self
                                )
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        button_action.triggered.connect(self.button_action_triggered)
        button_action.setStatusTip("This is an action button")
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def button_action_triggered(self, is_checked):
        print("click ", is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()