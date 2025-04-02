class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(selfs):
        print("Este animal ha nacido")

    def hablar(selfs):
        print("Este animal emite un sonido")
    pass

class Pajaro(Animal):
    # una forma de añadir un atributo de instancia
    """def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo"""
    # otra forma de añadir un atributo de instancia
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    def hablar(selfs):
        print("pio")
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")



piola = Pajaro(2, 'Amarillo', 300)

mi_animal = Animal(3,'rojo')



piola.nacer()
piola.hablar()
piola.volar(100)


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"