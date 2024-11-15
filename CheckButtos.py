import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QCheckBox, QRadioButton)


class RadioButton(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.button_cambio_rojo = QCheckBox("red")
        self.button_cambio_azul = QCheckBox("blue")
        self.button_cambio_naranja = QCheckBox("orange")
        self.button_cambio_amarillo = QCheckBox("yellow")
        self.button_cambio_rosa = QCheckBox("pink")
        self.button_cambio_gris = QCheckBox("gray")
        self.button_cambio_blanco = QCheckBox("white")
        self.button_formulario = QCheckBox("Formulario")

        self.addWidget(self.button_cambio_rojo)
        self.addWidget(self.button_cambio_azul)
        self.addWidget(self.button_cambio_naranja)
        self.addWidget(self.button_cambio_amarillo)
        self.addWidget(self.button_cambio_rosa)
        self.addWidget(self.button_cambio_gris)
        self.addWidget(self.button_cambio_blanco)
        self.addWidget(self.button_formulario)