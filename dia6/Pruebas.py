
# abrir texto e imprimir su contenido

archivo_texto = open('texto.txt')
print(archivo_texto.read())

# abrir texto e imprimir la primera linea

archivo_texto = open('texto.txt')
print(archivo_texto.readline())

# abrir texto e imprimir la segunda linea

archivo_texto = open('texto.txt')
archivo_texto.readline()
print(archivo_texto.readline())

archivo_texto.close()




#cerrar texto
archivo_texto.close()
