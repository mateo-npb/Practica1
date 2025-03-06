# administrador.py
from actor import Actor

class Administrador(Actor):
    def __init__(self, nombre, edad, direccion, rol):
        super().__init__(nombre, edad, direccion, 'Administrador')
        self.__rol = rol

    def get_rol(self):
        return self.__rol
    
    def set_rol(self, rol):
        self.__rol = rol

    def __str__(self):
        return f"{super().__str__()}, Rol: {self.get_rol()}"
