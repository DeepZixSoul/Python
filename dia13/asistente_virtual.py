import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

ide1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
ide2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# Escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_texto():

    # Almacenar recognizer en una variable
    re = sr.Recognizer()

    # Configurar el micrófono

    with sr.Microphone() as origen:
        # Tiempo espera
        re.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar escucha como audio
        audio = re.listen(origen)

        try:
            # Buscar en google lo que haya escuchado

            pedido = re.recognize_google(audio, language="es-ES")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido
        # En caso de que no comprenda el audio

        except sr.UnknownValueError:

            # Prueba de que no comprendió el audio
            print("Ups, Que ise?")

            # Devolver error
            return "Te espero"
        # En caso de no resolver el pedido

        except sr.RequestError:
            # Prueba de que no comprendió el audio
            print("Ups, No puede seh?")

            # Devolver error
            return "Te espero2"

        # Error inesperado

        except:
            # Prueba de que no comprendió el audio
            print("Ups, Mae mía!")

            # Devolver error
            return "Te espero"
        # En caso de no resolver el pedido


# Función para que escuchar al asistente
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    # Elegir que tipo de voz
    engine.setProperty('voice', ide1)

    # Dicte el mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Función informar el día de la semana
def pedir_dia():
    # Crear variable con datos de hoy

    dia_hoy = datetime.date.today()
    print(dia_hoy)

    # Crear vaiable para día de la semana
    dia_semana = dia_hoy.weekday()
    print(dia_semana)

    # Diccionario con nombres de días
    semanario = {0: 'Lunes',
                 1: 'Martes',
                 2: 'Miércoles',
                 3: 'Jueves',
                 4: 'Viernes',
                 6: 'Sábado',
                 7: 'Domingo'}
    # Decir el día de la semana
    hablar(f'Hoy es {semanario[dia_semana]}')


# Función informar hora
def pedir_hora():

    # Crea variable con datos de la hora
    hora_dia = datetime.datetime.now()
    hora = f' Son las {hora_dia.hour} horas con {hora_dia.minute} minutos y {hora_dia.second} segundos'

    # Decir lahora
    hablar(hora)


# Función saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir saludo
    hablar(f'Hola, {momento}, soy una MoshiMoshi, tu moshi personal. Por favor, dime en que te puedo moshimoshear')


# Función central del asistente
def pedir_ordenes():

    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('De acuerdo Moshi')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('De acuerdo Moshi')
            webbrowser.open('https://www.google.com')
            continue
        elif 'que día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('De acuerdo Moshi')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('De acuerdo moshii')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que encontré')
            continue
        elif 'reproducir' in pedido:
            hablar('Vale moshi moshete')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f' El precio de {accion} es {precio_actual}')
                continue

            except:
                hablar('Perdón no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Ta lueguito Moshi')
            break


pedir_ordenes()


# Pruebas de voces ver que voces hay
"""engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
"""