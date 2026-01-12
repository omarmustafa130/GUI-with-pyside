import sys
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QStackedLayout, 
    QPushButton
)
from PySide6.QtCore import QSize
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("stacked layout with buttons")
        self.setFixedSize(QSize(400,300))
        


        button_red = QPushButton("Red")
        button_green = QPushButton("Green")
        button_blue = QPushButton("Blue")

        button_red.pressed.connect(self._red_pressed)
        button_green.pressed.connect(self._green_pressed)
        button_blue.pressed.connect(self._blue_pressed)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(button_red)
        buttons_layout.addWidget(button_green)
        buttons_layout.addWidget(button_blue)

        self.color_layout = QStackedLayout()
        self.color_layout.addWidget(Color('red'))
        self.color_layout.addWidget(Color('green'))
        self.color_layout.addWidget(Color('blue'))

        page_layout = QVBoxLayout()

        page_layout.addLayout(buttons_layout)
        page_layout.addLayout(self.color_layout)

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)


    def _red_pressed(self):
        self.color_layout.setCurrentIndex(0)

    def _green_pressed(self):
        self.color_layout.setCurrentIndex(1)

    def _blue_pressed(self):
        self.color_layout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()