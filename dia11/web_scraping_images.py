import bs4
import requests
import lxml

resultad_imagen = requests.get('https://www.escueladirecta.com/courses/')

sopa_imagen = bs4.BeautifulSoup(resultad_imagen.text, 'lxml')

imagenes = sopa_imagen.select('.course-box-image')[0]['src']

print(imagenes)

imagenes_curso = requests.get(imagenes)

# Si se quiere guardar en un lugar distinto
# en el nombre del archivo poner la ubicacion del directorio C: ....
f = open('mi_imagen.jgp', 'wb')
f.write(imagenes_curso.content)
f.close()
