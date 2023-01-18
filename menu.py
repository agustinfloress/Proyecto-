import main
import clases
import funciones

def menuUser():
    ##menu para users
    print("Menu user: \n")
    print(" 1. Buscar una patente \n 2. Agregar patente \n 3. Pagar estacionamiento \n 4. Salir")
    opcion = int(input("Opcion: "))
    while opcion != 4: 
            if opcion == 1:
                ##busco la patente
                funciones.borrarPantalla()
                patente = input("Ingrese patente: ")
                cursor= main.conn.cursor()
                consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                parametros= (patente,)
                cursor.execute(consulta,parametros)
                resultado = cursor.fetchone()
                if resultado:
                    ##instancio el objeto con los datos del resultado de la query y llamo al metodo buscarPatente
                    auto = clases.Auto(resultado[0], resultado[1],resultado[2],resultado[3],resultado[4])
                    auto.buscarPatente()
                    opcion = input(" \n 0. Volver al menú \n")
                    funciones.volverMenu(opcion)
                else:
                    ##si no existe la patente, no existe el auto en el garage
                    print("No se encontro ningun auto")
                    opcion = input(" \n 0. Volver al menú \n")
                    funciones.volverMenu(opcion)
            elif opcion == 2:
                ##agrego la patente
                funciones.borrarPantalla()
                print("Para ingresar el vehiculo ingrese los siguientes datos:\n")
                patente= input("Patente:")
                cursor= main.conn.cursor()
                consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                parametros= (patente,)
                cursor.execute(consulta,parametros)
                resultado = cursor.fetchone()
                if resultado:
                    ##si existe la patente, no se puede agregar
                    print("La patente que ingresó ya existe")
                    opcion = input(" \n 0. Volver al menú \n")
                    funciones.volverMenu(opcion)
                else:
                    ##si no existe, instancio al objeto llamando al metodo agregarPatente
                    auto = clases.Auto(patente, input("Marca: \n"), input("Modelo: \n"), input("Color: \n"), input("Alguna observacion a tener en cuenta: \n"))
                    auto.agregarPatente()
                    opcion = input(" \n 0. Volver al menú \n")
                    funciones.volverMenu(opcion)
            elif opcion == 3:
                ##pagar estacionamiento
                funciones.borrarPantalla()
                patente = input("Ingrese patente de auto a retirar: ")
                cursor= main.conn.cursor()
                consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                parametros= (patente,)
                cursor.execute(consulta,parametros)
                resultado = cursor.fetchone()
                if resultado:
                    ##si existe el auto, instancio el objeto llamando al metodo pagarEstacionamiento
                    auto = clases.Auto(resultado[0], resultado[1],resultado[2],resultado[3],resultado[4])
                    auto.pagarEstacionamiento()
                    opcion = input(" \n 0. Volver al menú \n")
                    funciones.volverMenu(opcion)
                else:
                    print("no se encontro ningun auto")
                    opcion = input(" \n 0. Volver al menú \n")
                    funciones.volverMenu(opcion)
            funciones.borrarPantalla()            
            print("Menu user: \n")
            print(" 1. Buscar una patente \n 2. Agregar patente \n 3. Pagar estacionamiento \n 4. Salir")
            opcion = int(input("Opcion: "))   


def menuAdmin():
        print ("Menu admin: \n")
        print(" 1. Modificar fecha de ingreso o egreso de un auto \n 2. Buscar una patente \n 3. Agregar patente \n 4. Pagar estacionamiento \n 5. Salir")
        opcion = int(input("Opcion: "))
        while opcion != 5:
                if opcion == 1:
                    ##modificar la fecha de ingreso o egreso de un auto
                    funciones.borrarPantalla()
                    patente = input("Ingrese patente: ")
                    cursor= main.conn.cursor()
                    consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                    parametros= (patente,)
                    cursor.execute(consulta,parametros)
                    resultado = cursor.fetchone()
                    if resultado:
                        ##si existe el auto, instancio el objeto llamando al metodo modificarFecha
                        auto = clases.Auto(resultado[0], resultado[1],resultado[2],resultado[3],resultado[4])
                        auto.modificarFecha()
                    else:
                        print("No se encontro ningun auto")
                        opcion = input("\n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                elif opcion == 2:
                    ##busco la patente
                    funciones.borrarPantalla()
                    patente = input("Ingrese patente: ")
                    cursor= main.conn.cursor()
                    consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                    parametros= (patente,)
                    cursor.execute(consulta,parametros)
                    resultado = cursor.fetchone()
                    if resultado:
                        ##instancio el objeto con los datos del resultado de la query y llamo al metodo buscarPatente
                        auto = clases.Auto(resultado[0], resultado[1],resultado[2],resultado[3],resultado[4])
                        auto.buscarPatente()
                        opcion = input("\n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                    else:
                        print("La patente que ingresó no existe")
                        opcion = input(" \n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                elif opcion == 3:
                    ##agrego la patente
                    funciones.borrarPantalla()
                    print("Para ingresar el vehiculo ingrese los siguientes datos:\n")
                    patente= input("Patente:")
                    cursor= main.conn.cursor()
                    consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                    parametros= (patente,)
                    cursor.execute(consulta,parametros)
                    resultado = cursor.fetchone()
                    if resultado:
                        ##si existe la patente, no se puede agregar
                        print("La patente que ingresó ya existe")
                        opcion = input(" \n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                    else:
                        ##si no existe, instancio al objeto llamando al metodo agregarPatente
                        auto = clases.Auto(patente, input("Marca: \n"), input("Modelo: \n"), input("Color: \n"), input("Alguna observacion a tener en cuenta: \n"))
                        auto.agregarPatente()
                        opcion = input(" \n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                elif opcion == 4:
                    ##pagar estacionamiento
                    funciones.borrarPantalla()
                    patente = input("Ingrese patente de auto a retirar: ")
                    cursor= main.conn.cursor()
                    consulta = "select patente,marca,modelo,color,observacion from autos where patente=?"
                    parametros= (patente,)
                    cursor.execute(consulta,parametros)
                    resultado = cursor.fetchone()
                    if resultado:
                        ##si existe el auto, instancio el objeto llamando al metodo pagarEstacionamiento
                        auto = clases.Auto(resultado[0], resultado[1],resultado[2],resultado[3],resultado[4])
                        auto.pagarEstacionamiento()
                        opcion = input(" \n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                    else:
                        print("no se encontro ningun auto")
                        opcion = input(" \n 0. Volver al menú \n")
                        funciones.volverMenu(opcion)
                funciones.borrarPantalla()            
                print ("Menu admin: \n")
                print(" 1. Modificar fecha de ingreso o egreso de un auto \n 2. Buscar una patente \n 3. Agregar patente \n 4. Pagar estacionamiento \n 5. Salir")
                opcion = int(input("Opcion: "))