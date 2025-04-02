from Pathlib import Path

# Metodo para poder abrir carpetas desde cualquier sistema operativo usando el objeto "PATH"
carpeta = Path('C:/Users/el_vi/Desktop/Cursos Udemy/CursoPython/Documentos/6')/  'Pruebalejana.txt'
# dos formas de hacerlo separando el archivo por variable o incluyendola en la variable carpeta con un "/"
"""archivo = carpeta /  'Pruebalejana.txt'"""

"""mi_archivo = open(archivo)"""

mi_archivo = open(carpeta)
print(mi_archivo.read())



