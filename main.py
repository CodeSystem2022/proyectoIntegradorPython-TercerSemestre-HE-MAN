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
# Función para mostrar el menú principal
def leer_opcion():
    while True:
        try:
            opcion = int(input(Fore.MAGENTA+ Back.BLACK +"Ingrese una opción: "+ Style.RESET_ALL))
            print("======================================")
            if opcion < 1 or opcion > 9:
                raise ValueError
            return opcion
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número del 1 al 9.")

# Función para leer una opción del segundo menú
def leer_opcion2():
    while True:
        try:
            OPC = int(input(Fore.MAGENTA+ Back.BLACK +"Ingrese una opción: "+ Style.RESET_ALL))
            print("======================================")
            if OPC < 1 or OPC > 4:
                raise ValueError
            return OPC
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")


# Función para agregar un contacto a la base de datos
#Punto1
def agregar_contacto(contacto):
    cursor.execute('''
        INSERT INTO contactos (nombre, telefono, empresa, cargo)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    ''', (contacto.getnombre, contacto.gettelefono, contacto.getempresa, contacto.getcargo))
    contactoPersonal.id = cursor.fetchone()[0]
    conexion.commit()
    print("Contacto agregado exitosamente.")
#Punto1
def agregar_contacto2(Contacto2):
    cursor.execute('''
        INSERT INTO contactop (nombre, telefono, empresa, cargo,edad,correo,  whatsapp, facebook, instagram)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    ''', [Contacto2.getnombre, Contacto2.gettelefono, Contacto2.getempresa, Contacto2.getcargo, Contacto2.getedad,
          Contacto2.getcorreo, Contacto2.getwhatsapp, Contacto2.getfacebook, Contacto2.getinstagram])
    ContactoProfesional.id = cursor.fetchone()[0]
    conexion.commit()
    print("Contacto agregado exitosamente.")
#Punto 1 EL submenu
#Funcion para que al crear un contacto SE PUEDAD ELEJIR ENTRE CPROFESIONAL O PERSONAL
def datos_menu_dos():
        menu2()
        OPC = leer_opcion2()

        if OPC == 1:
            nombre, telefono, empresa, cargo, edad, correo, whatsapp, facebook, instagram = pedir_Datos_Contacto_Profesional()
            contacto_profesional = ContactoProfesional(id,nombre, telefono, empresa, cargo, edad, correo, whatsapp,facebook, instagram)
            agregar_contacto2(contacto_profesional)
        elif OPC == 2:
             nombre, telefono, empresa, cargo = capturar_datos_contacto()
             Contacto_personal = ContactoPersonal(id,nombre, telefono, empresa, cargo )
             agregar_contacto(Contacto_personal)
            
        elif OPC == 3:
            ejecutar_agenda()
        
        else:
            print(Fore.RED+"LA OPCION QUE INGRESO ES INCORRECTA "+Style.RESET_ALL)
            print(Fore.RED+"Igrese nuevamente una opcion "+Style.RESET_ALL)
#Funcion para el segundo menu
def menu2 ():
    print(Fore.MAGENTA + Back.BLACK + "=====MENU_CONTACTO=====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Contacto Profesional" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Contacto Personal" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Salir" + Style.RESET_ALL)


# Función para capturar los datos de un contacto desde el usuario
def capturar_datos_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    empresa = input("Ingrese la empresa: ")
    cargo = input("Ingrese el cargo: ")
    return nombre, telefono, empresa, cargo
#Funcion para capturar los datos del segundo menu
def pedir_Datos_Contacto_Profesional():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    empresa = input("Ingrese la empresa: ")
    cargo = input("Ingrese el cargo: ")
    edad  = input("Ingrese su edad")
    correo = input("Ingrese su correo")
    whatsapp = input("Tiene  WhatsApp?: ")
    facebook = input("Ingrese el perfil de Facebook: ")
    instagram = input("Ingrese el perfil de Instagram: ")
    return nombre, telefono, empresa, cargo,edad,correo,whatsapp, facebook, instagram


# SEBA BARROS
# Función para eliminar un contacto de la base de datos usando transacciones
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

# Cala Fernando
# Punto 4
# Funcion para agregar un evento por fecha
def agregar_evento(fecha, descripcion):
    fecha = datetime.strptime(fecha, '%Y-%m-%d').date()  # se convierte la variable fecha de string a tipo date
    fecha_actual = datetime.now().date()
    if fecha < fecha_actual:  # condicion para que no se agregue una fecha pasada
        print("No se puede agregar un evento con una fecha pasada.")
        return
    cursor.execute('''
         INSERT INTO eventos (fecha, descripcion)
         VALUES (%s, %s)
     ''', (fecha, descripcion))
    conexion.commit()
    print("Evento agregado exitosamente.")


# Punto 4
# Función para capturar los datos de un evento desde el usuario   
def capturar_datos_evento():
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    descripcion = input("Ingrese la descripción del evento: ")
    return fecha, descripcion

#Fabio Javier Flores
#Punto 5
# Función para visualizar eventos en una fecha determinada
def visualizar_eventos(fecha):
    cursor.execute('''
        SELECT  eventos.descripcion
        FROM eventos
        WHERE eventos.fecha = %s
    ''', (fecha,))
    eventos = cursor.fetchall()

    if len(eventos) > 0:
        print("Eventos para la fecha", fecha)
        for evento in eventos:
            print("Descripción:", evento[0])
            print("---")
    else:
        print("No hay eventos para la fecha", fecha)

#Punto 6
#funcion para borrar evento
def eliminar_evento_por_fecha(fecha):
    cursor.execute(" DELETE FROM eventos WHERE fecha = %s", (fecha,))
    conexion.commit()
    print("Evento eliminado exitosamente.")

#Punto 7
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


#Punto 7
# Función para buscar contactos por nombre para la otra tabla
def buscar_contacto2(nombre):
    cursor.execute("SELECT * FROM contactop WHERE nombre ILIKE %s", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    if len(resultados) > 0:
        print("Resultados de búsqueda:")
        for resultado in resultados:
            print(resultado)
    else:
        print(Fore.GREEN+"No se encontraron contactos con ese nombre."+Style.RESET_ALL)

#Punto 8
# Función para mostrar la lista de contactos
def mostrar_lista_contactos():
    cursor.execute("SELECT * FROM contactos ORDER BY nombre ASC") # ejecuta una consulta SQL para seleccionar todos los registros de la tabla "contactos" y ordenarlos en orden ascendente según el campo "nombre"
    contactos = cursor.fetchall() #  recupera todos los resultados de la consulta ejecutada en la línea anterior y los almacena en la variable contactos
    if len(contactos) > 0: #  verifica si la longitud de la lista contactos es mayor que cero, es decir, si hay contactos en la lista.
        print(Fore.YELLOW + Back.BLACK + "Lista de contactos PERSONAL:" + Style.RESET_ALL)
        for contacto in contactos: # recorre cada elemento de la lista contactos # crea un objeto ContactoPersonal utilizando los valores de las columnas del registro actual.
            contacto_personal = ContactoPersonal(contacto[0],contacto[1], contacto[2], contacto[3], contacto[4])
            contacto_personal.mostrar_informacion()
            print("---") #  imprime una línea separadora después de mostrar la información de cada contacto.
    else: #Si no hay contactos en la lista, se ejecuta este bloque de código.
        print("No hay contactos en la agenda.") # imprime por pantalla el mensaje "No hay contactos en la agenda."

#Punto 8
def mostrar_lista_contactos2():
    cursor.execute("SELECT * FROM contactop ORDER BY nombre ASC") # ejecuta una consulta SQL para seleccionar todos los registros de la tabla "contactop" y ordenarlos en orden ascendente según el campo "nombre".
    contactop = cursor.fetchall() # recupera todos los resultados de la consulta ejecutada en la línea anterior y los almacena en la variable contactop
    if len(contactop) > 0: # verifica si la longitud de la lista contactop es mayor que cero, es decir, si hay contactos en la lista.
        print(Fore.YELLOW + Back.BLACK + "Lista de contactos PROFESIONAL:" + Style.RESET_ALL) # imprime por pantalla un encabezado utilizando la biblioteca colorama
        for contacto in contactop: #  inicia un bucle que recorre cada elemento de la lista contactop. En cada iteración, el elemento actual se asigna a la variable contacto.
            contacto_profesional = ContactoProfesional(contacto[0],contacto[1], contacto[2], contacto[3], contacto[4], contacto[5],contacto[6],contacto[7],contacto[8],contacto[9])
            contacto_profesional.mostrar_informacion()  # llama al método mostrar_informacion() del objeto contacto_profesional para imprimir la información del contacto en pantalla. 
            print("---")   # imprime una línea separadora después de mostrar la información de cada contacto.
    else: # Si no hay contactos en la lista, se ejecuta este bloque de código.
        print("No hay contactos en la agenda.")


# Función para ejecutar la agenda
def ejecutar_agenda():
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            datos_menu_dos()
        elif opcion == 2:
            eliminar_contacto()
        elif opcion == 3:
            modificar_contacto()
        elif opcion == 4:
            fecha, descripcion = capturar_datos_evento()
            cursor.execute('SELECT * FROM contactos')
            contactos = cursor.fetchall()
            agregar_evento(fecha, descripcion)

        elif opcion == 5:
            fecha = input("Ingrese la fecha a visualizar (YYYY-MM-DD): ")
            visualizar_eventos(fecha)
        elif opcion == 6:
            fecha = (input("Digite la fecha (YYYY-MM-DD) del evento a ELIMINAR"))
            eliminar_evento_por_fecha(fecha)
        elif opcion == 7:
                print(Fore.YELLOW + "1. Contacto Profesional" + Style.RESET_ALL)
                print(Fore.YELLOW + "2. Contacto Personal" + Style.RESET_ALL)
                print(Fore.YELLOW + "3. Volver al Menu Principal" + Style.RESET_ALL)
                tabla = input("Seleccione el tipo de CONTACTO")
                if tabla == "1":
                    nombre = input("Ingrese el nombre del contacto a buscar: ")
                    buscar_contacto2(nombre)
                elif tabla == "2":
                    nombre = input("Ingrese el nombre del contacto a buscar: ")
                    buscar_contacto(nombre)
                elif tabla == "3":
                    ejecutar_agenda()
                else:
                    print("seleccione una opcion CORRECTA")
        elif opcion == 8:
            mostrar_lista_contactos()
            mostrar_lista_contactos2()
        elif opcion == 9:
            break
    print("¡Hasta la proxima amigo!")
    conexion.close()
    


# Ejecutamos la agenda
ejecutar_agenda()
