import app
import timing
import sys

#This file will manage the main logic, track the Activity classes and call functions from the timing and app files
class Activity:
    def __init__(self, name, hotkey, time):
        self.name = name
        self.hotkey = hotkey
        self.time = time

    def __str__(self):
        return f'"{self.name}" has "{self.hotkey}" as the hotkey, and you have recorded {self.time} today'

def main():
    #check the user-settings.json file exists

    #if it does not exist, render an app window to take initial settings

    while True:
        main_app()

def main_app():
    #move this function to a different .py file. Have the .app be only for rendering app windows.
    file = ''
    while True:
        # home_window returns 'change' to change the save directory
        # 'modify' to change settings
        # 'tracking' to start tracking
        # 'log' to view the log
        output = app.home_window()
        if output == 'change':
            file = app.file_path_window()
            break
        elif output == 'modify':
            activity1, activity2, activity3 = app.settings_window("One", "Two", "Three")
            break
        elif output == 'log':
            app.log_window()
            break
        elif output == 'export':
            app.export_window()
            break
        elif output == 'tracking':
            to_track = app.tracking_window()
            minutes = timing.record_time('ctrl + shift + F1')
            sys.exit(f"{minutes} minutes recorded")
            break


if __name__ == '__main__':
    main()