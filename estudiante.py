# estudiante.py
from actor import Actor

class Estudiante(Actor):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion, 'Estudiante')
        self.__curso = curso

    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        self.__curso = curso

    def __str__(self):
        return f"{super().__str__()}, Curso: {self.get_curso()}"
