""""""


"""def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num


generador = secuencia_infinita()"""
"""def secuencia_infinita():
    num = 0
    while True:
        num += 1

        yield num * 7


generador = secuencia_infinita()"""


"""def mi_generador():
    for x in range(1, 5):
        y = x - 1

        if y != 0:
            z = print("Te quedan" + str(y) + "vidas")

            yield z
"""
"""def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()"""
def secuencia_infinita():
    num = 0
    while True:
        num += 1

        yield num * 7


generador = secuencia_infinita()

print(f"Te quedan {next(generador)} vidas")
print(f"Te quedan {next(generador)} vidas")
