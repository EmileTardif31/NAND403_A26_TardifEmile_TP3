print("ui file imported")

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QMessageBox, QGroupBox, QSpinBox
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Random Animation Generator")
        self.setFixedWidth(400)
        self.create_ui()
 
    def create_ui(self):
        layout = QVBoxLayout(self)

        timing_group = QGroupBox("Animation Timing")
        timing_layout = QHBoxLayout()
        timing_group.setLayout(timing_layout)

        layout.addWidget(timing_group)

        timing_spin = QSpinBox(self)
        timing_spin.setRange(1, 10)
        timing_layout.addWidget(timing_spin)
 
        button = QPushButton(self)
        button.setText("Generate Animation")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
   
    def on_click(self):
        messageBox = QMessageBox.information(
            self,
            "Mon texte",
            text_box.toPlainText()
        )
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()