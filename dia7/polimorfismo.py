class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " Dice muuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " Dice beee")

vaca1 = Vaca('Juanita')
oveha1 = Oveja('Anastasia')

vaca1.hablar()
oveha1.hablar()

animales = [vaca1,oveha1]

for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveha1)

