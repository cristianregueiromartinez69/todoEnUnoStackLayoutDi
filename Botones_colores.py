import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout)

class boton_color(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.button_cambio_rojo = QPushButton("red")
        self.button_cambio_azul = QPushButton("blue")
        self.button_cambio_naranja = QPushButton("orange")
        self.button_cambio_amarillo = QPushButton("yellow")
        self.button_cambio_rosa = QPushButton("pink")
        self.button_cambio_gris = QPushButton("gray")
        self.button_cambio_blanco = QPushButton("white")
        self.button_formulario = QPushButton("Formulario")



        self.addWidget(self.button_cambio_rojo)
        self.addWidget(self.button_cambio_azul)
        self.addWidget(self.button_cambio_naranja)
        self.addWidget(self.button_cambio_amarillo)
        self.addWidget(self.button_cambio_rosa)
        self.addWidget(self.button_cambio_gris)
        self.addWidget(self.button_cambio_blanco)
        self.addWidget(self.button_formulario)



