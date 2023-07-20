import keyboard
import PySimpleGUI as sg

initial_text = "None"
window_title = "Autoclicker v0.1"

# left_column = [

# ]

# right_column = [
#     [
#         sg.Button("CLOSE", border_width=0),
#     ]
# ]

layout = [
    # [
    #     # sg.Column(left_column),
    #     # sg.VSeperator(),
    #     # sg.Column(right_column),
    # ]
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

sg.theme('DarkAmber')

window = sg.Window(window_title, layout, size=(200, 200))

# while True:
#     event, values = window.read()
#         break
#     break

while True:
    event, values = window.read()
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break
    if event == "Detect Keypress":
        pressedKey = keyboard.read_key()
        window['buttonPressed'].update(pressedKey)
    if event == "Start" or keyboard.is_pressed('shift+space'):
        print("started")
        if pressedKey == None:
            continue
        while True:
            keyboard.write(f'{pressedKey}', delay=0.01)
            if event == "Stop" or keyboard.is_pressed('shift+a'):
                print("stopped")
                break

window.close()