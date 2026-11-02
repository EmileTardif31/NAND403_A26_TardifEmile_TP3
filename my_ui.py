from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QMessageBox, QGroupBox, QSpinBox
 
class RandomAnimationUI(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Random Animation Generator")
        self.setFixedWidth(400)
        self.create_ui()
 
    def create_ui(self):
        layout = QVBoxLayout(self)

        # animation timing
        timing_group = QGroupBox("Animation Timing")
        timing_layout = QHBoxLayout()
        timing_group.setLayout(timing_layout)

        timing_text = QLabel("Duration (Frames)")
        step_text = QLabel("Step (Frames)")

        timing_spin = QSpinBox(self)
        step_spin = QSpinBox(self)
        timing_spin.setRange(1, 10)
        step_spin.setRange(1, 10)

        layout.addWidget(timing_group)
        timing_layout.addWidget(timing_text)
        timing_layout.addWidget(timing_spin)
        timing_layout.addWidget(step_text)
        timing_layout.addWidget(step_spin)

        # translate parameters
        translate_group = QGroupBox("Translate Parameters")
        translate_layout = QVBoxLayout()
        translate_layout_row1 = QHBoxLayout()
        translate_layout_row1.setSpacing(30)
        translate_layout_row2 = QHBoxLayout()
        translate_layout_row2.setSpacing(30)

        translate_layout.addLayout(translate_layout_row1)
        translate_layout.addLayout(translate_layout_row2)

        translate_group.setLayout(translate_layout)

        translate_minx = QLabel("min x")
        translate_miny = QLabel("min y")
        translate_minz = QLabel("min z")
        translate_maxx = QLabel("max x")
        translate_maxy = QLabel("max y")
        translate_maxz = QLabel("max z")

        translate_spin_minx = QSpinBox(self)
        translate_spin_miny = QSpinBox(self)
        translate_spin_minz = QSpinBox(self)
        translate_spin_maxx = QSpinBox(self)
        translate_spin_maxy = QSpinBox(self)
        translate_spin_maxz = QSpinBox(self)

        translate_spin_minx.setRange(-100, 100)
        translate_spin_minx.setValue(7)
        translate_spin_miny.setRange(-100, 100)
        translate_spin_miny.setValue(5)
        translate_spin_minz.setRange(-100, 100)
        translate_spin_minz.setValue(2)
        translate_spin_maxx.setRange(-100, 100)
        translate_spin_maxx.setValue(1)
        translate_spin_maxy.setRange(-100, 100)
        translate_spin_maxy.setValue(4)
        translate_spin_maxz.setRange(-100, 100)
        translate_spin_maxz.setValue(3)

        translate_spin_minx.setMinimumWidth(50)
        translate_spin_miny.setMinimumWidth(50)
        translate_spin_minz.setMinimumWidth(50)
        translate_spin_maxx.setMinimumWidth(50)
        translate_spin_maxy.setMinimumWidth(50)
        translate_spin_maxz.setMinimumWidth(50)

        layout.addWidget(translate_group)

        translate_layout_row1.addWidget(translate_minx)
        translate_layout_row1.addWidget(translate_spin_minx)
        translate_layout_row1.addWidget(translate_miny)
        translate_layout_row1.addWidget(translate_spin_miny)
        translate_layout_row1.addWidget(translate_minz)
        translate_layout_row1.addWidget(translate_spin_minz)
        translate_layout_row2.addWidget(translate_maxx)
        translate_layout_row2.addWidget(translate_spin_maxx)
        translate_layout_row2.addWidget(translate_maxy)
        translate_layout_row2.addWidget(translate_spin_maxy)
        translate_layout_row2.addWidget(translate_maxz)
        translate_layout_row2.addWidget(translate_spin_maxz)



        # bouton generate
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
    widget = RandomAnimationUI()
    widget.show()