import sys
from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QComboBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(300,300))
        combo_box = QComboBox(parent=self)
        combo_box.addItems(["Option A", "Option B", "Option C"])
        combo_box.currentIndexChanged.connect(self.combo_box_index_changed)
        combo_box.currentTextChanged.connect(self.combo_box_text_changed)
        #combo_box.setFrame(True)
        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        combo_box.setMaxCount(5)
        width = 100
        height = 25
        start_x = 125
        stary_y = 125

        combo_box.setFixedSize(QSize(width,height))
        combo_box.setGeometry(QRect(start_x, stary_y, width, height))
        #self.setCentralWidget(combo_box) 

    def combo_box_index_changed(self, index):
        print(index)
    
    def combo_box_text_changed(self, text):
        print(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()