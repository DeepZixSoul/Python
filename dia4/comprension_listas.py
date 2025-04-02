"""palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
lrista = [n / 2 for n in range(0,21,2)]
print(lrista)
print(lista)"""

palabra = 'python'

lista = [letra for letra in palabra]

print(lista)

lrista = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lrista)


pies = [10,20,30,40,50]
metros = [ p / 3.281 for p in pies]
print(metros)
