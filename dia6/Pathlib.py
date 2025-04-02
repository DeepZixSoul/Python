from pathlib import Path, PureWindowsPath

# Metodo para poder abrir carpetas desde cualquier sistema operativo usando el objeto "PATH"
carpeta = Path('C:/Users/el_vi/Desktop/Cursos Udemy/CursoPython/Documentos/6')/  'Pruebalejana.txt'
# dos formas de hacerlo separando el archivo por variable o incluyendola en la variable carpeta con un "/"
"""archivo = carpeta /  'Pruebalejana.txt'"""
print(carpeta)
# Cualquier ruta que quieras la transforma en un ruta de windows
ruta_windows= PureWindowsPath(carpeta)
print(ruta_windows)

# Metodo distinto para leer archivos. No necesitamos abrir y cerrar archivos
print(carpeta.read_text())

# Imprime el nombre del archivo
print(carpeta.name)

# Imprime que tipo(extension".txt, por ejemplo) de archivo es
print(carpeta.suffix)

# Imprime el nobre del archivo sin el formato
print(carpeta.stem)

# Saber si el archivo existe
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Existe!!")
