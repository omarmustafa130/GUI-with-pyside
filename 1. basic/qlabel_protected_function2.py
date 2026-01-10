import sys
from PySide6.QtCore import Qt  # Contains the key codes (Qt.Key_Escape, etc.)
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 1. Subclass QWidget to create our own custom window
class KeyHunterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Press any key!")
        self.resize(300, 200)

        # Create a label to display results
        self.label = QLabel("Press a key...")
        
        # Style the label to make it big and centered
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    # 2. OVERRIDE the keyPressEvent
    def keyPressEvent(self, event):
        """
        This method runs every time a keyboard key is pressed 
        IF this window is the active window.
        """
        
        # A. Check for specific functional keys (using Qt Enums)
        if event.key() == Qt.Key_Escape:
            self.label.setText("Escape! Closing...")
            self.close()  # Close the window
            
        elif event.key() == Qt.Key_Space:
            self.label.setText("Spacebar!")
            
        elif event.key() == Qt.Key_Return: # Enter key
            self.label.setText("Enter!")

        # B. Check for standard characters (Letters/Numbers)
        else:
            # event.text() gives the string representation (e.g., "a", "1", "@")
            key_text = event.text()
            
            # If it's a non-printable key (like F1 or Shift), text() might be empty
            if key_text:
                self.label.setText(f"You typed: {key_text}")
            else:
                self.label.setText(f"Special Key Code: {event.key()}")

        # C. (Optional) Call the parent's implementation
        # Generally good practice to pass the event up if you didn't handle it fully
        super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyHunterWindow()
    window.show()
    app.exec()