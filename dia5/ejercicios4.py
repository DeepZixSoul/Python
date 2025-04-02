""""Escribe una función llamada contar_primos() que requiera un solo argumento numérico
.Esta función va a mostrar en pantalla todos los números primos existentes en el
 rango que va desde cero hasta ese número incluido, y va a devolver la cantidad
  de números primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

"""def contar_primos(numero):
    numeros = 0
    for f in range(2,numero):
        numeros += f
        if numero == 0 or numero == 1:
            return print(f"{numero}no es valido")
        elif numero % f == 0:
            print(f"estos son {f}")



numero = 100
print(contar_primos(numero))
"""

def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)
print(contar_primos(50))

