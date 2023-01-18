import main
import funciones
import time
import datetime

class Usuario:

    def __init__(self, nombre, user, password, tipo_usuario):
        self.nombre= nombre
        self.user= user
        self.password= password
        self.tipo_usuario= tipo_usuario

    def login(self):
        ##login con usuario ya existente
        cursor= main.conn.cursor()
        consulta = "select tipo_usuario from usuarios where user=? and password=?;"
        parametros= (self.user,self.password)
        cursor.execute(consulta,parametros)
        main.conn.commit()
        resultado = cursor.fetchone()
        if resultado:
            print("Logueado!")
            time.sleep(1.5)
            funciones.borrarPantalla()
        else:
            print("Algo salio mal")
            exit()

    def registro(self):
        ##registrar un usuario en la bd
        cursor= main.conn.cursor()
        registro = "insert into usuarios (nombre,user,password,tipo_usuario) values (?,?,?,?)"
        parametros= (self.nombre,self.user,self.password,self.tipo_usuario)
        cursor.execute(registro,parametros)
        main.conn.commit()
        print("Usuario registrado exitosamente")
        time.sleep(1.5)
        funciones.borrarPantalla()


class Auto:

    def __init__(self, patente, marca, modelo, color, observacion):
        self.patente= patente
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.observacion= observacion

    def modificarFecha(self):
        ##checkeo si existe el auto y muestro los movimientos que tiene
        cursor= main.conn.cursor()
        parametros = (self.patente,)
        consulta_auto = "select patente,marca,modelo,color from autos where patente = ?"
        consulta_movimiento = "select * from movimientos where patente = ?"
        cursor.execute(consulta_auto,parametros)
        resultado_auto = cursor.fetchone()
        cursor.execute(consulta_movimiento,parametros)
        if cursor.fetchone():
            print("Los datos del auto a modificar fecha: ")
            print()
            print("Patente: ", resultado_auto[0], "\nMarca: ", resultado_auto[1], "\nModelo: ", resultado_auto[2], "\nColor: ", resultado_auto[3]) 
            consulta = "select fecha_ingreso, fecha_egreso from movimientos where patente= ?;"
            cursor.execute(consulta,parametros)
            resultado_movimiento = cursor.fetchone()
            print("Fecha de ingreso: ", resultado_movimiento[0], "\nFecha de egreso: ", resultado_movimiento[1])
            print("¿Desea modificar la fecha de ingreso o de egreso del vehiculo? \n 1. Modificar fecha de ingreso \n 2. Modificar fecha de egreso \n 0. Volver al menú")
            opcion = int(input("Opcion: "))
            if opcion != 0:
                funciones.opcionFecha(opcion,self.patente)
            else:
                funciones.volverMenu(opcion)   
        else:
            print("Patente mal ingresada")

    def buscarPatente(self):
        ##consulto la patente y muestro los campos que tiene
        cursor= main.conn.cursor()
        parametros = (self.patente,)
        consulta = "select patente,marca,modelo,color,observacion from autos where patente = ?"
        cursor.execute(consulta,parametros)
        resultado = cursor.fetchone()
        if resultado:
            print("Datos del auto registrado: ")
            print()
            print("Patente: ", resultado[0], "\nMarca: ", resultado[1], "\nModelo: ", resultado[2], "\nColor: ", resultado[3] , "\nObservacion: ", resultado[4])

    def agregarPatente(self):
        ##inserto el auto nuevo y lo agrego tambien en la tabla de movimientos con la hora actual
        cursor= main.conn.cursor()
        parametros= (self.patente, self.marca, self.modelo, self.color,self.observacion)
        insert_auto= "insert into autos (patente,marca,modelo,color,observacion) values (?,?,?,?,?);"
        cursor.execute(insert_auto,parametros)
        insert_movimiento= "insert into movimientos (patente,fecha_ingreso) values (?,?);"
        tiempo=datetime.datetime.now()
        ingreso=tiempo.strftime('%d/%m/%Y %H:%M:%S')
        parametros_movimientos = (self.patente, ingreso)
        cursor.execute(insert_movimiento,parametros_movimientos)
        print("El auto fue ingresado exitosamente")
        main.conn.commit()


    def pagarEstacionamiento(self):
        ##consulto si el auto esta en el garage, y si esta muestro los datos y actualizo la fecha de egreso con la hora actual
        cursor= main.conn.cursor()
        parametros = (self.patente,)
        consulta_auto = "select patente,marca,modelo,color from autos where patente = ?"
        consulta_movimiento = "select * from movimientos where patente = ?"
        cursor.execute(consulta_auto,parametros)
        resultado_auto = cursor.fetchone()
        cursor.execute(consulta_movimiento,parametros)
        if cursor.fetchone():
            print("Los datos del auto a retirar: ")
            print()
            print("Patente: ", resultado_auto[0], "\nMarca: ", resultado_auto[1], "\nModelo: ", resultado_auto[2], "\nColor: ", resultado_auto[3])
            update_movimiento= "update movimientos set fecha_egreso= ? where patente = ?;"
            tiempo=datetime.datetime.now()
            egreso=tiempo.strftime('%d/%m/%Y %H:%M:%S') 
            parametros_update = (egreso, self.patente)
            cursor.execute(update_movimiento, parametros_update)
            main.conn.commit()
            consulta = "select fecha_ingreso, fecha_egreso from movimientos where patente= ?;"
            cursor.execute(consulta,parametros)
            resultado_movimiento = cursor.fetchone()
            print("Fecha de ingreso: ", resultado_movimiento[0], "\nFecha de egreso: ", resultado_movimiento[1])
        else:
            print("patente mal ingresada")