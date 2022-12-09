import PySimpleGUI as sg
import time, sys, keyboard
# this one is mine
import timing

sg.theme('DarkBlue')

def home_window():
    layout = [  #[sg.Text("This is the main app")],
                [sg.Button('Change save directory')],
                [sg.Button('Modify Activity Names/ Hotkeys')],
                [sg.Button('Start Tracking')],
                [sg.Button("View Today's Log")],
                [sg.Button("I'm finished for the day!")],
                [sg.Button('Exit')]]

    window = sg.Window('TimeTracker', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            return 'close'
        elif event == 'Change save directory':
            window.close()
            return 'change'
        elif event == 'Modify Activity Names/ Hotkeys':
            window.close()
            return 'modify'
        elif event == 'Start Tracking':
            window.close()
            return 'tracking'
        elif event == "View Today's Log":
            window.close()
            return 'log'
        elif event == "I'm finished for the day!":
            window.close()
            return 'export'

def file_path_window(file):

    layout = [  [sg.Text("Input the folder you wish to save your data into")],
                [sg.Text(f"Currently configured to save into:  {file}")],
                [sg.InputText(), sg.FileBrowse()],
                [sg.Button('OK'), sg.Button('Cancel')]]
                
    window = sg.Window('FileInput', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        elif event == 'OK':
            window.close()
            return str(values[0])

def settings_window(Activity1, Activity2, Activity3):
    #takes as input the activity names and hotkey and returns the name and hotkey if modified.
    layout = [  [sg.InputText(f'{Activity1}'), sg.Button('Change Hotkey 1')],
                [sg.InputText(f'{Activity2}'), sg.Button('Change Hotkey 2')],
                [sg.InputText(f'{Activity3}'), sg.Button('Change Hotkey 3')],
                [sg.Button('Change Names'), sg.Button('Cancel')]]


    window = sg.Window('Settings', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return(Activity1, Activity2, Activity3)
        elif event == 'Change Names':
            window.close()
            return (values[0], values[1], values[2])
        elif event == 'Change Hotkey 1':
            window.close()
            hotkey_window(Activity1)
            #NEED TO OPEN HOTKEY SETTING WINDOW HERE
            break
        elif event == 'Change Hotkey 2':
            window.close()
            hotkey_window(Activity2)
            #NEED TO OPEN HOTKEY SETTING WINDOW HERE
            break    
        elif event == 'Change Hotkey 3':
            window.close()
            hotkey_window(Activity3)
            #NEED TO OPEN HOTKEY SETTING WINDOW HERE
            break


def hotkey_window(activity):
    #takes as input the activity that you want to modify the hotkey of
    print('Not implemented yet')


def tracking_window(act1, act2, act3):
    #displays the defined activity and what the configured hotkey is. And a button to start tracking.
    #while this window is open the program searches for hotkey input.
    layout = [  [sg.Text(f"{act1}"), sg.Button("Record Activity 1")],
                [sg.Text(f"{act2}"), sg.Button("Record Activity 2")],
                [sg.Text(f"{act3}"), sg.Button("Record Activity 3")],
                [sg.Button("Cancel")]]

    window = sg.Window("Tracking Window", layout)
    act = 'IloveMarie'
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            break
        elif event == "Record Activity 1":
            act = 'act1'
            break
        elif event == "Record Activity 2":
            act = 'act2'
            break
        elif event == "Record Activity 3":
            act = 'act3'
            break
    window.close()
    if act != 'IloveMarie':
        return act


def log_window(act1, hrs1, mins1, act2, hrs2, mins2, act3, hrs3, mins3):
    #displays the logs for the day as text. Takes activity name and time from the activity class as inputs and displays them
    #has a button that takes the user to the export window


    layout = [  [sg.Text(f"You have spent {hrs1} hours and {mins1} minutes on {act1} today")],
                [sg.Text(f"You have spent {hrs2} hours and {mins2} minutes on {act2} today")],
                [sg.Text(f"You have spent {hrs3} hours and {mins3} minutes on {act3} today")],
                [sg.Button('OK')]]
                
    window = sg.Window("Today's Timetracking", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            window.close()
            break
        

def export_window(file):
    #takes the save directory as input, displays that in a window and then allows the user to export their activity times
    #will add to the specified excell spreadsheet and append the day's logs to it.
    layout = [  [sg.Text(f'You have specified "{file}" as your export path')],
                [sg.Text(f"Pressing the button below will close the program and add a new row to the specified excel spreadsheet.")],
                [sg.Text(f"Make sure you are finished for the day."), sg.Button("EXPORT"), sg.Button("Cancel")]]
        
    window = sg.Window("Export", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            break
        elif event == "EXPORT":
            window.close()
            return 'export'

hotkey_quit_value = 0
start = 0
minutes = 0

def quit_loop():
    global hotkey_quit_value
    hotkey_quit_value = 1

def hotkey_wait(key):
    global hotkey_quit_value
    global start
    global minutes
    start = time.time()
    hotkey_quit_value = 0
    minutes = 0
    keyboard.add_hotkey(key, quit_loop)
    while hotkey_quit_value == 0:
        if time.time() - start > 60:
            minutes += 1
            print(f"{minutes} minutes elapsed")
            start = time.time()

def record_window(act, key):

    layout = [ [sg.Text(f"Start recording for {act}? {key} will stop recording")],
                [sg.Button("Confirm"), sg.Button("Cancel")]]

    window = sg.Window("Counting", layout)
    window.move(10, 10)

    global minutes
    global hotkey_quit_value
    while True:
        event, values = window.read()
        if event == "Confirm":
            print(f"Timer begun for {act}")
            break
        elif event == "Cancel":
            window.close()
            return minutes
    if minutes == 0:
        window.close()
        hotkey_wait(key)
        sg.popup(f"Recorded {minutes} minutes for {act}")


  
    return minutes
