mi_texto ="Esta es una prueba.py"
resultado = mi_texto.index("n")
print(resultado)
palabra = "ordenador"
palabra = palabra.index("n")
print(palabra)

palabra = "ordenador"
palabra = palabra[4]
print(palabra)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = frase.index("práctica")

print(frase)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = frase.rindex("práctica")

print(frase)