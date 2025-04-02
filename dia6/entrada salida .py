mi_archivo = open('Prueba.txt')
#aplica metodos string
"""una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)

print( mi_archivo.read())
"""

"""
for l in mi_archivo:
    print("Aqui dice : " + l)"""

# Metodos de lista para las linease
todas = mi_archivo.readlines()
pop = todas.pop()
print(todas)



mi_archivo.close()