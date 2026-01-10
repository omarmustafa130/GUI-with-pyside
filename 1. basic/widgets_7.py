import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox
from PySide6.QtCore import QRect, QSize
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400,400))
        singleBox = QSpinBox(self)
        singleBox.setMinimum(0)
        singleBox.setMaximum(10)
        #singleBox.setRange(1,10)
        singleBox.setSingleStep(1)
        singleBox.setPrefix("$")
        singleBox.setSuffix("c")
        singleBox.valueChanged.connect(self.single_value_changed)
        singleBox.textChanged.connect(self.single_value_changed_str)
        singleBox.setGeometry(QRect(150, 100, 100, 25))


        doubleBox = QDoubleSpinBox(self)
        doubleBox.setRange(10.0, 10.9)
        doubleBox.setSingleStep(0.1)
        doubleBox.valueChanged.connect(self.double_value_changed)
        doubleBox.textChanged.connect(self.double_value_changed_str)
        doubleBox.setGeometry(QRect(150, 200, 100, 25))
        

    def single_value_changed(self, i):
        print(i)

    def single_value_changed_str(self, str):
        print(str)

    def double_value_changed(self, f):
        print(f)

    def double_value_changed_str(self, str):
        print(str)

    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()