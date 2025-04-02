"""def suma_cuadados (*args):
    total = 0

    for arg in args:
        total = total + arg ** 2
    return total



print(suma_cuadados(1,3,5,2,6))
numero = -5
valor_absoluto = abs(numero)

print("Número original:", numero)
print("Valor absoluto:", valor_absoluto)
"""

"""def suma_absolutos (*args):
    total = 0

    for arg in args:
        total += abs(arg)
    return total

print(suma_absolutos(2,4,5,6,71,2,-2,-15))


"""


def numeros_persona(nombre,*args):
    suma_numeros = 0

    for arg in args:
        suma_numeros += arg
        print(f"{nombre}, la suma de tus números es {suma_numeros}")

    return suma_numeros
nombre = "Diego"
print(numeros_persona(nombre,4,5,6,71,2,-2,-15))



def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'
