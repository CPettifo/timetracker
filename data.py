# responsible for saving the day's temporary data if user closes the main window
# will also interact with the .sql database, and write the excel file on export
import json
from os.path import exists

def check_file(file):
    if exists(file):
        return True
    else:
        return False

def times_json_write(hrs1, mins1, hrs2, mins2, hrs3, mins3):
    times = {
        "hrs1" : hrs1,
        "mins1": mins1,
        "hrs2" : hrs2,
        "mins2": mins2,
        "hrs3" : hrs3,
        "mins3": mins3
    }
    # throws this dict into the temp folder
    with open("temp.json", "w") as file_object:
        json.dump(times, file_object)

def times_json_read():
    with open("temp.json", "r") as file_object:
        times = json.load(file_object)
        return (times["hrs1"], times["mins1"], times["hrs2"], times["mins2"], times["hrs3"], times["mins3"])