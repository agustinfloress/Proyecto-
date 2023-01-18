import main
import os
def borrarPantalla():
    ##borra la pantalla de la terminal para todos los sistemas operativos posibles
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def opcionFecha(opcion,patente):
    ##para modificar la fecha de ingreso o egreso de un auto
    if opcion == 1:
       fecha = input("Ingrese fecha de ingreso actualizada: ")
       parametros = (fecha,patente)
       cursor= main.conn.cursor()
       update_movimiento= "update movimientos set fecha_ingreso= ? where patente = ?;"
       cursor.execute(update_movimiento, parametros)
       main.conn.commit()
    elif opcion == 2:
       fecha = input("Ingrese fecha de egreso actualizada: ")
       parametros = (fecha,patente)
       cursor= main.conn.cursor()
       update_movimiento= "update movimientos set fecha_egreso= ? where patente = ?;"
       cursor.execute(update_movimiento, parametros)
       main.conn.commit()


def volverMenu(opcion):
    ##vuelve al menú
    if opcion == 0:
        pass