from datetime import datetime

import psycopg2
import colorama
from colorama import Fore, Style, Back  # cambia el menu de color
import contactoPersonal
from Contacto import *
from ContactoProfesional import ContactoProfesional
from contactoPersonal import ContactoPersonal

# Inicializar colorama
colorama.init()

# Conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    user='postgres',
    host="127.0.0.1",
    port="5432",
    database="agenda.db",
    password="admin"
)

cursor = conexion.cursor()

conexion.commit()

#Menu principal
# Función para mostrar el menú principal
def mostrar_menu():
    print(Fore.MAGENTA+ Back.BLACK +"=== Agenda de Contactos ===" + Style.RESET_ALL)
    print(Fore.CYAN+"1. Agregar contacto"+ Style.RESET_ALL)
    print(Fore.CYAN+"2. Eliminar contacto"+ Style.RESET_ALL)
    print(Fore.CYAN+"3. Modificar contacto"+ Style.RESET_ALL)
    print(Fore.CYAN+"4. Agregar evento"+ Style.RESET_ALL)
    print(Fore.CYAN+"5. Visualizar eventos por fecha"+ Style.RESET_ALL)
    print(Fore.CYAN+"6. Eliminar evento" + Style.RESET_ALL)
    print(Fore.CYAN+"7. Buscar contacto por nombre"+ Style.RESET_ALL)
    print(Fore.CYAN+"8. Mostrar lista de contactos"+ Style.RESET_ALL)
    print(Fore.CYAN+"9. Salir"+ Style.RESET_ALL)
# Emmanuel Sbona
def agregar_contacto2(Contacto2):
    cursor.execute('''
        INSERT INTO contactop (nombre, telefono, empresa, cargo,edad,correo,  whatsapp, facebook, instagram)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    ''', [Contacto2.getnombre, Contacto2.gettelefono, Contacto2.getempresa, Contacto2.getcargo, Contacto2.getedad,
          Contacto2.getcorreo, Contacto2.getwhatsapp, Contacto2.getfacebook, Contacto2.getwhatsapp])
    ContactoProfesional.id = cursor.fetchone()[0]
    conexion.commit()
    print("Contacto agregado exitosamente.")


# Función para eliminar un contacto de la base de datos
def eliminar_contacto():
    try:
        tabla = None
        while tabla not in ["1", "2"]:
            tabla = input("Ingrese el número de tabla en la que desea eliminar el contacto:\n1. ContactoPersonal\n2. ContactoProfesional\n")
            if tabla not in ["1", "2"]:
                print("Opción no válida. Por favor, ingrese 1 o 2.")
        tabla = int(tabla)
        contacto_id = None
        while not isinstance(contacto_id, int):
            try:
                contacto_id = int(input("Ingrese el ID del contacto a eliminar: "))
            except ValueError:
                print("ID no válido. Por favor, ingrese un número entero.")
        with conexion:
            with conexion.cursor() as cursor:
                if tabla == 1:
                    cursor.execute('DELETE FROM contactos WHERE id = %s', (contacto_id,))
                    print("Contacto eliminado exitosamente de la tabla contactos.")
                elif tabla == 2:
                    cursor.execute('DELETE FROM contactop WHERE id = %s', (contacto_id,))
                    print("Contacto eliminado exitosamente de la tabla contactop.")
                else:
                    print("Tabla no válida. No se pudo eliminar el contacto.")
                conexion.commit()
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        if cursor is not None:
            cursor.close()


# Función para modificar un contacto en la base de datos
def modificar_contacto(contacto_id, nombre, telefono, empresa, cargo, whatsapp, facebook, instagram):
    cursor.execute('''
        UPDATE contactos
        SET nombre = %s, telefono = %s, empresa = %s, cargo = %s,  whatsapp = %s, facebook = %s, instagram = %s
        WHERE id = %s
    ''', (nombre, telefono, empresa, cargo,  whatsapp, facebook, instagram, contacto_id))
    conexion.commit()
    print("Contacto modificado exitosamente.")


# Función para agregar un evento a la base de datos
def agregar_evento(fecha, descripcion, contacto_id):
    cursor.execute('''
        INSERT INTO eventos (fecha, descripcion, contacto_id)
        VALUES (%s, %s, %s)
    ''', (fecha, descripcion, contacto_id))
    conexion.commit()
    print("Evento agregado exitosamente.")


# Función para visualizar eventos en una fecha determinada
def visualizar_eventos(fecha):
    cursor.execute('''
        SELECT contactos.nombre, eventos.descripcion
        FROM eventos
        INNER JOIN contactos ON eventos.contacto_id = contactos.id
        WHERE eventos.fecha = %s
    ''', (fecha,))
    eventos = cursor.fetchall()

    if len(eventos) > 0:
        print("Eventos para la fecha", fecha)
        for evento in eventos:
            print("Contacto:", evento[0])
            print("Descripción:", evento[1])
            print("---")
    else:
        print("No hay eventos para la fecha", fecha)

#funcion para borrar evento
def eliminar_evento_por_fecha(fecha):
    cursor.execute(" DELETE FROM eventos WHERE fecha = %s", (fecha,))
    conexion.commit()
    print("Evento eliminado exitosamente.")


# Función para buscar contactos por nombre
def buscar_contacto(nombre):
    cursor.execute("SELECT * FROM contactos WHERE nombre ILIKE %s", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    if len(resultados) > 0:
        print("Resultados de búsqueda:")
        for resultado in resultados:
            print(resultado)
    else:
        print(Fore.GREEN+"No se encontraron contactos con ese nombre."+Style.RESET_ALL)

# ACA PARTE SEBA
#
#

# Función para modificar un contacto en la base de datos
#Punto3
def modificar_contacto():
    try:
        tabla = None # definimos tabla
        while tabla not in ("1", "2"):
            tabla = input( #solicitamos al usuario que ingrese el número de la tabla en la que desea modificar el contacto
                "Ingrese el número de tabla en la que desea modificar el contacto:\n1. ContactoPersonal\n2. ContactoProfesional\n")
            if tabla not in ("1", "2"): #Si la entrada no es "1" o "2", se muestra un mensaje de error
                print("Opción no válida. Por favor, ingrese 1 o 2.") #mensaje de error
        tabla = int(tabla) #pasamos la variable tabla a un entero.para poder comparar los valore en el if .
        contacto_id = None
        while not isinstance(contacto_id, int):  # Esto se ejecutara mientras la condición sea verdadera, es decir,
            # mientras contacto_id no sea un entero isinstance verifica que contacto_id
            try:
                contacto_id = int(input("Ingrese el ID del contacto a modificar: "))
            except ValueError:
                print("ID INCORRECTO. Por favor,Intentelo nuevamente.")
        with conexion:
            with conexion.cursor() as cursor:
                if tabla == 1:
                    nombre = input("Ingrese el nuevo nombre: ")
                    telefono = input("Ingrese el nuevo teléfono: ")
                    empresa = input("Ingrese la nueva empresa: ")
                    cargo = input("Ingrese el nuevo cargo: ")
                    cursor.execute( 'UPDATE contactos SET nombre = %s, telefono = %s, empresa = %s, cargo = %s WHERE id = %s',
                        (nombre, telefono, empresa, cargo, contacto_id))
                    print("Contacto modificado exitosamente en la tabla contactos.")
                elif tabla == 2:
                    nombre = input("Ingrese el nuevo nombre: ")
                    telefono = input("Ingrese el nuevo teléfono: ")
                    empresa = input("Ingrese la nueva empresa: ")
                    cargo = input("Ingrese el nuevo cargo: ")
                    edad = input("Ingrese la nueva edad: ")
                    correo = input("Ingrese el nuevo correo: ")
                    whatsapp = input("Ingrese el nuevo número de WhatsApp: ")
                    facebook = input("Ingrese el nuevo nombre de Facebook: ")
                    instagram = input("Ingrese el nuevo nombre de Instagram: ")
                    cursor.execute( 'UPDATE contactop SET nombre = %s, telefono = %s, empresa = %s, cargo = %s, edad = %s, correo = %s, whatsapp = %s, facebook = %s, instagram = %s WHERE id = %s',
                        (nombre, telefono, empresa, cargo, edad, correo, whatsapp, facebook, instagram, contacto_id))
                    print("Contacto modificado exitosamente en la tabla contactop.")
                else:
                    print("Tabla no válida. No se pudo modificar el contacto.")
                conexion.commit()
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        if cursor is not None:
            cursor.close()

