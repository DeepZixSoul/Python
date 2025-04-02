from collections import Counter
import os
import re
import timeit
import math
from datetime import datetime, date
from pathlib import Path


#ruta = 'C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\Practicas\\pythonProject1\\dia9\\Mi_Gran_Directorio'
"""funcion para abrir carpetas"""

ruta = Path('C:/Users/el_vi/Desktop/Cursos Udemy/Practicas/pythonProject1/dia9/Mi_Gran_Directorio')
patron = r'N\w{3}-\d{4}'



"""for txt in Path(guia).glob('**/*.txt'):
    print(txt)"""
#print(carpeta.read_text())

def busqueda_txt(ruta, patron):

    cuantos=''
    verificar = ''
    nombr_archivo = ''
    lista_verificar = []
    lista_nombre_archivo = []
    for txt in (ruta).glob('**/*.txt'):
        pathh_txt = txt
        #txt2 = open(txt, 'r')
        txt2 = Path(txt)
        txt1 = txt2.read_text()
        #txt1 = str(txt2.read())
        verificar = re.search(patron, txt1)
        #txt2.close()
        if verificar:
            nombr_archivo = pathh_txt.name
            lista_nombre_archivo.append(nombr_archivo)
            verificar = verificar.group()
            # devolver una lista
            lista_verificar.append(verificar)
    
    return lista_verificar,lista_nombre_archivo

print(busqueda_txt(ruta,patron))

a ,b = busqueda_txt(ruta,patron)
print(a)
print(b)

for serie in a :
    print(serie)

lista1 = ["Hola"]
lista2 = ["Mundo"]

# Ajusta la longitud del espacio entre las palabras para alinearlas correctamente
longitud_espacio = 10

# Imprime los elementos de las listas tabulados
print(lista1[0] + " " * (longitud_espacio - len(lista1[0])) + lista2[0])

"""ruta2 = 'C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\Practicas\\pythonProject1\\dia9\\Extraccion\\Mi_Gran_Directorio\\Directorio_3\\Directorio_3C\\archivo28.txt'

mi_archivo = open(ruta2, 'r')

print(mi_archivo.read()) 

mi_archivo.close()"""




"""def busqueda_txt(ruta):

    lista_txt =[]
    for carpeta, subcarpeta, archivo in os.walk(ruta):

        for arc in archivo:
            lista_txt.append(arc)

    return lista_txt



coincidencias = busqueda_txt(ruta)
print(coincidencias)


def iterador_d(ssss):
    for i in coincidencias:
        archivo = i
        yield archivo

algo = next(iterador_d(coincidencias))


print(algo)"""