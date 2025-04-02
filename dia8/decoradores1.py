"""funcion que recibe una funcion"""


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    # Los return de funciones no necesitan parentesis
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


# De eta forma se decoraría una función para poder
# "activa" o "desactivar" el decorador deseado
mayusculas_decorada = decorar_saludo(mayusculas)


# Utilizamos variable de función decorada
mayusculas_decorada('diego')
