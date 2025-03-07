# profesor.py
from actor import Actor

class Profesor(Actor):
    def __init__(self, nombre, edad, direccion, materia):
        super().__init__(nombre, edad, direccion, 'Profesor')
        self.__materia = materia

    def get_materia(self):
        return self.__materia
    
    def set_materia(self, materia):
        self.__materia = materia

    def __str__(self):
        return f"{super().__str__()}, Materia: {self.get_materia()}"
