#Construir un programa que muestre una ventana a través de la cual
#Se puedan Leer 10 datos Característicos de una persona.

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout,QHBoxLayout,QFormLayout,QRadioButton,QComboBox)
import sys

#Creamos una clase llamada RegistroPersonal donde inicializaremos los 10 datos personales 
#del individuo
class RegistroPersonal():
    def __init__(self,nombre,genero,edad,altura,peso,lugarNacimiento,estadoCivil,
                 profesion,color,equipo):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        self.altura=altura
        self.peso=peso
        self.lugarNacimiento=lugarNacimiento
        self.estadoCivil=estadoCivil
        self.profesion=profesion
        self.color=color
        self.equipo=equipo
        
#Creamos la ventana de nuestro programa
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Creamos las etiquetas y cuadros de texto correspondientes para el ingreso de datos 
        self.lblNombre=QLabel("Nombre:")
        self.lnNombre=QLineEdit()
        
        
        #Añadimos para el apartado de Género un ComboBox que almacenará 3 opciones de género 
        #(Adaptandose a tiempos modernos)
        self.lblGenero=QLabel("Genero:")
        self.optGenero=QComboBox()
        self.optGenero.addItem("Masculino")
        self.optGenero.addItem("Femenino")
        self.optGenero.addItem("Otro")
        
        
        self.lblEdad=QLabel("Edad:")
        self.lnEdad=QLineEdit()
        
        self.lblAltura=QLabel("Altura:")
        self.lnAltura=QLineEdit()
        
        self.lblPeso=QLabel("Peso:")
        self.lnPeso=QLineEdit()
        
        self.lblLugarNacimiento=QLabel("Lugar de Nacimiento:")
        self.lnLugarNacimiento=QLineEdit()
        
        #Al igual que con el apartado de género, se ha añadido un combobox para establecer 4 opciones de Estado Civil
        self.lblEstadoCivil=QLabel("Estado Civil:")
        self.optEstadoCivil=QComboBox()
        self.optEstadoCivil.addItem("Soltero/a")
        self.optEstadoCivil.addItem("Casado/a")
        self.optEstadoCivil.addItem("Acompañado/a")
        self.optEstadoCivil.addItem("Otro")
        
        self.lblProfesion=QLabel("Profesion:")
        self.lnProfesion=QLineEdit()
        
        self.lblColorFav=QLabel("Color Favorito:")
        self.lnColorFav=QLineEdit()
        
        self.lblEquipoFav=QLabel("Equipo Favorito:")
        self.lnEquipoFav=QLineEdit()
        
        #Etiquetas para Mostrar Información Guardada:
        self.lblNombre=QLabel("Nombre:")
        self.lblNombreResp=QLabel("")
        
        self.lblGenero=QLabel("Genero:")
        self.lblGeneroResp=QLabel("")
        
        self.lblEdad=QLabel("Edad:")
        self.lblEdadResp=QLabel("")
        
        self.lblAltura=QLabel("Altura:")
        self.lblAlturaResp=QLabel("")
        
        self.lblPeso=QLabel("Peso:")
        self.lblPesoResp=QLabel("")
        
        self.lblLugarNacimiento=QLabel("Lugar de Nacimiento:")
        self.lblLugarNacimientoResp=QLabel("")
        
        
        self.lblEstadoCivil=QLabel("Estado Civil:")
        self.lblEstadoCivilResp=QLabel("")
        
        self.lblProfesion=QLabel("Profesion:")
        self.lblProfesionResp=QLabel("")
        
        self.lblColorFav=QLabel("Color Favorito:")
        self.lblColorFavResp=QLabel("")
        
        self.lblEquipoFav=QLabel("Equipo Favorito:")
        self.lblEquipoFavResp=QLabel("")
        
        #Creamos los botones que permitan guardar la información y también para poder mostrar el último registro 
        btnGuardar=QPushButton("Guardar")
        self.lblRespuesta=QLabel("")
        btnGuardar.clicked.connect(self.ClickGuardar)
        
        btnMostrar=QPushButton("Mostrar Ultimo Registro")
        btnMostrar.clicked.connect(self.ClickMostrar)
                
        #Creamos un layout de tipo formulario para colocar los Widgets correspondientes a la entrada de datos
        layoutFormulario=QFormLayout()
        layoutFormulario.addRow(self.lblNombre,self.lnNombre)
        layoutFormulario.addRow(self.lblGenero,self.optGenero)
        layoutFormulario.addRow(self.lblEdad,self.lnEdad)
        layoutFormulario.addRow(self.lblAltura,self.lnAltura)
        layoutFormulario.addRow(self.lblPeso,self.lnPeso)
        layoutFormulario.addRow(self.lblLugarNacimiento,self.lnLugarNacimiento)
        layoutFormulario.addRow(self.lblEstadoCivil,self.optEstadoCivil)
        layoutFormulario.addRow(self.lblProfesion,self.lnProfesion)
        layoutFormulario.addRow(self.lblColorFav,self.lnColorFav)
        layoutFormulario.addRow(self.lblEquipoFav,self.lnEquipoFav)
        layoutFormulario.addRow(btnGuardar,self.lblRespuesta)
        
        #Creamos un layout de tipo formulario pero esta vez para la salida de datos
        layoutFormularioResp=QFormLayout()
        layoutFormularioResp.addRow(self.lblNombre,self.lblNombreResp)
        layoutFormularioResp.addRow(self.lblGenero,self.lblGeneroResp)
        layoutFormularioResp.addRow(self.lblEdad,self.lblEdadResp)
        layoutFormularioResp.addRow(self.lblAltura,self.lblAlturaResp)
        layoutFormularioResp.addRow(self.lblPeso,self.lblPesoResp)
        layoutFormularioResp.addRow(self.lblLugarNacimiento,self.lblLugarNacimientoResp)
        layoutFormularioResp.addRow(self.lblEstadoCivil,self.lblEstadoCivilResp)
        layoutFormularioResp.addRow(self.lblProfesion,self.lblProfesionResp)
        layoutFormularioResp.addRow(self.lblColorFav,self.lblColorFavResp)
        layoutFormularioResp.addRow(self.lblEquipoFav,self.lblEquipoFavResp)
        layoutFormularioResp.addRow(btnMostrar)
        
        #Añadimos los layouts a un layout principal de tipo Horizontal
        layoutPrincipal=QHBoxLayout()
        layoutPrincipal.addLayout(layoutFormulario)
        layoutPrincipal.addLayout(layoutFormularioResp)
        
        
        widget=QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layoutPrincipal)

#Definimos una función que se encargue de recoger las cadenas y opciones ingresadas en el formulario de ingreso de datos,
#Luego se crea un objeto de la clase con los parametros correspondientes
    def ClickGuardar(self):
        nombre=self.lnNombre.text()
        genero=self.optGenero.currentText()
        edad=self.lnEdad.text()
        altura=self.lnAltura.text()
        peso=self.lnPeso.text()
        lugarNacimiento=self.lnLugarNacimiento.text()
        estadoCivil=self.optEstadoCivil.currentText()
        profesion=self.lnProfesion.text()
        color=self.lnColorFav.text()
        equipo=self.lnEquipoFav.text()
        self.NuevoRegistro=RegistroPersonal(nombre,genero,edad,altura,peso,lugarNacimiento,estadoCivil,profesion,color,equipo)
        self.lblRespuesta.setText(f"{self.NuevoRegistro.nombre} Guardado con Exito!")
    
#Creamos una función que obtenga los atributos del último objeto creado a partir de la función anterior y la muestra en la ventana
    def ClickMostrar(self):
        self.lblNombreResp.setText(self.NuevoRegistro.nombre)
        self.lblGeneroResp.setText(self.NuevoRegistro.genero)
        self.lblEdadResp.setText(self.NuevoRegistro.edad)
        self.lblPesoResp.setText(self.NuevoRegistro.peso)
        self.lblAlturaResp.setText(self.NuevoRegistro.altura)
        self.lblLugarNacimientoResp.setText(self.NuevoRegistro.lugarNacimiento)
        self.lblProfesionResp.setText(self.NuevoRegistro.profesion)
        self.lblEstadoCivilResp.setText(self.NuevoRegistro.estadoCivil)
        self.lblColorFavResp.setText(self.NuevoRegistro.color)
        self.lblEquipoFavResp.setText(self.NuevoRegistro.equipo)
        
        
        
 #Ingresamos las instrucciones para ejecutar nuestra Ventana  
app=QApplication(sys.argv)
ventana=VentanaPrincipal()
ventana.show()
app.exec()

        
        