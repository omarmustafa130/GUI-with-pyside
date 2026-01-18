import sys
from layout_colorwidget import Color
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tab widget")

        tabs = QTabWidget()

        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)
        #tabs.setTabsClosable(True)
        #tabs.setDocumentMode(True)
        
        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)
        tabs.setTabShape(QTabWidget.TabShape.Triangular)
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()