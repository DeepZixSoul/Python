mi_set = set([1,2,(1,2,3,4),3,4,5])
print(type(mi_set))
print(len(mi_set))
print(2 in mi_set)
print(mi_set)

otro_set = {1,2,3,4,5}
print(type(otro_set))
print(otro_set)

s1 = set([1,2,3])
s2 = set([3,4,5])
s3 = s1.union(s2)
s3.add(6)
s3.remove(3)
s3.discard(7)
s3.pop()
s3.clear()
print(s3)
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)
sorte = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorte.add("Damian")
print(sorte)

verifica = (17834/32) == (87*56)
print(verifica)