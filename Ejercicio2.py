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
        
        #Inicializamos el atributo contraseña como una variable de tipo cadena vacío
        self.Contraseña=""
        
        #Colocamos la interfaz con dos opciónes de verificar y guardar
        self.lnIngresar=QLineEdit()
        self.lnVerificar=QLineEdit()
        self.lblRespuesta=QLabel(". . .")
        btnVerificar=QPushButton("Verificar")
        btnGuardar=QPushButton("Guardar")
        
        #Con el comando setEchoMode pasamos como parametro la QLineEdit que contendrá la contrseña que 
        #Ingresaremos para que se mantenga oculta
        self.lnIngresar.setEchoMode(QLineEdit.Password)
        self.lnVerificar.setEchoMode(QLineEdit.Password)
        
        self.lblGuardarContraseña=QLabel("Ingrese una clave a Guardar")
        self.lblVerificarGuardado=QLabel("Verificar Contraseña Guardada")
        
        #Conectamos los botones a las funciones correspondientes
        btnGuardar.clicked.connect(self.ClicBtnGuardar)
        btnVerificar.clicked.connect(self.ClicBtnVerificar)
        
        #Creamos los layouts donde estará todo distribuido, utilizaremos layouts Verticales y Horizontales
        layoutIngresar=QVBoxLayout()
        layoutVerificar=QVBoxLayout()
        layoutRespuesta=QHBoxLayout()
        layoutInput=QHBoxLayout()
        layoutOutput=QHBoxLayout()
        
        layoutPrincipal=QHBoxLayout()
        
        
        #Añadimos los Widgets a los layouts que hemos creado
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
    
    
    #Definimos las funciones que se encargarán de guardar y verificar la cadena que hemos colocado como contraseña
    def ClicBtnGuardar(self):
        self.Contraseña= self.lnIngresar.text()
        self.lblRespuesta.setText("Contraseña Guardada!")
        
    def ClicBtnVerificar(self):
        if self.Contraseña== self.lnVerificar.text():
            self.lblRespuesta.setText("Contraseña Correcta!")
        else:
            self.lblRespuesta.setText("Contraseña Incorrecta")
        
#Ingresamos las instrucciones para ejecutar nuestra Ventana                
app=QApplication(sys.argv)
Ventana=mainWindow()
Ventana.show()
app.exec()