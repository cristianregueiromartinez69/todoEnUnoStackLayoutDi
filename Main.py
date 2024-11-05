import sys
import random

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget,
                              QStackedLayout)

from CajaColor import CajaColor
from DatosFormulario import DatosWidget
from BotonesFormulario import Botones
from Botones_colores import boton_color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejemplo QStackLayout')
        self.setFixedSize(600, 600)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        caja_central = QVBoxLayout()
        caja_Formulario = QVBoxLayout()

        datos_widget = DatosWidget()
        botones_widget = Botones()
        boton_color_cambio = boton_color()

        caja_Formulario.addLayout(datos_widget)
        caja_Formulario.addLayout(botones_widget)


        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(CajaColor("red"))
        self.stack_layout.addWidget(CajaColor("blue"))
        self.stack_layout.addWidget(CajaColor("orange"))
        self.stack_layout.addWidget(CajaColor("yellow"))
        self.stack_layout.addWidget(CajaColor("pink"))
        self.stack_layout.addWidget(CajaColor("gray"))
        self.stack_layout.addWidget(CajaColor("white"))
        containerFormulario = QWidget()



        containerFormulario.setLayout(caja_Formulario)
        self.stack_layout.addWidget(containerFormulario)

        caja_central.addLayout(self.stack_layout)
        caja_central.addLayout(boton_color_cambio)




        self.stack_layout.setCurrentIndex(1)

        container = QWidget()
        container.setLayout(caja_central)
        self.setCentralWidget(container)
        self.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()