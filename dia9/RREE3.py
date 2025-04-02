import re

"""clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)"""

texto = 'No atendemos los lunes porlatarde'
# busca= re.search(r'lunes|martes', texto)
# Añade tantos carecteres como puntos
# busca= re.search(r'....demos...', texto)

# "^" Busca al comienzo del string
busca = re.search(r'^\D', texto)
print(busca)

# "$" Busca al final del string
busca = re.search(r'\D$', texto)
print(busca)

# "[^]" Excluye los obejtos de busqueda-
# en este caso \s para excluir los espacios vacíos
# el '+' sirve para decir una o más veces cada vez que
# encuentra un espacio vacío corta el grupo
busca = re.findall(r'[^\s]+', texto)
print(busca)

print(''.join(busca))
