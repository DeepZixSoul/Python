class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(selfs):
        print("Este animal ha nacido")
    pass

class Pajaro(Animal):
    pass

print(Pajaro.__bases__)
print(Animal.__subclasses__())

piola = Pajaro(2, 'Amarillo')
piola.nacer()
print(piola.color)

#Ejercicio 1

"""class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass"""
#Ejercicio 2
"""class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass"""

#Ejercicio 3

"""class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass
class Automovil(Vehiculo):
    pass"""