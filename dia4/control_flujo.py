
if 10 > 9 :
    print('Es correcto')


x = True

if x:
    print('Es correcto')

if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'perro'


if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No sé que animal tienes')



edad = 19
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >=7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')

#num1 = int(input("Ingresa un número:"))
#num2 = int(input("Ingresa otro número:"))

#if num1 > num2:
#    print(f"{num1} es mayor que {num2}")
#elif num2 == num1:
#   print(f"{num1} y {num2} son iguales")
#else:
#    print(f"{num2} es mayor que {num1}")

edad = 16
tiene_licencia = False
if edad >= 18 and not tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 and  tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")

elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")

elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python")

else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

