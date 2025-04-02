
"""a = "-------"
b = "ediegoe"
ingreso_letra = input("Ingresa una letra:")
ingreso_letra = str(ingreso_letra)
papa = ''
while ingreso_letra in b:

    papa += ingreso_letra
    print(papa)"""

def encontrar_posiciones_caracter(string, caracter):
    posiciones = []

    for i, char in enumerate(string):
        if char == caracter:
            posiciones.append(i)

    return posiciones

# Ejemplo de uso
cadena = "programming"
caracter_a_buscar = "g"
posiciones = encontrar_posiciones_caracter(cadena, caracter_a_buscar)

if posiciones:
    print(f"En la cadena '{cadena}', el carácter '{caracter_a_buscar}' se encuentra en las posiciones: {posiciones}")
else:
    print(f"En la cadena '{cadena}', el carácter '{caracter_a_buscar}' no está presente.")


"""def contar_ocurrencias_caracter(string, caracter):
    contador = 0
    palabra =''
    lugar = []
    for char in string:
        if char == caracter:
            encontrar_lugar_en_string = string.find(caracter_a_contar)
            encontrar_lugar_en_string = str(encontrar_lugar_en_string)
            contador += 1
            palabra += caracter_a_contar
            lugar += encontrar_lugar_en_string


    return contador,print(palabra),print(encontrar_lugar_en_string),print(lugar)

# Ejemplo de uso
cadena = "programgming"
caracter_a_contar = "g"
ocurrencias = contar_ocurrencias_caracter(cadena, caracter_a_contar)

print(f"En la cadena '{cadena}', el carácter '{caracter_a_contar}' se repite {ocurrencias} veces.")"""

"""a = "-------"
b = "ediegoe"
vidas = 10
while vidas >= 0 :
  ingreso_letra = input("Ingresa una letra:")
  ingreso_letra = str(ingreso_letra)
  papa = ''

  if ingreso_letra in b:
       c2 = ''
       papalabra = ''
       papalabra += ingreso_letra
       aleatorio1 = b.find(ingreso_letra)
       prueba = a[aleatorio1]
       prueba2 = b[aleatorio1]
       prueba = str(prueba)
       prueba2 = str(prueba2)

       a = a[:aleatorio1] + prueba2 + a[aleatorio1 + 1:]
       b = b[:aleatorio1] + prueba2 + b[aleatorio1 + 1:]
       c2 = a[:aleatorio1] + prueba2 + a[aleatorio1 + 1:]
       # papalabra += aleatorio2

       # palabra para desemcriptar

       print(f"Enhorabuena!:\n"
             f"{papalabra}\n"
             f"{aleatorio1}\n"
             f"{a}\n"
             f"{b}\n"
             f"{c2}\n"

             f"{prueba}\n"
             f"{prueba2}\n")
       if ingreso_letra ==prueba2:
           papa += ingreso_letra
           print(papa)



    


       if a == b :
            print("¡¡¡GANASTE!!!!!")

  if vidas == 0:
       print(f"Te quedan {vidas} vidas, perdiste")

  else:
       print(f"Intentalo de nuevo, te quedan {vidas} vidas.")

  vidas -= 1"""
"""
""if ingreso_letra in b and vidas > 0:
    papalabra += ingreso_letra

    aleatorio1 = b.find(ingreso_letra)

    prueba = a[aleatorio1]
    prueba2 = b[aleatorio1]

    prueba = str(prueba)
    prueba2 = str(prueba2)

    a = a[aleatorio1].join(prueba2)
    # papalabra += aleatorio2
"""""