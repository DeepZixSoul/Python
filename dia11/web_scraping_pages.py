import bs4
import requests
import lxml


# Forma de url
url_basica = "https://books.toscrape.com/catalogue/page-{}.html"


"""for n in range(1,11):
    print(url_basica.format(n))"""

resultado = requests.get(url_basica.format('1'))

sopita = bs4.BeautifulSoup(resultado.text, 'lxml')

# Contenido de la listas que buscamos
# print(sopita.select('.product_pod'))


# Largo de la lista que estamos buscando.
# print(len(sopita.select('.product_pod')))
""" Nobre original de la clase "star-rating Three"
 Pero al tener un espacio el espacrio entre
"raiting" y "Three" hay que reemplazarlo por un "." """
libros = sopita.select('.product_pod')
libros_estrellas = sopita.select('.star-rating.Three')
""" En este ejemplo en la etiqueta "a" tiene dos parametros
al necesitar el segundo lo indicamos con[1] 
y en el segundo['title'] estamos utilizandolo como
un diccionario y nos dá directamente el valor
de la clave title"""
ejemplo = libros[0].select('a')[1]['title']

print(ejemplo)