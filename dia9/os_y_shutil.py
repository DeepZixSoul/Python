import os
import shutil
import send2trash
# crear un archivo
"""archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())"""
#mover archivo
#shutil.move('curso.txt', 'c:\\Users\\el_vi\\Desktop')
#borrar archivo
"""os.unlink()"""
#borrar carpeta vacía
"""os.rmdir()"""
#borrar carpeta y su contenido, desaparecen
"""shutil.rmtree"""
#alternativa para eliminar algo y llevarlo a la papelera
"""send2trash.send2trash('curso.txt')"""
#almacenar ruta actual y subcarpetas, y archivos en ese orden


ruta = 'C:\\Users\\el_vi\\Desktop\\capetapeta'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arc in archivo:
        if arc.startswith('2015'):
            print(f'\t{arc}')
    print('\n')