"""Turno para una farmacia"""
import proyecto8_numeros
from os import system

turno_farmacia1 = proyecto8_numeros.contador_farmacia()
turno_perfumeria1 = proyecto8_numeros.contador_perfumeria()
turno_cosmeticos1 = proyecto8_numeros.contador_cosmeticos()

"Funcion para el menú de inicio"


def inicio():

    print('*' * 50)
    print('*' * 5 + " Bienvenido" + '*' * 5)
    print('*' * 50)
    print('\n')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):

        print("Elija su cita:")
        print('''
        [1] - Farmacia
        [2] - Cosmeticos
        [3] - Perfumería
        [4] - Sacar otro turno        
        [5] - Salir del programa''')
        eleccion_menu = input()

    system('cls')

    return int(eleccion_menu)


"""Función para contar turnos"""


def contador_turnos(lugar):

    letra = ''
    if lugar == turno_cosmeticos1:
        letra = 'C-'
    elif lugar == turno_perfumeria1:
        letra = 'P-'
    elif lugar == turno_farmacia1:
        letra = 'F-'
    return print(f"******** {letra}{next(lugar)} ********")


turno_decorado = proyecto8_numeros.decorar_saludo(contador_turnos)
finalizar_programa = False


while not finalizar_programa:

    menu = inicio()
    volver = ''

    if menu == 1:
        system('cls')
        turno_decorado(turno_cosmeticos1)
        volver = input("Pulse enter para volver al menú")

    elif menu == 2:
        turno_decorado(turno_perfumeria1)
        volver = input("Pulse enter para volver al menú")

    elif menu == 3:
        turno_decorado(turno_farmacia1)
        volver = input("Pulse enter para volver al menú")

    elif menu == 4:
        volver = input("Pulse enter para volver al menú")

        pass
    elif menu == 5:
        finalizar_programa = True
