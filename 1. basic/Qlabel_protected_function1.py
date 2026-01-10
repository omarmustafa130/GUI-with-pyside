import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

# 1. We create a new class that inherits from QLabel
class ClickableLabel(QLabel):
    
    # 2. We REIMPLEMENT the 'mousePressEvent' protected function
    def mousePressEvent(self, event):
        # This code runs whenever the user clicks this label
        print("You clicked the label!")
        
        # Optional: Call the parent version if you still want standard behavior
        super().mousePressEvent(event) 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Use our custom class instead of the standard QLabel
        self.label = ClickableLabel("Click Me!")
        layout.addWidget(self.label)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()