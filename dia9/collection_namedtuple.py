from collections import namedtuple
#funcionamiento normal
mi_tupla = (500, 18, 65)
print(mi_tupla[1])
# se crea un objeto
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.32, 76)

print(ariel.altura)
# Tambien recibe indces
print(ariel[2])

