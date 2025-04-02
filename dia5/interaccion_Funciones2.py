from random import randint

def lanzar_dados():

    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1 , dado2)

dados =lanzar_dados()

def evaluar_jugada(lista):


        if dado1 + dado2  <= 6 :
            print(f"La suma de los dados es {lista}. Lamentable")

        elif dado1 + dado2 > 6 and lista < 10:
            print(f"La suma de tus dadoses {lista}. Tienes buenas chances")
        elif dado1 + dado2 >= 10:
            print(f"La suma de tus dadoses {lista}. Parece una jugada ganadora")
        else:
            pass
evaluar_jugada(dados)

