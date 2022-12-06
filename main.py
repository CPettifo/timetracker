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
act3 = Activity("French", "ctrl + shift + F3")
file = ''
entries = 0

def main():
    # initialize the classes
    global act1, act2, act3, entries

    # check the user-settings.json file exists
    if data.check_file('activities.json') == False:
        preferences.write_json('Activity 1', 'ctrl + shift + F1', 'Activity 2', 'ctrl + shift + F2', 'Activity 3', 'ctrl + shift + F3', 0)
    # if the 'activities.json' file exists, read the data from it and assign it to the classes
    act1.name, act1.hotkey = preferences.read_json(1)
    act2.name, act2.hotkey = preferences.read_json(2)
    act3.name, act3.hotkey = preferences.read_json(3)
    entries = preferences.read_json(4)
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
        print(f"{entries} entries")
        print()
        #call on the logic function
        logic()

def logic():
    global act1, act2, act3, file, entries
    while True:
        # home_window returns 'change' to change the save directory
        # 'modify' to change settings
        # 'tracking' to start tracking
        # 'log' to view the log
        output = app.home_window()
        if output == 'change':
            file = app.file_path_window(file)
            print(file)
            #update the .json filepath folder
            data.filepath_update(file)
            break
        elif output == 'modify':
            act1.name, act2.name, act3.name = app.settings_window(act1.name, act2.name, act3.name)
            #update the .json file
            preferences.write_json(act1.name, act1.hotkey, act2.name, act2.hotkey, act3.name, act3.hotkey, entries)
            break
        elif output == 'log':
            app.log_window(act1.name, act1.hrs, act1.mins, act2.name, act2.hrs, act2.mins, act3.name, act3.hrs, act3.mins)
            break
        elif output == 'export':
            file = data.filepath_get()
            act = app.export_window(file)
            if act == 'export':
                data.times_json_kill()
                data.add_day_SQL(act1.name, act1.hrs, act1.mins, act2.name, act2.hrs, act2.mins, act3.name, act3.hrs, act3.mins)
                data.export_excel(file)
                preferences.write_json(act1.name, act1.hotkey, act2.name, act2.hotkey, act3.name, act3.hotkey, entries + 1)
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