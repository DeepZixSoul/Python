from collections import Counter
import os
import re
import timeit
import math
from datetime import datetime, date
from pathlib import Path
import time

ruta = Path('C:/Users/el_vi/Desktop/Cursos Udemy/Practicas/pythonProject1/dia9/Mi_Gran_Directorio')
patron = r'N\w{3}-\d{4}'
dia_hoy = datetime.today()
dia_hoy = dia_hoy.strftime("%d/%m/%Y")
inicio = time.time()
def busqueda_ruta_txt(ruta):

    lista_txt =[]
    for carpeta, subcarpeta, archivo in os.walk(ruta):

        #for sub in subcarpeta:

        for arc in archivo:
            lista_txt.append(arc)

    return lista_txt


coincidencias = busqueda_ruta_txt(ruta)
print(coincidencias)

declaracion2 = timeit


def busqueda_txt(ruta, patron):
    cuantos = ''
    verificar = ''
    nombr_archivo = ''
    lista_verificar = []
    lista_nombre_archivo = []
    for txt in (ruta).glob('**/*.txt'):
        pathh_txt = txt
        # txt2 = open(txt, 'r')
        txt2 = Path(txt)
        txt1 = txt2.read_text()
        # txt1 = str(txt2.read())
        verificar = re.search(patron, txt1)
        # txt2.close()
        if verificar:
            nombr_archivo = pathh_txt.name
            lista_nombre_archivo.append(nombr_archivo)
            verificar = verificar.group()
            # devolver una lista
            lista_verificar.append(verificar)

    return lista_verificar, lista_nombre_archivo



busqueda_txt(ruta,patron)
final = time.time()

tiempo_programa = final - inicio
tiempo_programa = math.ceil(tiempo_programa)


""" Duración de busqueda """


def _impresion(tiempo, funcion, tiempo_programa):
    numero_serie, nombre_archivo = funcion
    cantidadad_numeros_serie = len(numero_serie)
    longitud_maxima = max(max(len(x) for x in numero_serie), max(len(x) for x in nombre_archivo))
    print("----------------------------------------------------")
    print(f"Fecha de búsqueda: {tiempo_programa}\n")
    print(f"\tARCHIVO:\t\t\t\tNRO.SERIE:\n")
    for archivo, seria in zip(nombre_archivo, numero_serie):
        print("\t" + archivo.ljust(longitud_maxima) + "\t\t\t" + seria)
    print(f"\n\t-------------\t\t    ----------\n"
          
          f"\nNúmeros de serie encontras: {cantidadad_numeros_serie}."
          f"\nDuración de busqueda: {tiempo} segundos.")
    print("----------------------------------------------------")


_impresion(tiempo_programa,busqueda_txt(ruta, patron), dia_hoy )





""" Función para imprimir a la hora que se hizo la consulta"""



"""numeros = [8,3,3,2,1,5,6,6,7,2,8,9,1,2,3,4,3]
print(Counter(numeros))

print(Counter("mississippi"))"""