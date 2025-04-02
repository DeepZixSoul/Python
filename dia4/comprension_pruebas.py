"""for letra in palabra:
    lista.append(letra)
lrista = [n / 2 for n in range(0,21,2)]
print(lrista)
print(lista)"""

"""
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [c **2 for c in valores]
print(valores_cuadrado)
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [c  for c in valores if c %2 == 0 ]

print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]


°C = (°F - 32) * (5/9)

"""

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(f - 32) * (5/9) for f in temperatura_fahrenheit ]
print(grados_celsius)