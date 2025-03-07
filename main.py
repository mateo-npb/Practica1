# main.py
from estudiante import Estudiante
from profesor import Profesor
from administrador import Administrador

# Listas para almacenar los actores
list_estudiantes = []
list_profesores = []
list_administradores = []

def registrar_estudiante():
    print('Se va a registrar un estudiante')
    nombre = input('Ingresar el nombre: ')
    direccion = input('Ingresar la dirección: ')
    edad = input('Ingresar la edad: ')
    curso = input('Ingresar el curso: ')

    estudiante = Estudiante(nombre, edad, direccion, curso)
    list_estudiantes.append(estudiante)
    print('Estudiante guardado con éxito')

def registrar_profesor():
    print('Se va a registrar un profesor')
    nombre = input('Ingresar el nombre: ')
    direccion = input('Ingresar la dirección: ')
    edad = input('Ingresar la edad: ')
    materia = input('Ingresar la materia: ')

    profesor = Profesor(nombre, edad, direccion, materia)
    list_profesores.append(profesor)
    print('Profesor guardado con éxito')

def registrar_administrador():
    print('Se va a registrar un administrador')
    nombre = input('Ingresar el nombre: ')
    direccion = input('Ingresar la dirección: ')
    edad = input('Ingresar la edad: ')
    rol = input('Ingresar el rol: ')

    administrador = Administrador(nombre, edad, direccion, rol)
    list_administradores.append(administrador)
    print('Administrador guardado con éxito')

def mostrar_estudiantes():
    if len(list_estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print('Listado de estudiantes registrados:')
        for estudiante in list_estudiantes:
            print(estudiante)

def mostrar_profesores():
    if len(list_profesores) == 0:
        print("No hay profesores registrados.")
    else:
        print('Listado de profesores registrados:')
        for profesor in list_profesores:
            print(profesor)

def mostrar_administradores():
    if len(list_administradores) == 0:
        print("No hay administradores registrados.")
    else:
        print('Listado de administradores registrados:')
        for administrador in list_administradores:
            print(administrador)

# Menú interactivo
while True:
    print('::: MENU :::')
    print("""
    1. Registrar Estudiante
    2. Registrar Profesor
    3. Registrar Administrador
    4. Consultar Listado de Estudiantes
    5. Consultar Listado de Profesores
    6. Consultar Listado de Administradores
    7. Salir
    """)
    opcion = input('Ingresa la opción que desees ejecutar: ')

    if opcion == '1':
        registrar_estudiante()
    elif opcion == '2':
        registrar_profesor()
    elif opcion == '3':
        registrar_administrador()
    elif opcion == '4':
        mostrar_estudiantes()
    elif opcion == '5':
        mostrar_profesores()
    elif opcion == '6':
        mostrar_administradores()
    elif opcion == '7':
        print('Saliendo del sistema.')
        break  # Termina el programa
    else:
        print('Opción inválida, intenta nuevamente.')
