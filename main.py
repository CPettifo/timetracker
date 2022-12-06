import app, timing, preferences, data
import sys
import json

#This file will manage the main logic, track the Activity classes and call functions from the timing and app files
class Activity:
    def __init__(self, name, hotkey, hrs = 0, mins = 0):
        self.name = name
        self.hotkey = hotkey
        self.hrs = hrs
        self.mins = mins

    def __str__(self):
        return f'"{self.name}" has "{self.hotkey}" as the hotkey, and you have recorded {self.hrs} hours and {self.mins} minutes today'

    #allows you the main function to add minutes to the activity
    def add(self, n):
        hours = int(n / 60)
        minutes = (n - (hours * 60))
        self.mins += minutes
        self.hrs += hours
    #@classmethod
    #def get(cls):
        #will call on function to make a new activity

act1 = Activity("Coding", "ctrl + shift + F1")
act2 = Activity("Writing", "ctrl + shift + F2")
act3 = Activity("French", "ctrl + shift + F2")
file = ''

def main():
    # initialize the classes
    global act1, act2, act3

    # check the user-settings.json file exists
    if data.check_file('activities.json') == False:
        preferences.write_json('Activity 1', 'ctrl + shift + F1', 'Activity 2', 'ctrl + shift + F2', 'Activity 3', 'ctrl + shift + F3')
    # if the 'activities.json' file exists, read the data from it and assign it to the classes
    act1.name, act1.hotkey = preferences.read_json(1)
    act2.name, act2.hotkey = preferences.read_json(2)
    act3.name, act3.hotkey = preferences.read_json(3)
    # checks if there is a temp.json file and creates one if there is not
    if data.check_file('temp.json') == False:
        data.times_json_write(act1.hrs, act1.mins, act2.hrs, act2.mins, act3.hrs, act3.mins)
    # else read from the 'temp.json' file and assign the values to the classes
    else:
        act1.hrs, act1.mins, act2.hrs, act2.mins, act3.hrs, act3.mins = data.times_json_read()

    while True:
        print(act1)
        print(act2)
        print(act3)
        print()
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
            act = app.export_window(file)
            if act == 'export':
                sys.exit ("Exported data to excel file and deleted temp.json")
            break
        elif output == 'tracking':
            act = app.tracking_window(act1.name, act2.name, act3.name)
            if act == 'act1':
                minutes = app.record_window(act1.name, act1.hotkey)
                act1.add(minutes)
            elif act == 'act2':
                minutes = app.record_window(act2.name, act2.hotkey)
                act2.add(minutes)
            elif act == 'act3':
                minutes = app.record_window(act3.name, act3.hotkey)
                act3.add(minutes)
            break
        elif output == 'close':
            data.times_json_write(act1.hrs, act1.mins, act2.hrs, act2.mins, act3.hrs, act3.mins)
            # render a cute popup
            sys.exit("Exited with status 0")


if __name__ == '__main__':
    main()