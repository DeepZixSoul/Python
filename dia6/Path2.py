from pathlib import Path
# Metodo para saber direccion de este ordenador
base = Path.home()
# Contaquetnación de Path para una ruta "RELATIVA" no existe
guia = Path(base,"Europa", "España", Path("Murcia", "Limones.txt"))
#Devuelve un Path nuevo con el nombre del archivo indicado
guia2 = guia.with_name("Pelotas.txt")
print(base)
print(guia)
print(guia2)
#Parent devuelve la carpeta anterior desde el final
print(guia.parent)
print(guia.parent.parent)
guia.parents