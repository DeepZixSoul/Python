import time
"""devulve una lista desde 1 hasta cualquier
numero que elija el usuario"""


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final - inicio)

inicio2 = time.time()
prueba_while(1000000)
final2 = time.time()

print(final2 - inicio2)

