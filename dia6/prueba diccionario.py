mi_lista = ["a", "b", "c", "d", "e"]

# Crear un diccionario con índices como claves y elementos como valores
diccionario_resultante = {indice: elemento for indice, elemento in enumerate(mi_lista)}

# Mostrar el diccionario resultante
print(diccionario_resultante)