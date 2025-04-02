"""Crea una función llamada cantidad_atributos
 que cuente la cantidad de parémetros que se entregan,
  y devuelva esa cantidad como resultado."""

"""def cantidad_atributos(**kwargs):
    cantidad = len(kwargs)
    return cantidad

print(cantidad_atributos(x = 1, z = 2, y = 3, o = 5))

Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en
 forma de palabras clave (keywords).
 La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""

"""def lista_atributos(**kwargs):
    cantidad = list(kwargs.values())
    return cantidad
print(lista_atributos(x = 1, z = 2, y = 3, o = 5))
"""
"""
Crea una función llamada describir_persona, que tome como parámetros su nombre 
y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio

    for clave, valor in kwargs.items():
        print(f"{clave} es = a {valor}")
"""

def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona("Diego", color_ojos="azules", color_pelo="rubio")

