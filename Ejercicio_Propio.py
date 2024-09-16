from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout,QHBoxLayout,QFormLayout,QRadioButton,QComboBox,QTextBrowser)
import sys

#Se busca crear mediante un programa, una calculadora que permita conocer un plan de ahorro para un individuo 
#Segun su presupuesto y tiempo con el que dispone, ademas de mostrar otras opciones de tiempo según se requiera

#Creamos un listado que correspondrá a las opciones de unidades de tiempo para la calculadora
listadoTiempo=["Dias","Semanas","Meses","Años"]

#Creamos la ventana donde se ejecutará nuestro programa
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Asignamos un título a nuestra ventana
        self.setWindowTitle("Calculadora Ahorradora")
        
        #Creamos la estructura que tendrá el formulario de entrada de datos para la calculadora
        self.lblCantidad=QLabel("Monto a Ahorrar: ")
        self.lnCantidad=QLineEdit()
        
        #Para escoger la unidad de tiempo creamos un comboBox que tendrá como opciones la lista que creamos anteriormente:
        self.lblTiempo=QLabel("Tiempo: ")
        self.optTiempo=QComboBox()
        self.optTiempo.addItems(listadoTiempo)
        self.lnTiempoNum=QLineEdit()
        
        self.lblResultado=QLabel("Resultado: ")
        self.lblResultadoNum=QLabel("")
        
        #En un Text Browser mostraremos un pequeño enunciado del resultado obtenido según los cálculos. Ya que 
        #Es mas facil de visualizar para textos mas largos que una etiqueta
        self.lblResultadoEnunciado=QTextBrowser()
        
        #Creamos el botón calcular y lo conectamos a la función correspondiente luego de hacerle click
        btnCalcular=QPushButton("Calular")
        btnCalcular.clicked.connect(self.ClickBtnCalcular)
        
        #Creamos un Layout de tipo formulario para la entrada de datos de la calculadora
        layoutIngreso=QFormLayout()
        layoutIngreso.addRow(self.lblCantidad,self.lnCantidad)
        layoutIngreso.addRow(self.lblTiempo,self.lnTiempoNum)
        layoutIngreso.addRow(self.optTiempo)
        layoutIngreso.addRow(self.lblResultado, self.lblResultadoNum)
        layoutIngreso.addRow(btnCalcular)
        
        #Añadimos un layout para la salida de datos
        layoutSalida=QVBoxLayout()
        layoutSalida.addWidget(self.lblResultadoEnunciado)
        
        #Creamos la layout principal y colocamos las layouts de salida y entrada de datos correspondiente
        layoutPrincipal=QHBoxLayout()
        layoutPrincipal.addLayout(layoutIngreso)
        layoutPrincipal.addLayout(layoutSalida)
        
        
        widget=QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layoutPrincipal)
        
        
        #Creamos la función que se encargará de hacer los cálculos y generar el enunciado con la respuesta para el usuario
    def ClickBtnCalcular(self):
        
        #Obtenemos el texto de los recuadros de texto y los convertimos a variables de tipo Int para poder ser operados como números
        monto = int(self.lnCantidad.text())
        tiempoNum= int(self.lnTiempoNum.text())
        timepoUnidad= self.optTiempo.currentText()
        
        #Creamos complementos para el enunciado que se irán creado de acuerdo a lo que seleccione el usuario
        resp2=""
        resp3=""
        resp4=""
        
        #Colocamos condicionales para ajustar el enunciado y otras variables de tiempo con sus calculos de acuerdo a la opción que
        #El usuario haya seleccionado
        
        if timepoUnidad == "Semanas":
            resp2=f"Opción 2: ${round(monto/(tiempoNum*7),2)} por {tiempoNum*7} Días"    
        elif timepoUnidad == "Meses":
            resp2=f"Opción 2: ${round(monto/(tiempoNum*30),2)} por {tiempoNum*30} Días"
            resp3=f"Opción 3: ${round(monto/(tiempoNum*4),2)} por {tiempoNum*4} Semanas"
        elif timepoUnidad == "Años":
            resp2=f"Opción 2: ${round(monto/(tiempoNum*360),2)} por {tiempoNum*365} Días"
            resp3=f"Opción 3: ${round(monto/(tiempoNum*52),2)} por {tiempoNum*52} Semanas"
            resp4=f"Opción 4: ${round(monto/(tiempoNum*12),2)} por {tiempoNum*12} Meses"
        else: resp="Llene todos los datos antes de continuar"
        
        #Creamos la variable que contendrá el enunciado del resultado concatenando lo obtenido en el "If" anterior 
        resp=(f"Para ahorrar ${monto} en {tiempoNum} {self.optTiempo.currentText()} se deben guardar: ${round((monto/tiempoNum),2)} cada {self.optTiempo.currentText()}"
        +" / "+ resp2 + " / " + resp3 +" / " + resp4)
        
        #Pasamos el texto de la variable anterior al recuadro de texto de resultado
        self.lblResultadoEnunciado.setText(resp)
            
        
#Ingresamos las instrucciones para ejecutar nuestra Ventana         
app=QApplication(sys.argv)
ventana=VentanaPrincipal()
ventana.show()
app.exec()