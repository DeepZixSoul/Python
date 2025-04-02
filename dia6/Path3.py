from pathlib import Path
# Para ver los directorios en Europa sin entrar a los demas directorios
guia = Path(Path.home(),"Europa")

# Ver los txt de Europa no sirve si hay carpetas dentro de Europa
for txt in Path(guia).glob('*.txt'):
    print(txt)
# Para ver todos los txt en los directorios de europa
for txt in Path(guia).glob('**/*.txt'):
    print(txt)
# Para ver rutas desde puntos en particular

guai2 = Path("Europa", "España", "Barcelona","Sagrada familia.txt")
en_europa = guai2.relative_to(Path("Europa"))
en_espania = guai2.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)
