#Contruir un programa que muestre una Ventana en la cual
#Aparezca su nombre completo y su edad Centrados

#Importamos las librerias de PyQT5 que utilizaremos:
from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QPushButton,
                            QLabel,QLineEdit,QLayout,QVBoxLayout,QHBoxLayout)
import sys


#Creamos la clase donde se ejecutará nuestra ventana
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Colocamos nombre a nuestra ventana
        self.setWindowTitle("Ejercicio 1")
        
        #Establecemos el layout de nuestra ventana y lo que contnedrá
        #En este caso, dos Layouts Horizonales para mostrar ambos integrantes
        layout1=QVBoxLayout()
        layout2=QVBoxLayout()
        layoutCentral=QHBoxLayout()
        
        #Añadimos los widgets necesarios, en este caso unicamente utilizaremos el widget Label para mostrar información
        self.lblNombre1=QLabel("Oscar Rene Palacios Franco")
        self.lblEdad1=QLabel("Edad: 24 Años")
        
        self.lblNombre2=QLabel("Gerson Manases Flores Quinteros")
        self.lblEdad2=QLabel("Edad:19 Años")
        
        #Pasamos los widgets a los Layouts correspondientes
        layout1.addWidget(self.lblNombre1)
        layout1.addWidget(self.lblEdad1)
        layout2.addWidget(self.lblNombre2)
        layout2.addWidget(self.lblEdad2)
        layoutCentral.addLayout(layout1)
        layoutCentral.addLayout(layout2)
        
        widget=QWidget()
        widget.setLayout(layoutCentral)
        self.setCentralWidget(widget)
        
        
#Ingresamos las instrucciones para ejecutar nuestra Ventana
app=QApplication(sys.argv)
Ventana=mainWindow()
Ventana.show()
app.exec()
        
        
        
        
        