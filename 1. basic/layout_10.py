import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QLineEdit, QComboBox, QFormLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        layout = QFormLayout()

        self.name = QLineEdit()
        self.age = QSpinBox()
        self.age.setRange(0,150)
        self.icecream = QComboBox()
        self.icecream.addItems(["Chocolate", "Vanilla", "Strawberry"])
        layout.addRow("Name", self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favourite Ice Cream", self.icecream)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()