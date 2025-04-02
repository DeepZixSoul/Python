"""def suma():
    n1 = int(input("número 1: "))
    n2 = int(input("número 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)


try:
    suma()
except TypeError:
    print("Estas intentado concatenar tipos distintos")
except ValueError:
    print("No es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")
"""

"""def pedir_numero():

    while True:
        try:
            numero = int(input("Numero 1:"))
        except:
            print("No es un numero")
        else:
            print(f"Ingresaste{numero} ")
            break
    print("Gracias")

pedir_numero()
# ejercicio 2 
def cociente(num1,num2):
    
    try:
        
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
# Ejercicio 3

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
"""


def suma(num1, num2):
    try:
        numero = num1 + num2
    except:
        print("Error inesperado")
    else:
        print(f"Ingresaste{numero} ")


suma("t",2)