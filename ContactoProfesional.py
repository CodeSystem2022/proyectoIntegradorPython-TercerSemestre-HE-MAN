# Clase hija de Contacto para contactos profesionales
from Contacto import Contacto


class ContactoProfesional(Contacto):
    def __init__(self,id,nombre, telefono, empresa, cargo, edad, correo, whatsapp, facebook, instagram):
        super().__init__(id, nombre, telefono, empresa, cargo)
        self._edad = edad
        self._correo = correo
        self._whatsapp = whatsapp
        self._facebook = facebook
        self._instagram = instagram


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Edad:", self._edad)
        print("Correo:", self._correo)
        print("whatsapp:", self._whatsapp)
        print("facebook:", self._facebook)
        print("instagram:", self._instagram)
        print("Tipo: Profesional")


    @property
    def getedad(self):
        return self._edad

    @getedad.setter
    def set_edad(self, edad):
        self._edad = edad

    @property
    def getcorreo(self):
        return self._correo

    @getcorreo.setter
    def set_correo(self,correo):
        self._correo = correo

    @property
    def getid(self):
        return self._id

    @getid.setter
    def set_id(self, id):
        self._id = id

    @property
    def getwhatsapp(self):
        return self._whatsapp

    @getcorreo.setter
    def set_whatsapp(self, whatsapp):
        self._whatsapp = whatsapp

    @property
    def getfacebook(self):
        return self._facebook

    @getcorreo.setter
    def set_facebook(self, facebook):
        self._facebook = facebook

    @property
    def getinstagram(self):
        return self._instagram

    @getinstagram.setter
    def set_instagram(self, instagram):
        self._instagram = instagram


