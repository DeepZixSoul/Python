nombre = input("Ingresa tu nombre: ")

ventas = int(input(f"Hola {nombre} ingresa tus ventas totales para calcular tus comisiones: "))

comision = round((ventas * 13) / 100,2)

print(f"¡Enhorabuena {nombre} has ganado {comision}€ en comisiones!")
