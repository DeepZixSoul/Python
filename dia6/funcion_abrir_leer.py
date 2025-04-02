
"""def abrir_leer(texto):
    texto = open('')

    print(texto.read())

    texto.close()

abrir_leer()"""


def abrir_leer(texto):
    texto = open(texto,'r')

    return texto.read()

print(abrir_leer('texto.txt'))

# Función para escribir
""""def sobrescribir(texto):
    texto = open(texto,'w')
    texto = texto.write("contenido eliminado")
    return texto"""

#

