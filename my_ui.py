import sys
import os

project_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, project_path)

import importlib
import my_animator

importlib.invalidate_caches() # refresh le check des modules pour mieux reload nos fichiers

importlib.reload(my_animator) # reload my_animator

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QMessageBox, QGroupBox, QSpinBox
 
class RandomAnimationUI(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Random Animation Generator")
        self.setFixedWidth(400)
        self.create_ui()
 
    def create_ui(self):
        layout = QVBoxLayout(self)

        # --- animation timing ---

        timing_group = QGroupBox("Animation Timing")
        timing_layout = QHBoxLayout()
        timing_group.setLayout(timing_layout)

        timing_text = QLabel("Duration (Frames)")
        step_text = QLabel("Step (Frames)")

        global timing_spin
        global step_spin
        timing_spin = QSpinBox(self)
        step_spin = QSpinBox(self)
        timing_spin.setRange(1, 10)
        step_spin.setRange(1, 10)

        layout.addWidget(timing_group)
        timing_layout.addWidget(timing_text)
        timing_layout.addWidget(timing_spin)
        timing_layout.addWidget(step_text)
        timing_layout.addWidget(step_spin)

        # --- translate parameters ---

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

        global translate_spin_minx
        global translate_spin_miny
        global translate_spin_minz
        global translate_spin_maxx
        global translate_spin_maxy
        global translate_spin_maxz
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

        # --- rotate parameters ---

        rotate_group = QGroupBox("Rotate Parameters")
        rotate_layout = QVBoxLayout()
        rotate_layout_row1 = QHBoxLayout()
        rotate_layout_row1.setSpacing(30)
        rotate_layout_row2 = QHBoxLayout()
        rotate_layout_row2.setSpacing(30)

        rotate_layout.addLayout(rotate_layout_row1)
        rotate_layout.addLayout(rotate_layout_row2)

        rotate_group.setLayout(rotate_layout)

        rotate_minx = QLabel("min x")
        rotate_miny = QLabel("min y")
        rotate_minz = QLabel("min z")
        rotate_maxx = QLabel("max x")
        rotate_maxy = QLabel("max y")
        rotate_maxz = QLabel("max z")

        global rotate_spin_minx
        global rotate_spin_miny
        global rotate_spin_minz
        global rotate_spin_maxx
        global rotate_spin_maxy
        global rotate_spin_maxz
        rotate_spin_minx = QSpinBox(self)
        rotate_spin_miny = QSpinBox(self)
        rotate_spin_minz = QSpinBox(self)
        rotate_spin_maxx = QSpinBox(self)
        rotate_spin_maxy = QSpinBox(self)
        rotate_spin_maxz = QSpinBox(self)

        rotate_spin_minx.setRange(-100, 100)
        rotate_spin_minx.setValue(7)
        rotate_spin_miny.setRange(-100, 100)
        rotate_spin_miny.setValue(5)
        rotate_spin_minz.setRange(-100, 100)
        rotate_spin_minz.setValue(2)
        rotate_spin_maxx.setRange(-100, 100)
        rotate_spin_maxx.setValue(1)
        rotate_spin_maxy.setRange(-100, 100)
        rotate_spin_maxy.setValue(4)
        rotate_spin_maxz.setRange(-100, 100)
        rotate_spin_maxz.setValue(3)

        rotate_spin_minx.setMinimumWidth(50)
        rotate_spin_miny.setMinimumWidth(50)
        rotate_spin_minz.setMinimumWidth(50)
        rotate_spin_maxx.setMinimumWidth(50)
        rotate_spin_maxy.setMinimumWidth(50)
        rotate_spin_maxz.setMinimumWidth(50)

        layout.addWidget(rotate_group)

        rotate_layout_row1.addWidget(rotate_minx)
        rotate_layout_row1.addWidget(rotate_spin_minx)
        rotate_layout_row1.addWidget(rotate_miny)
        rotate_layout_row1.addWidget(rotate_spin_miny)
        rotate_layout_row1.addWidget(rotate_minz)
        rotate_layout_row1.addWidget(rotate_spin_minz)
        rotate_layout_row2.addWidget(rotate_maxx)
        rotate_layout_row2.addWidget(rotate_spin_maxx)
        rotate_layout_row2.addWidget(rotate_maxy)
        rotate_layout_row2.addWidget(rotate_spin_maxy)
        rotate_layout_row2.addWidget(rotate_maxz)
        rotate_layout_row2.addWidget(rotate_spin_maxz)

        # --- scale parameters ---
        scale_group = QGroupBox("Scale Parameters")
        scale_layout = QVBoxLayout()
        scale_layout_row1 = QHBoxLayout()
        scale_layout_row1.setSpacing(30)
        scale_layout_row2 = QHBoxLayout()
        scale_layout_row2.setSpacing(30)

        scale_layout.addLayout(scale_layout_row1)
        scale_layout.addLayout(scale_layout_row2)

        scale_group.setLayout(scale_layout)

        scale_minx = QLabel("min x")
        scale_miny = QLabel("min y")
        scale_minz = QLabel("min z")
        scale_maxx = QLabel("max x")
        scale_maxy = QLabel("max y")
        scale_maxz = QLabel("max z")

        global scale_spin_minx
        global scale_spin_miny
        global scale_spin_minz
        global scale_spin_maxx
        global scale_spin_maxy
        global scale_spin_maxz
        scale_spin_minx = QSpinBox(self)
        scale_spin_miny = QSpinBox(self)
        scale_spin_minz = QSpinBox(self)
        scale_spin_maxx = QSpinBox(self)
        scale_spin_maxy = QSpinBox(self)
        scale_spin_maxz = QSpinBox(self)

        scale_spin_minx.setRange(-100, 100)
        scale_spin_minx.setValue(7)
        scale_spin_miny.setRange(-100, 100)
        scale_spin_miny.setValue(5)
        scale_spin_minz.setRange(-100, 100)
        scale_spin_minz.setValue(2)
        scale_spin_maxx.setRange(-100, 100)
        scale_spin_maxx.setValue(1)
        scale_spin_maxy.setRange(-100, 100)
        scale_spin_maxy.setValue(4)
        scale_spin_maxz.setRange(-100, 100)
        scale_spin_maxz.setValue(3)

        scale_spin_minx.setMinimumWidth(50)
        scale_spin_miny.setMinimumWidth(50)
        scale_spin_minz.setMinimumWidth(50)
        scale_spin_maxx.setMinimumWidth(50)
        scale_spin_maxy.setMinimumWidth(50)
        scale_spin_maxz.setMinimumWidth(50)

        layout.addWidget(scale_group)

        scale_layout_row1.addWidget(scale_minx)
        scale_layout_row1.addWidget(scale_spin_minx)
        scale_layout_row1.addWidget(scale_miny)
        scale_layout_row1.addWidget(scale_spin_miny)
        scale_layout_row1.addWidget(scale_minz)
        scale_layout_row1.addWidget(scale_spin_minz)
        scale_layout_row2.addWidget(scale_maxx)
        scale_layout_row2.addWidget(scale_spin_maxx)
        scale_layout_row2.addWidget(scale_maxy)
        scale_layout_row2.addWidget(scale_spin_maxy)
        scale_layout_row2.addWidget(scale_maxz)
        scale_layout_row2.addWidget(scale_spin_maxz)

        # --- bouton generate ---

        button = QPushButton(self)
        button.setText("Generate Animation")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
   
    def on_click(self):
        my_animator.create_animation(
            timing_spin,
            step_spin,
            translate_spin_minx,
            translate_spin_miny,
            translate_spin_minz,
            translate_spin_maxx,
            translate_spin_maxy,
            translate_spin_maxz,
            rotate_spin_minx,
            rotate_spin_miny,
            rotate_spin_minz,
            rotate_spin_maxx,
            rotate_spin_maxy,
            rotate_spin_maxz,
            scale_spin_minx,
            scale_spin_miny,
            scale_spin_minz,
            scale_spin_maxx,
            scale_spin_maxy,
            scale_spin_maxz
        )
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = RandomAnimationUI()
    widget.show()