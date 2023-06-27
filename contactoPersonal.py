# Clase hija de Contacto para contactos personales
from Contacto import Contacto


class ContactoPersonal(Contacto):
    def __init__(self, id, nombre, telefono, empresa, cargo):
        super().__init__(id, nombre, telefono, empresa, cargo)


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Personal")

