import re

texto = 'llama al 564-525-6588 ya mismo'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'
patron3 = r'(\d{3})-(\d{3})-(\d{4})'
restultado = re.search(patron, texto)
restultado2 = re.search(patron2, texto)
restultado3 = re.search(patron3, texto)
print(restultado)
# resultado del patron en particular
print(restultado.group())

print(restultado2)
print(restultado2.group())

print(restultado3)
print(restultado3.group())
# Índice empieza por "1" no por "0"
print(restultado3.group(1))
print(restultado3.group(2))
print(restultado3.group(3))
