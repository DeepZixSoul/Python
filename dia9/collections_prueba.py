from collections import deque

from collections import defaultdict


#lista_ciudades =  ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.appendleft('Cordoba')
print(lista_ciudades)