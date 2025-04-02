"""
Escribe una función que requiera una cantidad indefinida deargumentos.
 Lo que hará esta función es devolver
True
si en algún momento se ha ingresado al numero
cero
repetido dos veces consecutivas
.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>>
True
(6,0,5,1,0,3,0,1) >>>
False"""

def la_funcion(*args):
    args = str(args)
    print(args)
    if ("0, 0") in args:
        return True
    else:
        return False





print(la_funcion((5,0,0,0,9,3,5)))

def cer_vecinos(*args):
    contador = 0
    for num in args:
        if contador +1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(cer_vecinos(5,6,1,0,0,3,5))

