class Pajaro:
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print(f"¡pío!, Mi color es {self.color}")
    def volar(self, metros):
        print(f"El pajaor voló {metros} metros.")
piola = Pajaro('Negro', 'Culiado')
piola.piar()
piola.volar(50)

#ejercicio 2
"""class Mago():
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()

merlin.lanzar_hechizo()"""

#ejercicio 3
"""Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"""

"""class Alarma():

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

"""