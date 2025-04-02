mi_lista = ["a", "b", "c", "d", "e"]

# Crear un diccionario con índices como claves y elementos como valores
diccionario_resultante = {}
for indice, elemento in enumerate(mi_lista):
    diccionario_resultante[indice] = elemento

# Mostrar el diccionario resultante
print(diccionario_resultante)
print(diccionario_resultante.values(0))