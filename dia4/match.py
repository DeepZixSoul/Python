"""serie = "n1"

if serie == "n2":
    print("Este es un popo")
elif serie == "n1":
    print("De puta madre")
elif serie == "n2":
    print("Otro popo")
else:
    print("Me cansé de esperar")

match serie:
    case "n2":
        print("Este es un popo")
    case "n1":
        print("De puta madre")
    case "n3":
        print("Otro popo")
    case _:
        print("Me cansé de esperar")

"""

cliente = {'nombre':'Diego',
           'edad': '29',
           'ocupacion': 'informatico'}
pelicula = {'titulo': 'avatar',
            'ficha_tecnica': {'protagonista': 'Keanu reeves',
                              'director': 'Lana y Lily wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre,edad,ocupacion)
        case{'titulo': titulo,
             'ficha_tecnica': {'protagonista': protagonista,
                               'director': director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No sé que es esto")


