import keyboard
import PySimpleGUI as sg
from threading import Thread, Event

def write_key(key, stop_event):
    while not stop_event.is_set():
        keyboard.write(f'{key}', delay=0.01)

def main():
    stop_event = Event()
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

    thread = None

    try:
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
                stop_event.clear()
                thread = Thread(target=write_key, args=(pressedKey, stop_event))
                thread.start()
            if event == "Stop":
                stop_event.set()
                thread.join()
                thread = None

        window.close()
    finally:
        if thread is not None:
            stop_event.set()
            thread.join()
        window.close()

if __name__ == "__main__":
    main()