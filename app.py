import sys, os
import speech_recognition as sr
from colorama import Fore
from art import tprint



from voice import voice_settings
from voice import config_voice
tprint("IRINA")

 # object creation

engine = config_voice.settings_voice()

voice_settings.settings_mic() # Started settings

rec = sr.Recognizer()

device_id = int(open('./config_mic.txt', 'r').read())

def answer(source):

    audio = rec.listen(source)

    query = rec.recognize_google(audio, language='ru-RU')

    text = query.lower()

    if text in ['стоп', "выключись"]:
        engine.say("Поняла вас, выключение через: 3... 2... 1...")
        engine.runAndWait()
        os.close()
    elif 'повтори' in text:
        
        engine.say(text.split()[1:])
        engine.runAndWait()
    elif text == 'что нужно сказать мне':
        engine.say('Я вас люблю, Максим')
        engine.runAndWait()
    elif text == 'почему я назвал тебя так':
        engine.say('Вы назвали меня Ирина из-за мема: "Ирина, еб твою мать"')
        engine.runAndWait()
    elif text == 'послание для димы':
        engine.say('Дима, пошли ебаца')
        engine.runAndWait()
    else:
        print(audio)
        engine.say(audio)

def record_volume():
    with sr.Microphone(device_index = device_id) as source:
        print(Fore.YELLOW + 'Распознование шумов...', Fore.RESET + '')
        rec.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print(Fore.GREEN + 'Слушаю...', Fore.RESET + '')

        engine.runAndWait()
        audio = rec.listen(source)

        query = rec.recognize_google(audio, language='ru-RU')

        text = query.lower()
        
        if text in ['ирина', 'рина', 'ириша', 'ира']:
            print(text)
            engine.say("Вы меня звали?")
            engine.runAndWait()
            answer(source)



    
        

engine.say("Ирина на связи")
while True:
    record_volume()