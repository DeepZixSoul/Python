from random import shuffle

# Lista inicial

palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista
# Comprobar palitos
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)
# Comprobar intentos
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos!")
    else:
        print("Te salvaste wey")
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)

seleccion = probar_suerte()

chequear_intento(palitos_mezclados, seleccion)



