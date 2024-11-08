import sys
import random

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget,
                              QStackedLayout)

from CajaColor import CajaColor
from DatosFormulario import DatosWidget
from BotonesFormulario import Botones
from Botones_colores import boton_color
from RadioButtons import BotonRadio

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

        boton_color_cambio_radio = BotonRadio()

        boton_color_cambio.button_cambio_rojo.clicked.connect(self.cambioRojo)
        boton_color_cambio.button_cambio_azul.clicked.connect(self.cambioAzul)
        boton_color_cambio.button_cambio_naranja.clicked.connect(self.cambioNaranja)
        boton_color_cambio.button_cambio_amarillo.clicked.connect(self.cambioAmarillo)
        boton_color_cambio.button_cambio_rosa.clicked.connect(self.cambioRosa)
        boton_color_cambio.button_cambio_gris.clicked.connect(self.cambioGris)
        boton_color_cambio.button_cambio_blanco.clicked.connect(self.cambioBlanco)
        boton_color_cambio.button_formulario.clicked.connect(self.cambioForm)

        caja_Formulario.addLayout(datos_widget)
        caja_Formulario.addLayout(botones_widget)

        boton_color_cambio_radio.button_cambio_rojo.clicked.connect(self.cambioRojo)
        boton_color_cambio_radio.button_cambio_rojo.setChecked(True) #Metodo para hacer que un boton esté presionando en el momento de iniciar la aplicación
        boton_color_cambio_radio.button_cambio_azul.clicked.connect(self.cambioAzul)
        boton_color_cambio_radio.button_cambio_naranja.clicked.connect(self.cambioNaranja)
        boton_color_cambio_radio.button_cambio_amarillo.clicked.connect(self.cambioAmarillo)
        boton_color_cambio_radio.button_cambio_rosa.clicked.connect(self.cambioRosa)
        boton_color_cambio_radio.button_cambio_gris.clicked.connect(self.cambioGris)
        boton_color_cambio_radio.button_cambio_blanco.clicked.connect(self.cambioBlanco)
        boton_color_cambio_radio.button_formulario.clicked.connect(self.cambioForm)

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
        caja_central.addLayout(boton_color_cambio_radio)




        self.stack_layout.setCurrentIndex(0)

        container = QWidget()
        container.setLayout(caja_central)
        self.setCentralWidget(container)
        self.show()

    def cambioRojo(self):
        self.stack_layout.setCurrentIndex(0)

    def cambioAzul(self):
        self.stack_layout.setCurrentIndex(1)

    def cambioNaranja(self):
        self.stack_layout.setCurrentIndex(2)

    def cambioAmarillo(self):
        self.stack_layout.setCurrentIndex(3)

    def cambioRosa(self):
        self.stack_layout.setCurrentIndex(4)

    def cambioGris(self):
        self.stack_layout.setCurrentIndex(5)

    def cambioBlanco(self):
        self.stack_layout.setCurrentIndex(6)

    def cambioForm(self):
        self.stack_layout.setCurrentIndex(7)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()