import pygame
import random
import math
from pygame import mixer
import io


# Inicializar Pygame
pygame.init()

# Agregar Música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)
# Crear Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption("Disparos LOCOOO")
icono = pygame.image.load("ovni.png")
fondo = pygame.image.load("Fondo.jpg")
pygame.display.set_icon(icono)

# Variables jugador
# Jugador tamaño 64 pix 800 pixeles de -
# ancho / 2 400 - 64 eje x lo mismo con el eje Y
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_change = 0
jugador_y_change = 0

# Variables enegimo
# Se deberia usar una funcion para no repetir codigo
# Se debería crear clases para crear varios enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_change = []
enemigo_y_change = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_change.append(0.2)
    enemigo_y_change.append(50)


# Funcion transformar fuente en bytes
def fuente_bytes(fuentee):
    # Abre el archivo TTF en modo lectura binaria
    with open(fuentee, 'rb') as f:
        # Lee todos losbytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


# Variables bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 550
bala_x_change = 0
bala_y_change = 0.6
bala_visibilidad = False

# Variable puntaje
puntaje = 0
fuente_bytes_transformado = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_bytes_transformado, 40)
texto_x = 10
texto_y = 10

# Texto Game Over

fuente_final = pygame.font.Font(fuente_bytes_transformado, 45)


# Función txto final
def texto_final():
    mi_fuente_final = fuente_final.render("PUTOOOOOOOOOOOO", True,(255, 255, 255))
    pantalla.blit(mi_fuente_final, (55, 200))
# Función mostrar puntaje


def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))
# Funcion jugador


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Funcion disparo bala
def disparo_bala(x, y):
    global bala_visibilidad
    bala_visibilidad = True
    # Valor x + valor e Y + valor, calculo de pixel según imagen nave
    pantalla.blit(img_bala, (x + 16, y + 10))


# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True


while se_ejecuta:

    # RGB
    # pantalla.fill((122, 91, 196))
    # Fondo
    pantalla.blit(fondo, (0, 0))

    # Iterar evento
    for evento in pygame.event.get():
        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclass
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_change = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_change = 0.4
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -1
                }
                """if not bala_visibilidad:
                    bala_x = jugador_x
                    disparo_bala(bala_x, bala_y)"""
                balas.append(nueva_bala)

        # Evento solar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_change = 0

    # Modificar ubicación del jugador
    jugador_x += jugador_x_change

    # Mantener dentro de bordes eje x 800-64= 736 jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_change[e]

    # Mantener dentro de bordes eje x 800-64= 736 jugador
        if enemigo_x[e] <= 0:
            enemigo_x_change[e] = 0.2
            enemigo_y[e] += enemigo_y_change[e]

        elif enemigo_x[e] >= 736:
            enemigo_x_change[e] = -0.2
            enemigo_y[e] += enemigo_y_change[e]

        # Colisión
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visibilidad = False
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    if bala_visibilidad:
        disparo_bala(bala_x, bala_y)
        bala_y -= bala_y_change

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)
    # Actualizar
    pygame.display.update()
