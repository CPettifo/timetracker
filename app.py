import PySimpleGUI as sg
import time
import sys

sg.theme('DarkBlue')

def logic():
    while True:
        main_app()

def main_app():
    file = ''
    while True:
        output = home_window()
        if output == 'change':
            file = file_path_window()
            break
        

    if file == '':
        file = file_path_window()

    print(file)
    return True

def home_window():
    layout = [  #[sg.Text("This is the main app")],
                [sg.Button('Change save directory')],
                [sg.Button('Modify Activity Names')],
                [sg.Button('Change Hotkeys')],
                [sg.Button('View Log')],
                [sg.Button('Exit')]]

    window = sg.Window('TimeTracker', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            sys.exit('Closed Successfully')
        elif event == 'Change save directory':
            window.close()
            return 'change'
        elif event == 'Modify Activity Names':
            window.close()
            return 'activities'
        elif event == 'Change Hotkeys':
            window.close()
            return 'hotkeys'

def file_path_window():

    layout = [  [sg.Text("Input the folder you wish to save your data into")],
                [sg.InputText(), sg.FileBrowse()],
                [sg.Button('OK'), sg.Button('Cancel')]]
                
    window = sg.Window('FileInput', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            if values == '':
                print('Must have input')
                break
            window.close()
            return str(values)
    
    
if __name__ == '__main__':
    logic()
