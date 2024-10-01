#Contruir un programa que muestre una ventana a través de la cual
# se pueda leer su numero de celula y su nombre completo

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout,QHBoxLayout,QFormLayout)
import sys

#Creamos la ventana principal donde se ejecutará nuestro programa
class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Asignamos un título a la ventana
        self.setWindowTitle("Ejercicio 3")
        layoutFormulario=QFormLayout()
        
        #Inicializamos los atributos Cédula y Nombre como variables de tipo cadena vacías.
        self.txtCedula=""
        self.txtNombre=""
        
        #Creamos los labels para la entrada de datos
        self.lblNombre=QLabel("Nombre: ")
        self.lnNombre=QLineEdit()
        
        
        self.lblCedula=QLabel("Cedula: ")
        self.lnCedula=QLineEdit()
        
        #Añadimos dos botones que permitan guardar y cargar la información ingresada
        btnGuardar=QPushButton("Guardar")
        btnMostrar=QPushButton("Cargar Datos")
        self.lblRespuesta=QLabel("")
        
        #Conectamos la función correspondiente a cada botón mediante el evento Clicked
        btnGuardar.clicked.connect(self.ClickBtnGuardarDatos)
        btnMostrar.clicked.connect(self.ClickBtnMostrar)
        
        #Añadimos los widgets correspondientes a un layout de tipo formulario
        layoutFormulario.addRow(self.lblNombre,self.lnNombre)
        layoutFormulario.addRow(self.lblCedula,self.lnCedula)
        layoutFormulario.addRow(btnGuardar,self.lblRespuesta)
        

        #Creamos los labels de la salida de datos de momento vacios 
        self.lblNombreGuardado=QLabel(" - ")
        self.lblCedulaGuardado=QLabel(" - ")
        
        #Añadimos los widgets de la salida de datos a un layot de tipo Vertical
        layoutMostrarDatos=QVBoxLayout()
        layoutMostrarDatos.addWidget(self.lblNombreGuardado)
        layoutMostrarDatos.addWidget(self.lblCedulaGuardado)
        layoutMostrarDatos.addWidget(btnMostrar)
        
        #Creamos un layout principal de tipo horizontal y colocamos los layouts anteriores dentro de ella
        layoutPrincipal=QHBoxLayout()
        layoutPrincipal.addLayout(layoutFormulario)
        layoutPrincipal.addLayout(layoutMostrarDatos)
        
        widget=QWidget()
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)
        
        #Creamos una función encargada de guardar las cadenas de text en las variables que iniciamos anteriormente
    def ClickBtnGuardarDatos(self):
            self.txtNombre=self.lnNombre.text()
            self.txtCedula=self.lnCedula.text()
            self.lblRespuesta.setText("Datos Guardados con Exito")
            
        #Función que Asigna el texto de las variables a las etiquetas de salida de datos en la ventana
    def ClickBtnMostrar(self):
            self.lblNombreGuardado.setText(self.txtNombre)
            self.lblCedulaGuardado.setText(self.txtCedula)
        
    
 #Ingresamos las instrucciones para ejecutar nuestra Ventana  
app=QApplication(sys.argv)
ventana = ventanaPrincipal()
ventana.show()
app.exec()
        
        
        
        
                
        