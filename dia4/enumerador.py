lista = ['a', 'b', 'c']
indice = 0
for item in lista:
    print(indice, item)
    indice += 1

lista1 = ['a', 'b', 'c']

for item1 in enumerate(lista1):
    print(item1)

for indice1, item1 in enumerate(lista1):
    print(indice1,item1)
for indice1, item1 in enumerate(range(50,80)):
    print(indice1,item1)
litas4= ['a', 'b', 'c']
mis_tuples = list(enumerate(litas4))
print(mis_tuples)
print(mis_tuples[1][1])

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):

    print(f'{nombre} se encuentra en el índice {indice}')


python = "Python"
lista_indices = list(enumerate(python))
print(lista_indices)

lista_nombres1 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombres_conm,indice11 in enumerate(lista_nombres1):
    if nombres_conm.startswith("M"):
        print(f'{nombres_conm} {indice11}')

"""""
for nombre in lis1:

    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no comienza con l : ' + nombre)"""