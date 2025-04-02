nombres = ['Ana', 'Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']

#zip llega al largo de la lsita más corta

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(capitales,paises))

for capital,pais in combinados:
    print(f"La capital de {pais} es {capital}")

marcas = ['hola','chau']
productos =['chau', 'hola']
mi_zip = zip(marcas,productos)

espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']

ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espaniol, portugues, ingles))
print(numeros)



"""a1 = uno / um / one
b2 =  dos / dois / two
c3 = tres / três / three
d4 = cuatro / quatro / four
f5 = cinco / cinco / five"""
