'''
    Author: Jorge Martín
    Año creación: 2023
    Description:
    Asistente virtual tipo jarvis con Python. 
    Version: 1.0
    Dependencias: 
    Comandos implementados por ahora: (Decir antes jarvis)
    
    reproduce:  Ejemplo "reproduce musica relajante"
    hora:
    busca: Ejemplo "busca noticias de España"
    salir:
    
    
'''
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser

# Nombre del asistente virtual
names = ['jarvis', 'harvis']

# Inicialización de los componentes de voz
listener = sr.Recognizer()
engine = pyttsx3.init()

# Selección y configuración de la voz en español de España y masculina
voices = engine.getProperty('voices')
spanish_male_voice = None
for voice in voices:
    if 'es_ES' in voice.languages and 'male' in voice.gender:
        spanish_male_voice = voice
        break

if spanish_male_voice:
    engine.setProperty('voice', spanish_male_voice.id)
else:
    print("No se encontró una voz masculina en español de España, usando la predeterminada.")

engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    """Hace que el asistente hable."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Escucha comandos de voz y responde solo si se dice 'Jarvis' o 'Harvis'."""
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES').lower()
            if any(name in rec for name in names):
                rec = rec.split(maxsplit=1)[1] if len(rec.split(maxsplit=1)) > 1 else ''
                run(rec)
    except Exception as e:
        print("Error al escuchar:", e)

def run(rec):
    """Procesa el comando recibido."""
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '').strip()
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec or 'buscar' in rec:
        search_term = rec.replace('busca', '').replace('buscar', '').strip()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
        talk(f"Buscando en Google: {search_term}")
    elif 'salir' in rec:
        global flag
        flag = False
        talk("Saliendo...")
    else:
        talk("No entiendo el comando: " + rec)

# Ciclo principal del programa
flag = True
while flag:
    listen()





    