import os
# ruta = os.getcwd() (esta ruta)
# abrir una ruta distinta usando el metodo "chdir" de "os"

"""ruta = os.chdir('C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\CursoPython\\Documentos\\6')
archivo = open('Pruebalejana.txt')
print(archivo.read())"""
#Crear carpeta distinta (makedirs)


"""ruta = os.makedirs('C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\CursoPython\\Documentos\\6\\otra')"""
#
"""ruta = 'C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\Practicas\\pythonProject1\\dia6\\Prueba3.txt'
"""
"""#nombre base del elemento elemnto= os.path.basename(ruta)
elemnto = os.path.dirname(ruta)
print(elemnto)

# Recibir ambos elementos separados en una tupla
elemnto = os.path.split(ruta)
print(elemnto)
"""
"""#Eliminar directorio(carpetas)
os.rmdir('C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\CursoPython\\Documentos\\6\\otra')
"""
#leer archivo sin los metodos de "os"
otro_archivo = open('C:\\Users\\el_vi\\Desktop\\Cursos Udemy\\CursoPython\\Documentos\\6\\Pruebalejana.txt')
print(otro_archivo.read())