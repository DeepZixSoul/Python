"""def suma(**kwargs):

    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} es = a {valor}")
        total += valor
    return total
print (suma(x=3, y= 5, z=2))

"""
def prueba(num1, num2, *args, **kwargs):

    print(f" el primer valor es {num1}")
    print(f" el primer valor es {num2}")

    for arg in args:
        print(f" arg = {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave} es = a {valor}")

args = [23,123,15,71,81]

kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

"""prueba(15,50,23,123,15,71,81, x = "uno", y = "dos", z="tres")
"""

prueba(15,50, *args, **kwargs)

