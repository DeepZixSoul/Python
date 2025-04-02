from  random import *

lista_palabras=["Diegoso","Sandrana","Amorcito","Katylinda","SauronJose","Dormilona","Chochazo"]
aleatorio = choice(lista_palabras)
aleatorio = aleatorio.lower()

def pedir_letra(incognita):
     palabra = ''
     palabra1 = ''

     for letra in aleatorio:
          letra1 = letra.replace(letra,"-")
          palabra1 += letra1
          palabra += letra # comprobar palabra


     return palabra1,palabra, print("Bienvenid@ al juego del ahoracado:\n")

def contador_vidas(nombre):

     vidas = 10

     print(f"Tienes {vidas} vidas\n")


     a, b, c = nombre

     print(f"La palabra tiene {a} letras\n")

     while vidas >= 0 or a != b :
          ingreso_letra = input("Ingresa una letra:")
          ingreso_letra = str(ingreso_letra)
          ingreso_letra = ingreso_letra.lower()
          c2 = ''
          vidas -= 1
          for indice,letra in enumerate(b):

               aleatorio1 = indice
               prueba = a[aleatorio1]
               prueba2 = b[aleatorio1]
               prueba = str(prueba)
               prueba2 = str(prueba2)

               if letra == ingreso_letra:

                    a = a[:aleatorio1] + prueba2 + a[aleatorio1 + 1:]
                    b = b[:aleatorio1] + prueba2 + b[aleatorio1 + 1:]
                    c2 = a[:aleatorio1] + prueba2 + a[aleatorio1 + 1:]
                    # papalabra += aleatorio2

                    # palabra para desemcriptar
          else:
               print(f"Intentalo de nuevo, te quedan {vidas} vidas.\n"
                     f"{a}")



          if vidas == 0:
               print(f"Te quedan {vidas} vidas, perdiste\n"
                     f"La palabra era: !{b}¡")
               break
          elif a == b:
               print(f"La pabra es: !{a}¡\n"
                     f"¡¡¡GANASTE!!!!!")
               break


contador_vidas(pedir_letra(aleatorio))

