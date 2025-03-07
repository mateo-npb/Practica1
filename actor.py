# actor.py
class Actor:
    def __init__(self, nombre, edad, direccion, tipo_actor):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
        self.__tipo_actor = tipo_actor  # Puede ser 'Estudiante', 'Profesor', etc.

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_tipo_actor(self):
        return self.__tipo_actor

    def set_tipo_actor(self, tipo_actor):
        self.__tipo_actor = tipo_actor

    def __str__(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Dirección: {self.get_direccion()}, Tipo: {self.get_tipo_actor()}"
