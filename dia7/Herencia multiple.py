class Padre:
    def hablar(self):
        print("Hola")
class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("que tal")

# Hereda primero padre por posicion
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()

#Metodo  de clase para ver orden de herencia
print(Nieto.__mro__)


# Ejercicio 1
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre, Padre):
    pass

# Ejercicio 2
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Reptil,Pez,Ave,Mamifero):
    pass