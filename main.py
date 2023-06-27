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


