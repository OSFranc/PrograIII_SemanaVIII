#Contruir un programa que muestre una ventan a través de la cual
#Se puedan leer 3 datos basicos de 3 mascotas diferentes

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout,QHBoxLayout,QFormLayout,QRadioButton)
import sys

#Creamos una lista donde se almacenarán los objetos que iremos creando de la clase Mascotas
listadoMascotas=[]

#Creamos la clase mascotas con 3 atributos: nombre, raza y edad
class Mascotas:
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
            
#Creamos la ventana donde se ejecturará nuestro programa

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Incializamos los atributos Nombre, Raza y Edad como cadenas vacías
        self.txtNombre=""
        self.optRaza=""
        self.intEdad=""
        
        #Creamos las etiquetas y recuadros donde se ingresarán los datos de la mascota:
        self.lblNombre=QLabel("Nombre de la Mascota: ")
        self.lnNombre=QLineEdit()
        
        self.optRazaGato=QRadioButton("Gato")
        self.optRazaPerro=QRadioButton("Perro")
        
        self.lblEdad=QLabel("Edad de la Mascota: ")
        self.lnEdad=QLineEdit()
        
        #Creamos un botón que permita guardar la información almacenada y conectarla a la función correspondiente
        btnGuardar=QPushButton("Guardar Mascota")
        btnGuardar.clicked.connect(self.ClickBtnGuardar)
        
        self.lblRespuesta=QLabel(". . .")
        
       #Creamos un apartado donde se mostrarán los datos guardados de 3 mascotas
        self.lblMascotaGuardada1Nombre=QLabel("...")
        self.lblMascotaGuardada1Edad=QLabel("")
        self.lblMascotaGuardada1Raza=QLabel("")
        
        self.lblMascotaGuardada2Nombre=QLabel("...")
        self.lblMascotaGuardada2Edad=QLabel("")
        self.lblMascotaGuardada2Raza=QLabel("")
        
        self.lblMascotaGuardada3Nombre=QLabel("...")
        self.lblMascotaGuardada3Edad=QLabel("")
        self.lblMascotaGuardada3Raza=QLabel("")
        
        #Añadimos la entrada de datos a un Layout de tipo Formulario
        layoutFormularioMascota=QFormLayout()
        layoutFormularioMascota.addRow(self.lblNombre,self.lnNombre)
        layoutFormularioMascota.addRow(self.lblEdad,self.lnEdad)
        layoutFormularioMascota.addRow(self.optRazaGato,self.optRazaPerro)
        layoutFormularioMascota.addRow(btnGuardar,self.lblRespuesta)
        
        layoutMostrarMascotas=QHBoxLayout()
        layoutMascota1=QVBoxLayout()
       
       #Creamos los layouts donde se mostrará la información de cada mascota
        layoutMascota1.addWidget(self.lblMascotaGuardada1Nombre)
        layoutMascota1.addWidget(self.lblMascotaGuardada1Edad)
        layoutMascota1.addWidget(self.lblMascotaGuardada1Raza)
        
        layoutMascota2=QVBoxLayout()
        #Labels para las mascotas
        layoutMascota2.addWidget(self.lblMascotaGuardada2Nombre)
        layoutMascota2.addWidget(self.lblMascotaGuardada2Edad)
        layoutMascota2.addWidget(self.lblMascotaGuardada2Raza)
        
        layoutMascota3=QVBoxLayout()
        #Labels para las mascotas
        layoutMascota3.addWidget(self.lblMascotaGuardada3Nombre)
        layoutMascota3.addWidget(self.lblMascotaGuardada3Edad)
        layoutMascota3.addWidget(self.lblMascotaGuardada3Raza)
        
        layoutMostrarMascotas.addLayout(layoutMascota1)
        layoutMostrarMascotas.addLayout(layoutMascota2)
        layoutMostrarMascotas.addLayout(layoutMascota3)

        #Añadimos ambos layouts a un layout principal y lo establecemos como tal
        layoutPrincipal=QVBoxLayout()
        layoutPrincipal.addLayout(layoutFormularioMascota)
        layoutPrincipal.addLayout(layoutMostrarMascotas)
        
        #Conectamos las funciones al boton guardar
        btnGuardar.clicked.connect(self.ClickBtnGuardar)
        btnGuardar.clicked.connect(self.ActializarLabels)
        
        
        widget=QWidget()
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)
    
    #La función guarda la información ingresada y crea un nuevo objeto de la clase Mascotas con los 3 atributos que acaba de obtener
    #Luego inserta este nuevo objeto a la lista creada anteriormente
    def ClickBtnGuardar(self):
        self.txtNombre=self.lnNombre.text()
        self.intEdad=self.lnEdad.text()
        
        if self.optRazaGato.isChecked():
            self.optRaza="Gato"
        elif self.optRazaPerro.isChecked():
            self.optRaza="Perro"
        else: self.optRaza="No se ha Seleccionado"
        
        NuevaMascota=Mascotas(self.txtNombre,self.optRaza,self.intEdad)
        listadoMascotas.append(NuevaMascota)
                
        self.lblRespuesta.setText(f"{NuevaMascota.nombre} guardado con Exito")       
        
    #La función se activa también al presionar el botón guardar, y muestra la información guardada en la lista según su posición 
    #en la misma, con un máximo de 3 posiciones posibles 
    def ActializarLabels(self):
        
        self.lblMascotaGuardada1Nombre.setText(listadoMascotas[0].nombre)
        self.lblMascotaGuardada1Edad.setText(listadoMascotas[0].edad)
        self.lblMascotaGuardada1Raza.setText(listadoMascotas[0].raza)
        
        if len(listadoMascotas)==4:
            self.lblMascotaGuardada2Nombre.setText(listadoMascotas[3].nombre)
            self.lblMascotaGuardada2Edad.setText(listadoMascotas[3].edad)
            self.lblMascotaGuardada2Raza.setText(listadoMascotas[3].raza)
        
        if len(listadoMascotas)==6:   
            self.lblMascotaGuardada3Nombre.setText(listadoMascotas[5].nombre)
            self.lblMascotaGuardada3Edad.setText(listadoMascotas[5].edad)
            self.lblMascotaGuardada3Raza.setText(listadoMascotas[5].raza)
        
        
 #Ingresamos las instrucciones para ejecutar nuestra Ventana      
app=QApplication(sys.argv)
Ventana=ventanaPrincipal()
Ventana.show()
app.exec()