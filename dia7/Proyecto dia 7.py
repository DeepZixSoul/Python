from random import randint
from os import system
class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = int(numero_cuenta)
        self.balance = int(balance)
    def imprimir(self):
        print(f"Nombre cliente: {self.nombre} {self.apellido}\n"
              f"Número de cuenta: ES {self.numero_cuenta}\n"
              f"Balance de cuenta: {self.balance}€")
    def depositar(self):
        dinero_depositar = input("¿Cuanto dinero quiere depositar?: ")
        self.balance = int(self.balance) + int(dinero_depositar)
        print(f"Usted depositó: {dinero_depositar}€\n"
              f"Ahora su cuenta tiene: {self.balance}€")

    def retirar(self):
        dinero_retirar = int(input("¿Cuanto dinero quiere retirar?: "))
        if dinero_retirar > self.balance:
            dinero_retirar = int(input("Ingrese un valor valido: "))
        self.balance = self.balance - dinero_retirar
        print(f"Usted retiró: {dinero_retirar}€\n"
              f"Ahora su cuenta tiene: {self.balance}€")

cliente1 = Cliente('Sandra', 'Prieto',456365234,500)

"""cliente1.imprimir()
cliente1.depositar()
cliente1.retirar()"""

"""codigo, depositar , retirar , salir
"""

def crear_cliente():
    print("Bienvenido a nuestro servicio, para poder crear su cuenta siga las siguientes instrucciones:")
    nombre_cliente = input("Escriba su numbre: ")
    apellido_cliente = input("Escriba su apellido: ")
    numero_cuenta = randint(50000000,90000000)
    print(f"Su número de cuenta es ES {numero_cuenta}!")
    balance_cuenta = input("¿Cuanto dinero desea ingresar?: ")
    #se puede hacer así también
    cliente3 = Cliente(nombre_cliente, apellido_cliente, numero_cuenta, balance_cuenta)
    return nombre_cliente, apellido_cliente, numero_cuenta, balance_cuenta

cliente2 = crear_cliente()
a,b,c,d = cliente2

cliente2 = Cliente(a,b,c,d)


def inicio():

    print('*' * 34)
    print('*' * 5 + " Bienvenido al Banquito " + '*' * 5)
    print('*' * 34)
    print('\n')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Menú")
        print('''
        [1] - Consultar cuenta
        [2] - Retirar dinero
        [3] - Depositar dinero
        [4] - Salir del menú
        ''')
        eleccion_menu = input("Elige una opcion:")

    return int(eleccion_menu)

finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        cliente2.imprimir()
        input("Pulse enter para volver:")
        system('cls')

    elif menu == 2:
        cliente2.retirar()
        input("Pulse enter para volver:")
        system('cls')

    elif menu == 3:
        cliente2.depositar()
        input("Pulse enter para volver:")
        system('cls')

    elif menu == 4:
        finalizar_programa = True
