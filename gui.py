
import sys
# manipulador de items aplicacion ventana y ventanas emergentes
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtCore, QtGui, QtWidgets           # manipulacion archivos designer
from dataSource import *

# ***************  Conexion Base de Datos  *****************#
con = dataSource("", "", "", "bdproyecto", "","sqlite")

# Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):

    # variables utilizadas
    encabezado = ""
    tabla = ""
    sql = ""
    datos = []
    
    # Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        # Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("interfaz.ui", self)  
        
        # ********************************************* eventos *********************************************#
        # Ingresar en el login  
        self.btningresar.clicked.connect(self.mostrar)
        # ******************************************* eventos ventana 
        # ver datos tablas
        self.btn_usuario.clicked.connect(self.usuario)
        self.btn_bien.clicked.connect(self.bien)
        self.btn_personal.clicked.connect(self.personal)
        self.btn_control.clicked.connect(self.control)     
        # ******************************************* eventos Crud
        # Seleccionar datos
        self.verdatos.clicked.connect(self.seleccionar)
        # Guardar
        self.btn_guardar_usuario.clicked.connect(self.ausuario)
        self.btn_guardar_bien.clicked.connect(self.abien)
        self.btn_guardar_personal.clicked.connect(self.apersonal)
        self.btn_guardar_control.clicked.connect(self.acontrol)
        # Modificar
        self.btn_modificar_usuario.clicked.connect(self.modificaru)
        self.btn_modificar_bien.clicked.connect(self.modificarb)
        self.btn_modificar_personal.clicked.connect(self.modificarp)
        self.btn_modificar_control.clicked.connect(self.modificarc)
        # eliminar
        self.btn_eliminar.clicked.connect(self.eliminar)


    #******************************************** Login Inicio Secion  ****************************************#
    def mostrar(self):
        if not self.txtusuario.text() and not self.txtclave.text():
            self.resultado.setText("Introducir Datos!!")
        else:
            u = self.txtusuario.text()
            p = self.txtclave.text() 
            self.tabla = "usuario"
            self.sql = "select * from "+ self.tabla +" where user='"+u+"' and pass='"+p+"' and rol='Administrador'"
            q = con.getData(self.sql)
            if not q:
                self.resultado.setText("Usuario o Contraseña Incorrecta")
            else:
                self.swventana.setCurrentIndex(1)



    #******************************************** Seleccionar tabla ****************************************#
    # ver los datos de la tabla usuarios
    def usuario(self):
        self.encabezado =["ID ", "Identificacion ", " Nombres y Apellidos ", " Usuario ", " Contraseña ", " Rol "]
        self.tabla = "usuario" 
        self.sql = "select * from " + self.tabla
        self.ver()  
    # agregar usuario 
    def ausuario(self,event):
        resultado = QMessageBox.question(self,"!Agregar!","Deseas agregar el Usuario "+self.txtnombre_usuario.text()+"", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.datos.append(self.txtidentificacion_usuario.text())
            self.datos.append(self.txtnombre_usuario.text())
            self.datos.append(self.txtusuario_nombre.text())
            self.datos.append(self.txtclave_usuario.text())
            self.datos.append(self.cbxrol.currentText())
            self.agregar()
    # Borrar usuario 
    def busuario(self):
        self.sql = "delete from "+ self.tabla +" where id_usuario = "

    # ***************************************************************
    # ver los datos de la tabla Bien
    def bien(self):
        self.encabezado =["ID", "Identificacion", "Nombre", "Ficha Formacion", "Tipo", "Serie", "Marca"]
        self.tabla = "bienes"
        self.sql = "select * from " + self.tabla
        self.ver()  
    # agregar bien
    def abien(self):
        resultado = QMessageBox.question(self,"!Agregar!","Deseas agregar el Bien de "+self.txtnombre_bien.text()+"?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.datos.append(self.txtidentificacion_bienes.text())
            self.datos.append(self.txtnombre_bien.text())
            self.datos.append(self.txtfichafor_bien.text())
            self.datos.append(self.txttipo_bien.text())
            self.datos.append(self.txtserie_bien.text())
            self.datos.append(self.txtmarca_bien.text())
            self.agregar()
    # Borrar Bienes 
    def bbien(self):
        self.sql = "delete from "+ self.tabla +" where id_bienes = "

    # ***************************************************************
    # ver los datos de la tabla Personal
    def personal(self):
        self.encabezado =["ID", "Identificacion", "Nombre", "Ficha Formacion", "Telefono", "Correo", "Rol"]
        self.tabla = "personal"
        self.sql = "select * from " + self.tabla
        self.ver()    
    # agregar Personal
    def apersonal(self):
        resultado = QMessageBox.question(self,"!Agregar!","Deseas agregar el Personal "+self.txtnombres_personal.text()+"?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.datos.append(self.txtidentificacion_personal_7.text())
            self.datos.append(self.txtnombres_personal.text())
            self.datos.append(self.txtfichaformacion_personal.text())
            self.datos.append(self.txttelefono_personal.text())
            self.datos.append(self.txtcorreo_personal.text())            
            self.datos.append(self.cbxrol_personal.currentText())
            self.agregar()
    # Borrar Personal 
    def bpersonal(self):
        self.sql = "delete from "+ self.tabla +" where id_personal = "

    # ***************************************************************
    # ver los datos de la tabla Control
    def control(self):
        self.encabezado =["ID", "Identificacion", "Fecha Entrada", "Fecha Salida"]
        self.tabla = "controles" 
        self.sql = "select * from " + self.tabla
        self.ver() 
    # agregar Control 
    def acontrol(self):
        resultado = QMessageBox.question(self,"!Agregar!","Deseas agregar el Control E/S con ID "+self.txtidentificacion_control.text()+"", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.datos.append(self.txtidentificacion_control.text())
            self.datos.append(self.dtfechahe.text())
            self.datos.append(self.dtfechahs.text())
            self.agregar()
    # Borrar control 
    def bcontrol(self):
        self.sql = "delete from "+ self.tabla +" where id_control = "
   
    #******************************************** funciones crud *******************************************#
    def agregar(self):
        valores = ""
    
        for i in self.datos:
            v = ""
            try:
                int (i)
                v = str(i)
            except:
                v = "\"" + str(i) + "\""  
            valores += ", " + v
       
        q = "insert into "+ self.tabla + " values (null" + valores + ")"
        v = con.query(q)
                
        self.ver()
               
    #******************************** funcion ver datos ************************************************ # 
    def ver(self):
        self.datos.clear()

        encabezado = self.encabezado
        sql = self.sql

        self.verdatos.clear()

        _translate = QtCore.QCoreApplication.translate

         # organizacion del encabezado
        cantidad = len(encabezado)
        self.verdatos.setColumnCount(cantidad)

        for i in range (cantidad):
            item = QtWidgets.QTableWidgetItem()
            self.verdatos.setHorizontalHeaderItem(i, item)
        
            item = self.verdatos.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", encabezado[i]))
        
        self.verdatos.setVerticalHeaderLabels(encabezado)

        # Vista de elementos
        c = con.getData(sql)
        fila = 1
        
        for i in c:
            self.verdatos.setRowCount(fila)
            for p in range (cantidad):
                self.verdatos.setItem(fila - 1, p, QtWidgets.QTableWidgetItem(str(i[p])))
            fila += 1

    # **************************************  funcion Modificar datos usuario ******************************************* # 
    
    def modificaru (self):
        resultado = QMessageBox.question(self,"!Editar!","Deseas Editar el Usuario", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            try:
                datosm = []
                # obtengo el numero de la fila seleccionada
                fila = self.verdatos.currentRow()
                # obtengo el valor de las celdas
                
                cantidad = len(self.encabezado)
                
                for i in range (cantidad):
                    datosm.append((self.verdatos.item(fila, i)).text())

                cambio = False
                for i in range (len(datosm)):
                    if self.datos[i] == datosm[i]:
                        cambio = True
            
                if cambio:
                    sql = "update " + self.tabla + " set nombre = '" + datosm[1] + "', identificacion = '" + datosm[2] + "', user = '" + datosm[3] + "', pass = '" + datosm[4] + "', rol = '" + datosm[5] + "' where id = " + datosm[0] +""
                    q = con.query(sql)
                    if q:
                        QMessageBox.information(self, 'Modificacion Exitosa',"Se modificaron los datos de manera satisfactoria", QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, 'Error Modificacion',"Hubo un error en la consulta", QMessageBox.Yes)
                self.ver()
            except:
                QMessageBox.information(self, 'Error al Modificar',"Debe seleccionar un registro de la lista para Modificar", QMessageBox.Yes)

    # **************************************  funcion Modificar datos bien ******************************************* # 
    
    def modificarb (self):
        resultado = QMessageBox.question(self,"!Editar!","Deseas Editar el Bien", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            try:
                datosm = []
                # obtengo el numero de la fila seleccionada
                fila = self.verdatos.currentRow()
                # obtengo el valor de las celdas
                
                cantidad = len(self.encabezado)
                
                for i in range (cantidad):
                    datosm.append((self.verdatos.item(fila, i)).text())

                cambio = False
                for i in range (len(datosm)):
                    if self.datos[i] == datosm[i]:
                        cambio = True
            
                if cambio:
                    sql = "update " + self.tabla + " set identificacion = " + datosm[1] + ", nombre = '" + datosm[2] + "', ficha_formacion = " + datosm[3] + ", tipo = '" + datosm[4] + "', serie = '" + datosm[5] + "', marca = '" + datosm[6] + "' where id = " + datosm[0] +""
                    q = con.query(sql)
                    if q:
                        QMessageBox.information(self, 'Modificacion Exitosa',"Se modificaron los datos de manera satisfactoria", QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, 'Error Modificacion',"Hubo un error en la consulta", QMessageBox.Yes)
                self.ver()
            except:
                QMessageBox.information(self, 'Error al Modificar',"Debe seleccionar un registro de la lista para Modificar", QMessageBox.Yes)

    # **************************************  funcion Modificar datos personal ******************************************* # 
    
    def modificarp (self):
        resultado = QMessageBox.question(self,"!Editar!","Deseas Editar el Personal", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            try:
                datosm = []
                # obtengo el numero de la fila seleccionada
                fila = self.verdatos.currentRow()
                # obtengo el valor de las celdas
                
                cantidad = len(self.encabezado)
                
                for i in range (cantidad):
                    datosm.append((self.verdatos.item(fila, i)).text())

                cambio = False
                for i in range (len(datosm)):
                    if self.datos[i] == datosm[i]:
                        cambio = True
            
                if cambio:
                    sql = "update " + self.tabla + " set identificacion = " + datosm[1] + ", nombre = '" + datosm[2] + "', ficha_formacion = " + datosm[3] + ", telefono = " + datosm[4] + ", correo = '" + datosm[5] + "', rol = '" + datosm[6] + "' where id = " + datosm[0] +""
                    q = con.query(sql)
                    if q:
                        QMessageBox.information(self, 'Modificacion Exitosa',"Se modificaron los datos de manera satisfactoria", QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, 'Error Modificacion',"Hubo un error en la consulta", QMessageBox.Yes)
                self.ver()
            except:
                QMessageBox.information(self, 'Error al Modificar',"Debe seleccionar un registro de la lista para Modificar", QMessageBox.Yes)

    # **************************************  funcion Modificar datos control ******************************************* # 
    
    def modificarc (self):
        resultado = QMessageBox.question(self,"!Editar!","Deseas Editar el Control E/S", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            try:
                datosm = []
                # obtengo el numero de la fila seleccionada
                fila = self.verdatos.currentRow()
                # obtengo el valor de las celdas
                
                cantidad = len(self.encabezado)
                
                for i in range (cantidad):
                    datosm.append((self.verdatos.item(fila, i)).text())

                cambio = False
                for i in range (len(datosm)):
                    if self.datos[i] == datosm[i]:
                        cambio = True
            
                if cambio:
                    sql = "update " + self.tabla + " set identificacion = " + datosm[1] + ", fechahe = '" + datosm[2] + "', fechahs = '" + datosm[3] + "' where id = " + datosm[0] +""
                    q = con.query(sql)
                    if q:
                        QMessageBox.information(self, 'Modificacion Exitosa',"Se modificaron los datos de manera satisfactoria", QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, 'Error Modificacion',"Hubo un error en la consulta", QMessageBox.Yes)
                self.ver()
            except:
                QMessageBox.information(self, 'Error al Modificar',"Debe seleccionar un registro de la lista para Modificar", QMessageBox.Yes)
        

    # **************************************  funcion borrar datos ******************************************* # 
    
    def eliminar (self):
        try:
            q = "delete from "+ self.tabla +" where id = "+ str(self.datos[0])+""
            
            resultado = QMessageBox.question(self, "Eliminar registro", "¿Esta Seguro que quieres Borrar el registro?", QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes: 
                con.query(q) 
            self.ver()
        except:
            QMessageBox.information(self, 'Error al eliminar',"Debe seleccionar un dato de la lista para eliminar", QMessageBox.Yes)

    
    # ****************************************  funciones especiales ******************************************* # 
    
    # funcion seleccionar elemento
    def seleccionar(self):
        self.datos.clear()
        
        # obtengo el numero de la fila seleccionada
        fila = self.verdatos.currentRow()
        # obtengo el valor de las celdas
        
        cantidad = len(self.encabezado)
        
        for i in range (cantidad):
            self.datos.append((self.verdatos.item(fila, i)).text())
       

    # ****************************************  Evento para cuando la ventana se cierra ******************************************* # 
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()


# Instancia para iniciar una aplicación
app = QApplication(sys.argv)
# Crear un objeto de la clase
_ventana = Ventana()
# Mostra la ventana
_ventana.show()
# Ejecutar la aplicación
app.exec_()