mi_lista = ['e', 'b', 'c']
mi_lista2 = ['d', 'a', 'f']

mi_lista3 = mi_lista + mi_lista2
mi_lista3.append("g")
eliminado = mi_lista3.pop(0)


print(mi_lista3)
print(eliminado)
mi_lista3.sort()
print(mi_lista3)
mi_lista3.reverse()
print(mi_lista3)

mi_lista = ['e', 'b', 'c', 3, True]

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)