#'r' para solo lectura 'w' escritura borrando todo el archivo y empezando de 0
#'a' para escribir desde la ultima línea de un archivo sin borrar

mi_archivo = open('Prueba1.txt', 'a')

mi_archivo.write('Bienvenido')

mi_archivo.close()


#Pasar una lista de strings(no escribe lineas distintas)
"""mi_archivo.writelines(['hola','mundo','aqui','estoy'])"""
# Para escribir lineas seaparadas
"""
mi_archivo = open('Prueba1.txt', 'w')
lista = ['hola','mundo','aqui','estoy']

for p in lista:
    mi_archivo.writelines(p + '\n')"""

"""mi_archivo.write('''hola 
mundo
aqui
estoy''')"""


"""mi_archivo.write('hola\n')
mi_archivo.write('mundo')"""

"""def registro_error(texto):
    texto = open(texto,'a')
    texto = texto.write("se ha registrado un error de ejecución")
    return texto"""
