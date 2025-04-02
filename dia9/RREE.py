import re

texto = 'Si necesitas ayuda llama al (658)-586.9977 las 24 horas del día al servicio de ayuda online'

patron = 'nada'
patron1 = 'ayuda'
busqueda = re.search(patron, texto)
busqueda1 = re.search(patron1, texto)
busqueda2 = re.findall(patron1, texto)
print(busqueda)
print(busqueda1)
# Ubicación de la palabra encontrada
print(busqueda1.span())
# Ubicación del cominezo de la palabra
print(busqueda1.start())
# Ubicación del final de la palabra encontrada
print(busqueda1.end())

# Ubicación de los dos elementos que salen en un texto
for hallazgo in re.finditer(patron1, texto):
    print(hallazgo.span())
