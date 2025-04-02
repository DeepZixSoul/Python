""" listas en estado normal"""
from collections import Counter


numeros = [8,3,3,2,1,5,6,6,7,2,8,9,1,2,3,4,3]
print(Counter(numeros))

print(Counter("mississippi"))


#contar palabras, las separamos con split
frase = "al pan pan y al vino vino"

print(Counter(frase.split()))
#Enseña todos los numeros
serie = Counter([1,2,1,2,3,2,1,2,3,1,1,1,2,4,3,2,1,1])
print(serie.most_common())
#Enseña el primero
serie = Counter([1,2,1,2,3,2,1,2,3,1,1,1,2,4,3,2,1,1])
print(serie.most_common(1))
#Enseña el primero y el segundo
serie = Counter([1,2,1,2,3,2,1,2,3,1,1,1,2,4,3,2,1,1])
print(serie.most_common(2))
#Ordena los objetos unicos en una lista
print(list(serie))
