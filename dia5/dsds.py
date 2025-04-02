def es_primo(numero):
    """
    Verifica si un número dado es primo.

    Parámetros:
    - numero (int): El número que se quiere verificar.

    Retorna:
    - bool: True si el número es primo, False si no lo es.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso:
numero_ingresado = int(input("Ingresa un número para verificar si es primo: "))

if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")
