cliente = {'nombre': "Diego", 'Apellido': "Mancebo", 'Peso':82,'Talla':44}
print(cliente)

resultoda = cliente['nombre']
print(resultoda)

dic = {'c1': 33, 'c2': [1, 2, 3], 'c3':{'c5':82,'Talla':44}}
print(dic)

resultoda = dic['c2'][1]
print(resultoda)
resultoda = dic['c3']['c5']
print(resultoda)

dic1 = {'d1': ['a', 'b', 'c'], 'd2': ['d', 'e', 'f']}
dic1['d3'] = 'g'
print(dic1)
print(dic1['d2'][1].upper())
dic1['d1'] = 3
print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1.items())
mi_dic = {'nombre':'Karen', 'apellido':'Jurgens', 'edad':35, 'ocupacion':'Periodista'}
print(mi_dic)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["edad"] = 36
mi_dic["pais"] = "Colombia"
mi_dic["ocupacion"] = "Editora"

print(mi_dic)