import bs4
import requests
import lxml

# Variables
resultado_busqueda_web = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

sopita = bs4.BeautifulSoup(resultado_busqueda_web.text, 'lxml')

#print(sopita.select('title')[0].getText())

parrafo_busqueda = sopita.select('p')[3].getText()

columna_lateral = sopita.select('.r-snippetized')
print(columna_lateral)

