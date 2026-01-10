import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])
window = QPushButton("Press here!")
window.show()

app.exec()
