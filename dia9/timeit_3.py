import timeit
"""devulve una lista desde 1 hasta cualquier
numero que elija el usuario"""

declaracion = """
prueba_for(10)
"""

mi_setuo = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

"""

duracion = timeit.timeit(declaracion, mi_setuo, number=1000000)
print(duracion)


declaracion2 = """
prueba_while(10)
"""
# definicion de una funcion
mi_setuo2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

"""

duracion2 = timeit.timeit(declaracion2, mi_setuo2, number=1000000)
print(duracion2)


def calcular_suma(n):
    suma = 0
    s = []
    for i in range(n):
        suma += i
        s.append(i)
    return suma,s
print(calcular_suma(8))

tiempo = timeit.timeit('calcular_suma(1000)', setup='from __main__ import calcular_suma', number=100000)
print(f"Tiempo promedio de ejecución: {tiempo} segundos")