import sys
from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.widget = QListWidget()
        self.widget.addItems(["Option 1", "Option 2", "Option 3"])
        self.widget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        #self.widget.currentItemChanged.connect(self.item_changed)
        #self.widget.currentTextChanged.connect(self.text_changed)
        self.widget.selectionModel().selectionChanged.connect(self.selection_changed)
        self.setCentralWidget(self.widget)

    def item_changed(self, item):
        print(item.text())

    def text_changed(self, text):
        print(text)

    def selection_changed(self):
        list = []
        for i in self.widget.selectedItems():
            list.append(i.text())
        print(f"Selected Items: ", list)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()