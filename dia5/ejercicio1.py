"""Crea una función llamada devolver_distintos()
que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15
, va a devolver elnúmero mayor.
Si la suma de los 3 numeros es menor a 10, va a
devolver el número menor.
Si la suma de los 3 números es un valor
entre 10 y 15(incluidos) va a devolver
el número de valor intermedio."""

"""def devolver_distintos(*args):
    suma = 0
    for n in args :
        suma += n
        if suma > 15:
            return max(args)
        elif suma < 10:
            return min(args)
        elif suma in range(10,15):
            sumao = sorted(args)
            return args[1]
  

"""
def devolver_distintos(*args):
    suma = sum(args)
    print(suma)
    if suma > 15:
        return max(args)
    elif suma < 10:
        return min(args)
    elif suma in range(10, 15):
        args = sorted(args)
        return args[1]






print(devolver_distintos(6,4,3))