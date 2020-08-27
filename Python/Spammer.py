from pyautogui import hotkey, press
from time import sleep
from pyperclip import copy

delay = int(input('Insira o delay entre as frases (em segundos) // Insert the delay between phrases (in seconds) :'))

print('Iniciando... // Starting...')

while True:
    texto = open('textoparaspam.txt', 'r')
    for palavra in texto:
        copy(palavra)
        sleep(delay)
        hotkey("ctrl", "v")
        press('enter')                                   
        print('Palavra enviada // Word sended')
    texto.close()

