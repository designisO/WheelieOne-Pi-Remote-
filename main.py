import PySimpleGUI as sg

layout = [[sg.Text("REMOTE INFO", key="remote")],
          [sg.Button("FORWARD", size=(25, 3), font="Ariel 32", button_color=('white', 'green'))],
          [sg.Button("LEFT", size=(18, 3), font="Ariel 24", button_color=('black', 'yellow')), sg.Button("RIGHT", size=(14, 3), font="Ariel 24", button_color=('white', 'blue'))],
          [sg.Button("STOP", size=(25, 3), font="Ariel 32", button_color=('white', 'red'))],
          [sg.Button("QUIT")]
          ]
# Create the Window
window = sg.Window('WHEELIEONE REMOTE', layout)
# Event Loop to process "events"
while True:
    event, values = window.read()
    window['remote'].Update(event)  # show the button in the feedback text
    print(event, values)
    if event in (None, 'QUIT'):
        break
window.close()