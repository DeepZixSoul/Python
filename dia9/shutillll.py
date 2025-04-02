import shutil

# comprimir archivo
"""carpeta_origen = 'C:\\Users\\el_vi\\Desktop\\capetapeta'
# nombre para nueva carpeta
archivo_destion = 'capetapeta_comprimido'

shutil.make_archive(archivo_destion, 'zip', carpeta_origen)
"""
# podriamos añadir la ruta para llevarlo a un lugar especifico
shutil.unpack_archive('Proyecto+Dia+9.zip', 'Extraccion', 'zip')
