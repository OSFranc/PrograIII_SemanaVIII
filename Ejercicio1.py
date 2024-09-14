#Contruir un programa que muestre una Ventana en la cual
#Aparezca su nombre completo y su edad Centrados

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QPushButton,
                            QLabel,QLineEdit,QLayout,QVBoxLayout,QHBoxLayout)
import sys


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout1=QVBoxLayout()
        layout2=QVBoxLayout()
        layoutCentral=QHBoxLayout()
        self.lblNombre1=QLabel("Oscar Rene Palacios Franco")
        self.lblEdad1=QLabel("Edad: 24 Años")
        
        self.lblNombre2=QLabel("Gerson Manases Flores Quinteros")
        self.lblEdad2=QLabel("Edad:19 Años")
        
        layout1.addWidget(self.lblNombre1)
        layout1.addWidget(self.lblEdad1)
        layout2.addWidget(self.lblNombre2)
        layout2.addWidget(self.lblEdad2)
        layoutCentral.addLayout(layout1)
        layoutCentral.addLayout(layout2)
        
        widget=QWidget()
        widget.setLayout(layoutCentral)
        self.setCentralWidget(widget)
        
app=QApplication(sys.argv)
Ventana=mainWindow()
Ventana.show()
app.exec()
        
        
        
        
        