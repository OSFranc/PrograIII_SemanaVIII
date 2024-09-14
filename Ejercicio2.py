#Contruir un programa que muestre una ventana y que
#lea una clave secreta sin mostrar los caracteres que la componen

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QPushButton,
                            QLabel,QLineEdit,QLayout,QVBoxLayout,QHBoxLayout)
import sys


#Creamos la clase donde se ejecutará nuestra ventana
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ejercicio 2")
        
        self.Contraseña=""
        
        self.lnIngresar=QLineEdit()
        self.lnVerificar=QLineEdit()
        self.lblRespuesta=QLabel(". . .")
        btnVerificar=QPushButton("Verificar")
        btnGuardar=QPushButton("Guardar")
        
        self.lnIngresar.setEchoMode(QLineEdit.Password)
        self.lnVerificar.setEchoMode(QLineEdit.Password)
        
        self.lblGuardarContraseña=QLabel("Ingrese una clave a Guardar")
        self.lblVerificarGuardado=QLabel("Verificar Contraseña Guardada")
        
        btnGuardar.clicked.connect(self.ClicBtnGuardar)
        btnVerificar.clicked.connect(self.ClicBtnVerificar)
        
        layoutIngresar=QVBoxLayout()
        layoutVerificar=QVBoxLayout()
        layoutRespuesta=QHBoxLayout()
        layoutInput=QHBoxLayout()
        layoutOutput=QHBoxLayout()
        
        layoutPrincipal=QHBoxLayout()
        
        layoutIngresar.addWidget(self.lblGuardarContraseña)
        layoutIngresar.addWidget(self.lnIngresar)
        layoutIngresar.addWidget(btnGuardar)
        
        layoutVerificar.addWidget(self.lblVerificarGuardado)
        layoutVerificar.addWidget(self.lnVerificar)
        layoutVerificar.addWidget(btnVerificar)
        
        layoutRespuesta.addWidget(self.lblRespuesta)
        
        layoutInput.addLayout(layoutIngresar)
        layoutInput.addLayout(layoutVerificar)
        layoutOutput.addLayout(layoutRespuesta)
        
        layoutPrincipal.addLayout(layoutInput)
        layoutPrincipal.addLayout(layoutOutput)
        
        
        widget=QWidget()
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)        
    
    def ClicBtnGuardar(self):
        self.Contraseña= self.lnIngresar.text()
        self.lblRespuesta.setText("Contraseña Guardada!")
        
    def ClicBtnVerificar(self):
        if self.Contraseña== self.lnVerificar.text():
            self.lblRespuesta.setText("Contraseña Correcta!")
        else:
            self.lblRespuesta.setText("Contraseña Incorrecta")
        
                
app=QApplication(sys.argv)
Ventana=mainWindow()
Ventana.show()
app.exec()