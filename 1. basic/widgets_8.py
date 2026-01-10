import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QSlider(Qt.Orientation.Horizontal)
        widget.setMinimum(0)
        widget.setMaximum(10)
        widget.setSingleStep(1)
        widget.setSliderPosition(5)
        widget.sliderMoved.connect(self.slider_position)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, value):
        print(f"value: {value}")

    def slider_position(self, position):
        print(f"position: {position}")

    def slider_pressed(self):
        print(f"slider pressed!")

    def slider_released(self):
        print(f"slider released!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()