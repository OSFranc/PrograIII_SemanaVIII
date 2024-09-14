#Contruir un programa que muestre una ventana a través de la cual
# se pueda leer su numero de celula y su nombre completo

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout,QHBoxLayout,QFormLayout)
import sys

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ejercicio 3")
        layoutFormulario=QFormLayout()
        
        self.txtCedula=""
        self.txtNombre=""
        
        self.lblNombre=QLabel("Nombre: ")
        self.lnNombre=QLineEdit()
        
        
        self.lblCedula=QLabel("Cedula: ")
        self.lnCedula=QLineEdit()
        
        btnGuardar=QPushButton("Guardar")
        btnMostrar=QPushButton("Cargar Datos")
        self.lblRespuesta=QLabel("")
        
        btnGuardar.clicked.connect(self.ClickBtnGuardarDatos)
        btnMostrar.clicked.connect(self.ClickBtnMostrar)
        
        layoutFormulario.addRow(self.lblNombre,self.lnNombre)
        layoutFormulario.addRow(self.lblCedula,self.lnCedula)
        layoutFormulario.addRow(btnGuardar,self.lblRespuesta)
        

        
        self.lblNombreGuardado=QLabel(" - ")
        self.lblCedulaGuardado=QLabel(" - ")
        
        layoutMostrarDatos=QVBoxLayout()
        layoutMostrarDatos.addWidget(self.lblNombreGuardado)
        layoutMostrarDatos.addWidget(self.lblCedulaGuardado)
        layoutMostrarDatos.addWidget(btnMostrar)
        
        layoutPrincipal=QHBoxLayout()
        layoutPrincipal.addLayout(layoutFormulario)
        layoutPrincipal.addLayout(layoutMostrarDatos)
        
        widget=QWidget()
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)
        
    def ClickBtnGuardarDatos(self):
            self.txtNombre=self.lnNombre.text()
            self.txtCedula=self.lnCedula.text()
            self.lblRespuesta.setText("Datos Guardados con Exito")
            
    def ClickBtnMostrar(self):
            self.lblNombreGuardado.setText(self.txtNombre)
            self.lblCedulaGuardado.setText(self.txtCedula)
        
    

app=QApplication(sys.argv)
ventana = ventanaPrincipal()
ventana.show()
app.exec()
        
        
        
        
                
        