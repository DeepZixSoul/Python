lista_numeros = [1,1,14,17,2,2,751,22,43,]

def reducir_lista(lista_numeros):
    lista_numeros = list(set(lista_numeros))
    numero_mas_alto = max(lista_numeros)
    lista_numeros.remove(numero_mas_alto)
    return lista_numeros

listra = reducir_lista(lista_numeros)

print(len(listra))

def promedio(lista):
    promedi = 0
    indice = len(lista)
    for nunmero in lista:

        promedi = promedi + nunmero
    return promedi / indice

print(promedio(listra))


"""
# Ejemplo de lista
mi_lista = [1, 5, 3, 8, 2]

# Encuentra el número más alto en la lista
numero_mas_alto = max(mi_lista)

# Elimina el número más alto de la lista
mi_lista.remove(numero_mas_alto)

print(mi_lista)
>>> """