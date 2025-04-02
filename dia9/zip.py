import zipfile
#genera carpeta y mete dos archivos comprimidos en ella
"""mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('texto_a.txt')
mi_zip.write('texto_b.txt')

mi_zip.close()"""

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()
