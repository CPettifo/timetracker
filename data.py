# responsible for saving the day's temporary data if user closes the main window
# will also interact with the .sql database, and write the excel file on export
import json, os
from datetime import date
from os.path import exists
from cs50 import SQL

def check_file(file):
    if exists(file):
        return True
    else:
        return False

def filepath_update(filepath):
    with open("filepath.json", "w") as file_object:
        json.dump(filepath, file_object)

def filepath_get():
    with open("filepath.json", "r") as file_object:
        filepath = json.load(file_object)
        return filepath

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

def times_json_kill():
    os.remove("temp.json")

db = SQL("sqlite:///log.db")

def add_day_SQL(act1, hrs1, mins1, act2, hrs2, mins2, act3, hrs3, mins3):
    db.execute("INSERT INTO times (date, act1, hrs1, mins1, act2, hrs2, mins2, act3, hrs3, mins3) VALUES(:date, :act1, :hrs1, :mins1, :act2, :hrs2, :mins2, :act3, :hrs3, :mins3)",
                date = str(date.today()),
                act1 = act1,
                hrs1 = hrs1,
                mins1 = mins1,
                act2 = act2,
                hrs2 = hrs2,
                mins2 = mins2,
                act3 = act3,
                hrs3 = hrs3,
                mins3 = mins3)

def export_excel():
    # Read SQL database, export into an excel spreadsheet
    25 + 3