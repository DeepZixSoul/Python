"""class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan')

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)
print(mi_pajaro.alas)"""

#ejercicio 1

"""class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
casa_blanca = Casa('blanco','4')"""

#ejercicio 2

"""Crea una clase llamada Cubo, 
y asígnale el atributo de clase:

caras = 6

y el atributo de instancia:

color

Crea una instancia cubo_rojo, 
de dicho color."""

"""class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo('rojo')"""

class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('Humano', 'True', '17')