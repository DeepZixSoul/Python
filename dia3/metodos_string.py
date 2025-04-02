frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase.upper()
print(fragmento)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[3].upper()
print(fragmento)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase.split()
print(fragmento)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase.split("t")
print(fragmento)



a = "Aprender"
b = "python"
c = "es"
d = "divertido"
e = " ".join([a,b,c,d])
print(e)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase.find("s")
print(fragmento)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase.replace("c","ch")
print(fragmento)

lista_palabras = ["La","legibilidad","cuenta."]
lista_palabras2 = " ".join(lista_palabras)
print(lista_palabras2)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")
print(frase)