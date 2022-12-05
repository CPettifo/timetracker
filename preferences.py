# This file allows for the changing of names and hotkeys for the different activities
import json
from os.path import exists

#check if file exists
def check_file():
    filename = 'activities.json'
    if exists(filename):
        return True
    else:
        return False


#write to file
def write_json(name1, hotkey1, name2, hotkey2, name3, hotkey3):        
    activity = {
        "name1" : name1,
        "hotkey1" : hotkey1,
        "name2" : name2,
        "hotkey2" : hotkey2,
        "name3" : name3,
        "hotkey3" : hotkey3
    }
    with open('activities.json', 'w') as file_object:
        json.dump(activity, file_object)

#read from file
def read_json(n):
    with open('activities.json', 'r') as file_object:
        data = json.load(file_object)
    if n == 1:
        return (data["name1"], data["hotkey1"])
    elif n == 2:
        return (data["name2"], data["hotkey2"])
    elif n == 3:
        return (data["name3"], data["hotkey3"])


while __name__ == '__main__':
    check_file()
    write_json('coding', 'shift', 'french', 'ctrl', 'reading', 'space')
    read_json('activities.json')