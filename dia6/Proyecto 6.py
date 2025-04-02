from pathlib import Path
import sys
from os import system
base = Path(Path.home(),"Recetas")

print("*" * 70 + "")
print(f"*" * 6 + f" Buenas tus recetas se encuentra en{base} " + "*" * 6)
print("*" * 70 + "\n")
# Enseñar categoría de recetas

def recetas_total():
    total_recetas = 0

    for txt in Path(base).glob('**/*.txt'):
        total_recetas += 1

    return total_recetas
print("*" * 70 + "")
print ("*" * 21 + f" Hay un total de {recetas_total()} recetas " + "*" * 21)
print("*" * 70 + "\n")
# Elegir categoría
def elegir_categoria(directorio):

    ruta_principal = Path(base)
    categoria = [ruta for ruta in ruta_principal.iterdir() if ruta.is_dir()]
    diccionario_categoria = {}
    print("Categoría de recetas:\n")
    for indice,directorio in enumerate(categoria):
        directorio_str = directorio.stem
        diccionario_categoria[indice] = directorio_str
        print(f"{indice+1}- {directorio_str}\n")


    categoria_elegir =  int(input("Elige una cageroría: \n")) -1

    resultado = diccionario_categoria[categoria_elegir]
    #nombre_dir = diccionario_categoría.get(categoria_elegir)
    path_categoria = Path(base)/ resultado
    system('cls')
    print(f"Aquie tiene las recestas de {resultado}:\n")
    #print(nombre_dir)
    #print(path_categoría)

    return path_categoria


# Opción 1

def leer_recetas(categoria):
    path_categoria = Path(base, categoria)
    diccionario_recetas = {}
    for indice, txt in enumerate(path_categoria.glob('*.txt')):
        txt_str = txt.stem
        diccionario_recetas[indice] = txt_str
        print(f" {indice+1} {txt_str}")

    eleccion_cocinero = int(input("\nElija el número de receta: \n")) -1


    resultado = diccionario_recetas[eleccion_cocinero]


    rece_txt = diccionario_recetas.get(eleccion_cocinero) + '.txt'

    enseniar_receta = path_categoria/ rece_txt
    enseniar_receta = enseniar_receta.read_text()
    system('cls')
    print(f"Usted eligió la siguiente receta\n¡¡¡{resultado}!!!:\n"
          f"Estos son sus ingredientes :{enseniar_receta}\n")


#Opcion_1 = leer_recetas(elegir_categoria(base))


# Opción 2

def crear_recetas(categoria):

    nueva_receta_nombre = input("Ingrasa el nombre de la receta:")
    nueva_receta_nombre = nueva_receta_nombre + ".txt"

    cateoria_path = Path(base,categoria)
    nuevo_archivo = cateoria_path / nueva_receta_nombre
    gola = input("Ingrese ingredientes: ")
    with open(nuevo_archivo, 'a') as archivo:
        archivo.write(gola)


    #with_name añadir nombre de nuevo txt

#Opcion_2 = crear_recetas(elegir_categoria(base))

# Opción 3

def crear_directorio():
    ruta_principal = Path(base)
    categoria = [ruta for ruta in ruta_principal.iterdir() if ruta.is_dir()]
    diccionario_categoria = {}
    for indice, directorio in enumerate(categoria):
        directorio_str = directorio.stem
        diccionario_categoria[indice] = directorio_str
        print(f"{indice + 1}- {directorio_str}\n")
    nuevo_directorio = input("Ingresa nombre de la nueva categoría:")
    ruta_nuevo_directorio = base / nuevo_directorio
    if ruta_nuevo_directorio.exists():
        print(f"¡Advertencia! El directorio '{ruta_nuevo_directorio}' ya existe.")
    else:
        # Crear el nuevo directorio
        ruta_nuevo_directorio.mkdir(parents=True)
        print(f"Se ha creado el nuevo directorio: {ruta_nuevo_directorio}")

#Opcion_3 = crear_directorio()

# Opción 4

def eliminar_recetas(categoria):
    path_categoria = Path(base, categoria)
    diccionario_recetas = {}
    for indice, txt in enumerate(path_categoria.glob('*.txt')):
        txt_str = txt.stem
        diccionario_recetas[indice] = txt_str
        print(f" {indice+1} {txt_str}")

    eleccion_cocinero = int(input("\nElija el número de receta: \n")) -1
    system('cls')
    resultado = diccionario_recetas[eleccion_cocinero]
    print("***" * 24 + "\n")

    rece_txt = diccionario_recetas.get(eleccion_cocinero) + ".txt"

    enseniar_receta = path_categoria / rece_txt
    enseniar_receta = enseniar_receta.unlink()
    print(f"Usted eliminó la siguiente receta:\n¡¡¡{resultado}!!!\n")


#Opcion_4 = eliminar_recetas(elegir_categoria(base))

# Opción 5

def eliminar_directorio():

    ruta_principal = Path(base)
    categoria = [ruta for ruta in ruta_principal.iterdir() if ruta.is_dir()]
    diccionario_categoria = {}
    for indice, directorio in enumerate(categoria):
        directorio_str = directorio.stem
        diccionario_categoria[indice] = directorio_str
        print(f"{indice + 1}- {directorio_str}\n")
    categoria_elegir = int(input("Elige una cageroría para eliminar: \n")) - 1
    system('cls')
    resultado = diccionario_categoria[categoria_elegir]
    # nombre_dir = diccionario_categoría.get(categoria_elegir)
    path_categoria = Path(base) / resultado

    if path_categoria.exists():
        print(f"¡Advertencia! El directorio '{path_categoria}' se elminará.")
        path_categoria.rmdir()
    else:
        # Crear el nuevo directorio
        print(f"La categoría {path_categoria} se eliminara")

#Opcion_5 = eliminar_directorio()

# Opción_6

def terminar_programa():
    print("El programa se cerrará.")
    sys.exit()

#Opcion_6 = terminar_programa()



entrada_usuario = ''

while entrada_usuario != 6:
    print("Bienvenido al recetario ¿ Que deceas hacer?\n"
          "[1]-Leer Recetas\n"
          "[2]-Crear Recetas\n"
          "[3]-Crear Categoría de recetas\n"
          "[4]-Eliminar Recetas\n"
          "[5]-Eliminar Categoría de recetas\n"
          "[6]-Salir del programa\n")
    entrada_usuario = int(input("Elige una opción:"))
    system('cls')

    if entrada_usuario == 1 :
        leer_recetas(elegir_categoria(base))
        input("Pulse enter para volver al menú:")
        system('cls')
    elif entrada_usuario == 2:
        crear_recetas(elegir_categoria(base))
        input("Pulse enter para volver al menú:")
        system('cls')
    elif entrada_usuario == 3:
        crear_directorio()
        input("Pulse enter para volver al menú:")
        system('cls')
    elif entrada_usuario == 4:
        eliminar_recetas(elegir_categoria(base))
        input("Pulse enter para volver al menú:")
        system('cls')
    elif entrada_usuario == 5:
        eliminar_directorio()
        input("Pulse enter para volver al menú:")
        system('cls')
    else :
        terminar_programa()
