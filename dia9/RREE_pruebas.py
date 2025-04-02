import re
#Detectar si el email lo escribió bien
"""def verificar_email(email):
    patron = r'\w+\@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("ok")
    else:
        print("La dirección de email es incorrecta")

clave = 'diego@kik.com'
"""

#Detectar que la frase empiece con "Hola"
"""def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")
"""

"""def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


clave = 'XX1234'
"""
def verificar_cp(cp):
    patron = r'N\w{3}-\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
        print(verificar.group())
    else:
        print("No has saludado")


clave = 'Nryu-12365'
print(verificar_cp(clave))

"El código postal ingresado no es correcto"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'
patron3 = r'(\d{3})-(\d{3})-(\d{4})'