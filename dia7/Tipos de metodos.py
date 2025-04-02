class Pajaro:
    #Argumento clase
    alas = True
    #Metodos de instancia
    #Metedo de instancia para añadir un atributo de instancia
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print(f"¡pío!, Mi color es {self.color}")
    def volar(self, metros):
        print(f"El pajaor voló {metros} metros.")

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el paharo")

# Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f" Puso {cantidad} huevos")
        # No se puede accdere a los metodos de instancia
        #print(f" Es de color{self.color}")
        # Si se puede accecer a los argumentos de clase
        cls.alas = False
        print(Pajaro.alas)
# Metodos estaticos
    @staticmethod
    def mirar():
        # No puede acceder a las instacians
        # No puede acceder a los atributos de las clases
        print("El pajaro mira")

Pajaro.mirar()

"""piola = Pajaro('Negro', 'Culiado')
piola.piar()
piola.volar(50)
piola.alas = False
print(piola.alas)"""
#Metodo de clase
Pajaro.poner_huevos(3)

#Pajaro.piar()
# Ejericio 1
"""class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
"""
# Ejericio 2

"""class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        Jugador.vivo = True"""

