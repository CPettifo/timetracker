import app, timing, preferences
import sys
import json

#This file will manage the main logic, track the Activity classes and call functions from the timing and app files
class Activity:
    def __init__(self, name, hotkey, hours = 0, minutes = 0):
        self.name = name
        self.hotkey = hotkey
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'"{self.name}" has "{self.hotkey}" as the hotkey, and you have recorded {self.hours} hours and {self.minutes} minutes today'

    #allows you the main function to add minutes to the activity
    def add(self, n):
        hrs = int(n / 60)
        mins = (n - (hrs * 60))
        self.minutes += mins
        self.hours += hrs
    #@classmethod
    #def get(cls):
        #will call on function to make a new activity

act1 = Activity("Coding", "ctrl + shift + F1")
act2 = Activity("Writing", "ctrl + shift + F2")
act3 = Activity("French", "ctrl + shift + F2")
file = ''

def main():
    #check the user-settings.json file exists
    if preferences.check_file() == False:
        preferences.write_json('Activity 1', 'Hotkey 1', 'Activity 2', 'Hotkey 2', 'Activity 3', 'Hotkey 3')
    #if it does not exist, render an app window to take initial settings
    


    #testing initialisation of classes

    global act1
    global act2
    global act3
    act1.add(200)

    while True:
        print(act1)
        print(act2)
        print(act3)
        #call on the logic function
        logic()

def logic():
    global act1
    global act2
    global act3
    global file
    while True:
        # home_window returns 'change' to change the save directory
        # 'modify' to change settings
        # 'tracking' to start tracking
        # 'log' to view the log
        output = app.home_window()
        if output == 'change':
            file = app.file_path_window(file)
            break
        elif output == 'modify':
            act1.name, act2.name, act3.name = app.settings_window(act1.name, act2.name, act3.name)
            #update the .json file
            preferences.write_json(act1.name, act1.hotkey, act2.name, act2.hotkey, act3.name, act3.hotkey)
            break
        elif output == 'log':
            app.log_window(act1.name, act1.hours, act1.minutes, act2.name, act2.hours, act2.minutes, act3.name, act3.hours, act3.minutes)
            break
        elif output == 'export':
            app.export_window(file)
            break
        elif output == 'tracking':
            act = app.tracking_window(act1.name, act2.name, act3.name)
            if act == 'act1':
                minutes = timing.record_time(act1.hotkey)
                act1.add(minutes)
            elif act == 'act2':
                minutes = timing.record_time(act2.hotkey)
                act2.add(minutes)
            elif act == 'act3':
                minutes = timing.record_time(act3.hotkey)
                act3.add(minutes)
            break


if __name__ == '__main__':
    main()