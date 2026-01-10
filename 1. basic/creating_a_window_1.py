import sys
from PySide6.QtWidgets import QApplication, QWidget

#app = QApplication(sys.argv)
app = QApplication([])

window = QWidget()
window.show()

app.exec()