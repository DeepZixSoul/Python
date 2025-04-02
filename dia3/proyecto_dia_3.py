texto = input("Ingrese texto: ")
textol = texto.lower()
texto1 = list(texto)

letra1 = input("Ingrese la primera letra: ").lower()

letra2 = input("Ingrese la segunda letra: ").lower()

letra3 = input("Ingrese la tercer letra: ").lower()


print(f"La letra \"{letra1}\"  aparece :  {textol.count(letra1,0, -1)} veces,\nLa letra \"{letra2}\"  aparece :  {textol.count(letra2,0, -1)} veces,\nLa letra \"{letra3}\"  aparece :  {textol.count(letra3, )} veces,")

print(f"El texto tiene {len(texto1)} caracteres")

print(f"La primera letra del texto es \"{texto[0]}\"\nLa última letra del texto es \"{texto[-1]}\"")

print(f"El texto al revés sería: \"{texto[::-1]}\"")

python = "python"

pythont = python not in textol

pythonq = python in textol


dicta = {"Verdadero": pythonq, "Falso": pythont }

if "python" in textol:
    print("¡La palabra python está en el texto!")
else:
    print("¡La palabra python no está en el texto!")

