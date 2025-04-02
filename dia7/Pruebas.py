
# Ejericio 3

"""class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas - 1

"""


#iterar un objeto específico
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
def iterador(objetos):
    for iterador in objetos:
        print(len(iterador))

iterador(lista)
# diferencia entre iterar una lista de objetos
for dato in [palabra, lista, tupla]:
    print(len(dato))


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


juan = Mago()

pepe = Arquero()

sandra = Samurai()

personajes = [pepe,juan,sandra]
for ataque in personajes:
    ataque.atacar()

