import sys
from PySide6.QtWidgets import QApplication, QDial, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDial")
        widget = QDial()
        widget.setRange(0,10)
        widget.setSingleStep(1)
        widget.setSliderPosition(5)
        widget.sliderMoved.connect(self.slider_moved)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(widget)

    def slider_pressed(self):
        print("Slider pressed!")

    def slider_released(self):
        print("Slider released!")  

    def slider_moved(self, position):
        print(f"Position: {position}")  

    def value_changed(self, value):
        print(f"Value: {value}")    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()