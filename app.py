import PySimpleGUI as sg
import time
import sys

sg.theme('DarkBlue')

def main_app():
    #move this function to a different .py file. Have the .app be only for rendering app windows.
    file = ''
    while True:
        # home_window returns 'change' to change the save directory
        # 'modify' to change settings
        # 'tracking' to start tracking
        # 'log' to view the log
        output = home_window()
        if output == 'change':
            file = file_path_window()
            break
        elif output == 'modify':
            activity1, activity2, activity3 = settings_window("One", "Two", "Three")
            break
        elif output == 'log':
            log_window()
            break
        elif output == 'export':
            export_window()
            break
        elif output == 'tracking':
            tracking_window()
            break

    #if file == '':
    #    file = file_path_window()

    print(file)
    return True

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
            sys.exit('Closed Successfully')
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

def file_path_window():

    layout = [  [sg.Text("Input the folder you wish to save your data into")],
                [sg.InputText(), sg.FileBrowse()],
                [sg.Button('OK'), sg.Button('Cancel')]]
                
    window = sg.Window('FileInput', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            break
        elif event == 'OK':
            if values == '':
                print('Must have input')
                break
            window.close()
            return str(values)

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
            return values
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
    return (Activity1, Activity2, Activity3)


def hotkey_window(activity):
    #takes as input the activity that you want to modify the hotkey of
    print('Not implemented yet')


def tracking_window():
    #displays the defined activity and what the configured hotkey is. And a button to start tracking.
    #while this window is open the program searches for hotkey input.
    layout = [  [sg.Text(f"Activity 1"), sg.Button("Record Activity 1")],
                [sg.Text(f"Activity 2"), sg.Button("Record Activity 2")],
                [sg.Text(f"Activity 3"), sg.Button("Record Activity 3")],
                [sg.Button("Cancel")]]

    window = sg.Window("Tracking Window", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            break
        elif event == "Record Activity 1":
            print("Now recording activity 1")
        elif event == "Record Activity 2":
            print("Now recording activity 2")
        elif event == "Record Activity 3":
            print("Now recording activity 3")




def log_window():
    #displays the logs for the day as text. Takes activity name and time from the activity class as inputs and displays them
    #has a button that takes the user to the export window


    layout = [  [sg.Text(f"You have spent X hours and X minutes on ACTIVITY 1 today")],
                [sg.Text(f"You have spent X hours and X minutes on ACTIVITY 2 today")],
                [sg.Text(f"You have spent X hours and X minutes on ACTIVITY 3 today")],
                [sg.Button('OK'), sg.Button("I'm finished for the day!")]]
                
    window = sg.Window("Today's Timetracking", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            window.close()
            break
        elif event == "I'm finished for the day!":
            window.close()
            export_window()
            break
        

def export_window():
    #takes the save directory as input, displays that in a window and then allows the user to export their activity times
    #will add to the specified excell spreadsheet and append the day's logs to it.
    layout = [  [sg.Text(f"You have specified FILEPATH as your export path")],
                [sg.Text(f"Pressing the button below will close the program and add a new row to the specified excel spreadsheet.")],
                [sg.Text(f"Make sure you are finished for the day."), sg.Button("EXPORT"), sg.Button("Cancel")]]
        
    window = sg.Window("Export", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            log_window()
            break
        elif event == "EXPORT":
            sys.exit("Data successfully exported now display a cute popup message")

    
