"""def chequear_3_cigras(numero):
    return numero in range(100,1000)

suma = 413 + 345
resultado = chequear_3_cigras(suma)
print(resultado)"""

"""def chequear_3_cigras(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False
resultado = chequear_3_cigras([55, 99 ,300])
print(resultado)
"""

"""def chequear_3_cigras(lista):

    lista_3_cifras =[]

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
resultado = chequear_3_cigras([55, 99 ,300])
print(resultado)"""


"""def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True


lista_numeros = todos_positivos([32, 2, 1, 3, -3])
print(lista_numeros)

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]


def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True"""


"""lista_numeros = [233, -3,50000,3,51,88]

def suma_menores(lista):
    suma = 0
    for n in lista:
        if n > 0:
            suma1 = suma + n
            continue
    return suma1





ew = suma_menores(lista_numeros)

print(ew)"""

"""lista_numeros = [233, -3,50000,3,51,88]

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(1, 1000):
            suma +=  n
        else:
            pass
    return suma



ew = suma_menores(lista_numeros)

print(ew)"""


"""lista_numeros = [1, 50, 500, 5000, 750, 600]


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma
"""




"""mi_valor = list(range(1,16))
suma_cuadrados = 0
for cuadrados in mi_valor:
    mi_valor = cuadrados ** 2

    print(mi_valor)
    suma_cuadrados = suma_cuadrados + mi_valor
    print(suma_cuadrados)
    ----------------------------
    lista_nombres1 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombres_conm,indice11 in enumerate(lista_nombres1):
    if nombres_conm.startswith("M"):
        print(f'{nombres_conm} {indice11}')

"""

lista_numeros = [12, 21, 302, 2000, 55, 630, 33, 61,32,33,44]


def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad

print(cantidad_pares(lista_numeros))


"""lista_numeros = [233, -3,50000,3,51,88]

def cantidad_pares(lista_numeros):
    cuenta = ''
    for n,o in enumerate(lista_numeros):
        if o %2 == 0:
            cuenta =+ o
        else:
            pass
            
    return
print(cantidad_pares(lista_numeros))
"""