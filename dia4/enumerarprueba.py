"""lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):

    print(f'{nombre} se encuentra en el índice {indice}')
"""

lista_nombres1 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombres_conm,indice11 in enumerate(lista_nombres1):
    if indice11.startswith("M"):
        print(nombres_conm)

"""""
for nombre in lis1:

    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no comienza con l : ' + nombre)"""