#Contruir un programa que muestre una ventan a través de la cual
#Se puedan leer 3 datos basicos de 3 mascotas diferentes

from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout,QHBoxLayout,QFormLayout,QRadioButton)
import sys

listadoMascotas=[]

class Mascotas:
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        
    #def PasarDatos(self):
    #    listadoMascotas.append(self)
        

    
        
    
    
class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.txtNombre=""
        self.optRaza=""
        self.intEdad=""
        
        self.lblNombre=QLabel("Nombre de la Mascota: ")
        self.lnNombre=QLineEdit()
        
        self.optRazaGato=QRadioButton("Gato")
        self.optRazaPerro=QRadioButton("Perro")
        
        self.lblEdad=QLabel("Edad de la Mascota: ")
        self.lnEdad=QLineEdit()
        
        btnGuardar=QPushButton("Guardar Mascota")
        btnGuardar.clicked.connect(self.ClickBtnGuardar)
        
        self.lblRespuesta=QLabel(". . .")
        
        #Mostrar a las mascotas guardadas en la Ventana:
        self.lblMascotaGuardada1Nombre=QLabel("...")
        self.lblMascotaGuardada1Edad=QLabel("")
        self.lblMascotaGuardada1Raza=QLabel("")
        
        self.lblMascotaGuardada2Nombre=QLabel("...")
        self.lblMascotaGuardada2Edad=QLabel("")
        self.lblMascotaGuardada2Raza=QLabel("")
        
        self.lblMascotaGuardada3Nombre=QLabel("...")
        self.lblMascotaGuardada3Edad=QLabel("")
        self.lblMascotaGuardada3Raza=QLabel("")
        
        layoutFormularioMascota=QFormLayout()
        layoutFormularioMascota.addRow(self.lblNombre,self.lnNombre)
        layoutFormularioMascota.addRow(self.lblEdad,self.lnEdad)
        layoutFormularioMascota.addRow(self.optRazaGato,self.optRazaPerro)
        layoutFormularioMascota.addRow(btnGuardar,self.lblRespuesta)
        
        layoutMostrarMascotas=QHBoxLayout()
        layoutMascota1=QVBoxLayout()
        #Labels para la mascota1
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

        
        layoutPrincipal=QVBoxLayout()
        layoutPrincipal.addLayout(layoutFormularioMascota)
        layoutPrincipal.addLayout(layoutMostrarMascotas)
        
        btnGuardar.clicked.connect(self.ClickBtnGuardar)
        btnGuardar.clicked.connect(self.ActializarLabels)
        
        
        widget=QWidget()
        widget.setLayout(layoutPrincipal)
        self.setCentralWidget(widget)
    
    
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
        
        #NuevaMascota.PasarDatos()
                
        self.lblRespuesta.setText(f"{NuevaMascota.nombre} guardado con Exito")       
        
    def ActializarLabels(self):
        self.lblMascotaGuardada1Nombre.setText(str(len(listadoMascotas)))
        self.lblMascotaGuardada1Nombre.setText(listadoMascotas[0].nombre)
        
        if len(listadoMascotas)==4:
            self.lblMascotaGuardada2Nombre.setText(listadoMascotas[3].nombre)
        
        if len(listadoMascotas)==6:   
            self.lblMascotaGuardada3Nombre.setText(listadoMascotas[5].nombre)
        
    
app=QApplication(sys.argv)
Ventana=ventanaPrincipal()
Ventana.show()
app.exec()


        
        
    
    
    