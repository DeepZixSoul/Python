
# Generadores de turnos

# Texto funciones con funcionalidad


def contador_farmacia():
    num = 0
    while True:
        num += 1
        yield num
#turno_farmacia = contador_farmacia()

def contador_cosmeticos():
    num = 0
    while True:
        num += 1
        yield num

#turno_cosmeticos = contador_cosmeticos()
def contador_perfumeria():
    num = 0
    while True:
        num += 1
        yield num
#turno_perfumeria = contador_perfumeria()

"""def contador_turnos(lugar):
    letra = ''
    if lugar == turno_cosmeticos:
        letra = 'C-'
    elif lugar == turno_perfumeria:
        letra = 'P-'
    else:
        letra = 'F-'
    return print(f"******** {letra}{next(lugar)} ********")"""

def decorar_saludo(funcion):


    def otra_funcion(palabra):

        print('Su turno es el número:')
        funcion(palabra)
        print('  Por favor, espere  ')
    # Los return de funciones no necesitan parentesis
    return otra_funcion



"""tu_puta_madre = decorar_saludo(contador_turnos)

tu_puta_madre(turno_cosmeticos)
tu_puta_madre(turno_cosmeticos)

tu_puta_madre(turno_perfumeria)
tu_puta_madre(turno_perfumeria)

tu_puta_madre(turno_farmacia)
tu_puta_madre(turno_farmacia)
"""