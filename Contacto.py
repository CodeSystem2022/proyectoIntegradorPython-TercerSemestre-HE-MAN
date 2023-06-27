# Clase Padre para contactos
class Contacto:
    def __init__(self,id, nombre, telefono, empresa, cargo):
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
        self._empresa = empresa
        self._cargo = cargo


    def mostrar_informacion(self):
        print("ID:",self._id)
        print("nombre:", self._nombre)
        print("telefono:", self._telefono)
        print("empresa:", self._empresa)
        print("cargo:", self._cargo)


# Getters y Setters
    @property
    def getid(self):
        return self._id

    @getid.setter
    def set_id(self, id):
       self._id = id
    @property
    def getnombre(self):
      return self._nombre

    @getnombre.setter
    def setnombre(self, nombre):
       self._nombre = nombre

    @property
    def gettelefono(self):
     return self._telefono

     @gettelefono.setter
     def settelefono(self, telefono):
         self._telefono = telefono



    @property
    def getempresa(self):
     return self._empresa

    @getempresa.setter
    def set_empresa(self, empresa):
     self._empresa = empresa

    @property
    def getcargo(self):
     return self._cargo

    @getcargo.setter
    def set_cargo(self, cargo):
       self._cargo = cargo



