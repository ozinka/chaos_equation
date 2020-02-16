import PySimpleGUI as sg

# sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('10:00'),sg.Text("12:55", size=(5, 1), font="Helvetica 13", key='text')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('', layout,
                   no_titlebar=True,
                   grab_anywhere=True,
                   keep_on_top=True,
                   background_color="white")
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    print('You entered ')

window.close()
