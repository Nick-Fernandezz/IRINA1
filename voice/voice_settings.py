import turtle
import speech_recognition as sr
from colorama import Fore

def settings_mic():

    with open('./config_mic.txt', 'r') as config:

        device = config.read()

        print(device)

        if device == 'None':
            
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                print(f'{index}. {name}')

            with open('./config_mic.txt', 'w') as config:
                try:
                    while True:

                        mic_index = input(Fore.GREEN + 'Введите номер устройства ввода аудио: ')
                        print(Fore.RESET + '')

                        if int(mic_index) > len(sr.Microphone.list_microphone_names()):
                            print(Fore.YELLOW + 'Введите номер устройства из списка', Fore.RESET + '')
                            continue

                        else:
                            try:
                                config.write(mic_index)
                                print(Fore.GREEN + "Настройки применены!", Fore.RESET + '')
                                config.close()
                            except:
                                print(Fore.RED + 'Ошибка применения настроек', Fore.RESET + '')
                            break
                except:
                    print(Fore.RED + "Ошибка настройки устройства ввода аудио", Fore.RESET + '')
        else: 
            print(Fore.GREEN + f'Применен микрофон с индексом {device}', Fore.RESET + '')
