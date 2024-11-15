import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QRadioButton)

class BotonRadio(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.button_cambio_rojo = QRadioButton("red")
        self.button_cambio_azul = QRadioButton("blue")
        self.button_cambio_naranja = QRadioButton("orange")
        self.button_cambio_amarillo = QRadioButton("yellow")
        self.button_cambio_rosa = QRadioButton("pink")
        self.button_cambio_gris = QRadioButton("gray")
        self.button_cambio_blanco = QRadioButton("white")
        self.button_formulario = QRadioButton("Formulario")

        self.addWidget(self.button_cambio_rojo)
        self.addWidget(self.button_cambio_azul)
        self.addWidget(self.button_cambio_naranja)
        self.addWidget(self.button_cambio_amarillo)
        self.addWidget(self.button_cambio_rosa)
        self.addWidget(self.button_cambio_gris)
        self.addWidget(self.button_cambio_blanco)
        self.addWidget(self.button_formulario)

'''
La sintaxis es la misma que la de QPushButton, solo que es circular
Si tenemos uno seleccionado, se deseleccionan los demás
Para conectarlo, funcionan como los QPushButton 
'''