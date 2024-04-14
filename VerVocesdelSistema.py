'''
Author: Jorge Martín
    Año creación: 2024
    Description: Listadod de voces instaladas en el sistema
'''        


import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}")
    print(f"Name: {voice.name}")
    print(f"Gender: {voice.gender}")
    print(f"Languages: {voice.languages}")
    print(f"Age: {voice.age}")
    print("-" * 40)


