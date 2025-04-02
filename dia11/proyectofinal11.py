import bs4
import requests
import lxml


# Crear url sin número de página
url_basica = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista de títulos con 4 o 5 estrellas

titulos_calidad = []

# iterar páginas

for pagina in range (1, 51):

    # Crear sopita en cada página
    url_pagina = url_basica.format(pagina)
    resultado = requests.get(url_pagina)
    sopita = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Selecionar datos de los libros
    libros_totales = sopita.select('.product_pod')

    # Iterar libros
    for libro in libros_totales:

        # Ver si tiene 4 o 5 estrellas

        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # Guardar titulo en una variable

            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a la lista
            titulos_calidad.append(titulo_libro)

# Ver libros de 4 o 5 estrellas en consola

for t in titulos_calidad:
    print(t)