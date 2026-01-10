import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox

class MianWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        checkbox = QCheckBox("This is a checkbox")
        #checkbox.setCheckState(Qt.CheckState.Checked)
        #checkbox.checkStateChanged.connect(self.show_state_2)
        checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.show_state_1)
        self.setCentralWidget(checkbox)

    def show_state_1(self, s):
        print(s)
        if s == Qt.CheckState.Checked.value:
            print("Checked")
        elif s == Qt.CheckState.Unchecked.value:
            print("Unchecked")
        elif s == Qt.CheckState.PartiallyChecked.value:
            print("PartiallyChecked")


    def show_state_2(self, s):
        print(s.value)
app = QApplication(sys.argv)

window = MianWindow()
window.show()

app.exec()