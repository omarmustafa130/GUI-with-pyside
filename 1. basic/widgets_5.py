import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        listWidget = QListWidget()
        listWidget.addItems(["Option 1", "Option 2", "Option 3"])
        self.setCentralWidget(listWidget)
        listWidget.currentItemChanged.connect(self.item_changed)
        listWidget.currentTextChanged.connect(self.text_changed)
        listWidget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)

    def item_changed(self, current_item, prev_item):
        print(f"Current Item: {current_item.text()}")
        if prev_item:
            print(f"Previous Item: {prev_item.text()}")
        else:
            print("Previous Item: None")

    def text_changed(self, text):
        print(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()