import flask 

import clases
import menu
import sqlite3
##creacion de la bd y las tablas
conn = sqlite3.connect("garage.db")
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios 
    (id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     nombre   TEXT NOT NULL,
     user TEXT NOT NULL,
     password TEXT NOT NULL,
     tipo_usuario TEXT NOT NULL);''')
conn.execute('''CREATE TABLE IF NOT EXISTS movimientos 
        (id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        patente TEXT NOT NULL,
        fecha_ingreso TEXT NOT NULL,
        fecha_egreso TEXT);''')
conn.execute('''CREATE TABLE IF NOT EXISTS autos 
    (id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     patente   TEXT NOT NULL,
     marca TEXT NOT NULL,
     modelo TEXT NOT NULL,
     color TEXT NOT NULL,
     observacion TEXT NOT NULL);''')


def main():
    print("Ingrese el número de la opción que desee:")
    print("1.Login con usuario ya existente")
    print("2.Registrar un usuario que no existe")
    opcion = int(input(""))
    ##login con usuario existente
    if opcion == 1:
        print("LOGIN")
        user = input("ingrese usuario: ")
        password = input ("ingrese contraseña: ")
        ##checkeo si existe usuario
        cursor= conn.cursor()
        consulta = "select nombre,user,password,tipo_usuario from usuarios where user=? and password=?"
        parametros= (user,password)
        cursor.execute(consulta,parametros)
        resultado = cursor.fetchone()
        if resultado:
            usuario = clases.Usuario(resultado[0], resultado[1], resultado[2], resultado[3])
            usuario.login()
            if usuario.tipo_usuario == "admin":
                ##menu para los admin
                menu.menuAdmin()
            else:
                ##menu para los users
                menu.menuUser()  
        else:
            print("Usuario mal ingresado")   
    ##registro de usuario nuevo       
    elif opcion == 2:
        print("REGISTRO")
        nombre = input ("Nombre: ")
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        tipo_usuario = input ("Tipo de usuario (admin o user): ")
        usuario = clases.Usuario(nombre, usuario, password, tipo_usuario)
        usuario.registro()
        if usuario.tipo_usuario == "admin":
            ##menu para los admin
            menu.menuAdmin()
        else:
            ##menu para los users
            menu.menuUser()

if __name__ == "__main__":
    main()
    conn.close()

