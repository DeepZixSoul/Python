alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumnos in alumnos_clase:

    print("Hola " + alumnos)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    print(suma_numeros)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for pares in lista_numeros:
     if pares %2 == 0:
         suma_pares = pares + suma_pares
         print(suma_pares)

for pares in lista_numeros:
     if pares %2 == 1:
         suma_impares = pares + suma_impares
         print(suma_impares)