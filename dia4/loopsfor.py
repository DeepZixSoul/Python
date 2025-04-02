lista = ['a', 'b', 'c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f" Letra {numero_letra}: '{letra}' ")

lis1 = ['Pablo', 'Lola', 'Fede', 'Cacho', 'Susi']

for nombre in lis1:

    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no comienza con l : ' + nombre)


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

numeros1= [1,2,3,4,5]
mi_valor1 = 0

for numero1 in numeros1:
    mi_valor1 = mi_valor1 + numero1
    print(mi_valor1)

palabra = 'python'
for letra in palabra:
    print(letra)

for letra1 in 'palabra':
    print(letra1)

for a,b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dictt = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dictt.items():
    print(item)

dictt = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dictt.values():
    print(item)

dictt = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for a, b in dictt.items():
    print(a)
    print(b)
