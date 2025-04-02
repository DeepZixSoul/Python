# Para poder leerlo primero hay que cerrar el modo escritura
"""mi_archivo = open('texto.txt', 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('texto.txt', 'r')
print(mi_archivo.read())
mi_archivo.close()"""
# Añadir una nueva linea
"""mi_archivo = open('texto.txt', 'a')
mi_archivo.write('\nNuevo inicio de sesión')
mi_archivo.close()
mi_archivo = open('texto.txt', 'r')
print(mi_archivo.read())
mi_archivo.close()"""

# Añadir una nueva linea con una lista de strings concatenada con tabudalor \t

mi_archivo = open('texto.txt', 'a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for p in registro_ultima_sesion:
    mi_archivo.writelines(p + '\t')

mi_archivo.close()
mi_archivo = open('texto.txt', 'r')
print(mi_archivo.read())
mi_archivo.close()
