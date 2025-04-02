from random import *
eureka = randint(1, 100)


nombre = input("Ingresa tu nombre: ")
print(f"\nBuenas {nombre} tengo un número mágico entre el 1 y 100 tienes 8 intentos para adivinarlo!\n")

intento = 1
contador = 1
numero = 0

while contador <= 8 or numero != eureka:
    numero = input(f"¡Este es tu {contador} intento!\n\nIngresa tu numero: ")
    numero = int(numero)

    if numero < 1 or numero > 100:
        print("\n¡¡¿NO ENTIENDES CUANDO TE HABLO?!! TÚ NÚERO TIENE QUE SER DEL 1 AL 100 \n")
        contador += 1
        continue
    elif contador == 8:
        print("¡TU EXISTENCIA NO MERECE UNA RESPUESTA! ")
        break
    elif numero < eureka :
        print("\n¿Estás cerca o lejos? ¡No te lo diré! Aunque me das pena.¡TU NÚMERO ES MENOR QUE EL NÚMERO MÁGICO!\n")
        contador += 1
        continue
    elif numero > eureka :
        print("\n¿Estás cerca o lejos? ¡Vuelve a buscar entre tus pocas neuronas! Eres un insulto."
              "¡TU NÚMERO ES MAYOR QUE EL NÚMERO MÁGICO!\n")
        contador += 1
        continue
    elif numero == eureka:
        if contador == 1:
            print(f"\n¿?¿?¿?¿?¡DIOS! ¿Estás ahí? Solo tú puedes saber este número. ¡Dime el sentido de la vida por favor!\n"
                  f"¡En solo {contador} intento! Solo una divinidad podría lograrlo....")
        else:
            print(
                f"\n¿?¿?¿?¿?¡DIOS! ¿Estás ahí? Solo tú puedes saber este número. ¡Dime el sentido de la vida por favor!\n"
                f"¡En solo {contador} intentos! Solo una divinidad podría lograrlo....")
        break


""""

while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
    #monedas -= 1
    """

"""    else:
        print(f"¡¡IMBECIL ESTE ES TÚ {intento}º INTENTO!!\n"
              f"'Morirás si no consigues en {contador} intentos....delicious :P ")
        numero = input(f"Siguiente intento:")"""
