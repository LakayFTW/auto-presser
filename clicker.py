import keyboard
import PySimpleGUI as sg
from threading import Thread

def write_key(key):
    while start:
        keyboard.write(f'{key}', delay=0.01)

def main():
    global start
    start = False
    initial_text = "None"
    window_title = "Autoclicker v0.1"
    pressedKey = None
    sg.theme('DarkAmber')
    layout = [
        [
            sg.Button("Detect Keypress", border_width=0), sg.Text(initial_text, key='buttonPressed', size=30),
        ],
        [
            sg.HSeparator()
        ],
        [
            sg.Button("Start", border_width=0), sg.Button("Stop", border_width=0), sg.Button("CLOSE", border_width=0)
        ]
    ]

    window = sg.Window(window_title, layout, size=(200, 200))

    while True:
        event, values = window.read()
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break
        if event == "Detect Keypress":
            pressedKey = keyboard.read_key()
            window['buttonPressed'].update(pressedKey.upper())
        if event == "Start":
            if pressedKey == None:
                continue
            start = True
            # keyboard.write(f'{pressedKey}', delay=0.01)
            thread = Thread(target=write_key, args=(pressedKey))
            thread.start()
        if event == "Stop":
            start = False
            thread.join()
            continue

    window.close()

t1 = Thread(target=main)
t1.start()
t1.join()