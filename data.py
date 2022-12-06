# responsible for saving the day's temporary data if user closes the main window
# will also interact with the .sql database, and write the excel file on export
import json, os, xlsxwriter
from datetime import date
from os.path import exists
from cs50 import SQL
import preferences

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
    entries = preferences.read_json(4)
    if entries == 0:
        db.execute('''
            CREATE TABLE times (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                act1 TEXT NOT NULL,
                hrs1 TEXT NOT NULL,
                mins1 TEXT NOT NULL,
                act2 TEXT NOT NULL,
                hrs2 TEXT NOT NULL,
                mins2 TEXT NOT NULL,
                act3 TEXT NOT NULL,
                hrs3 TEXT NOT NULL,
                mins3 TEXT NOT NULL
            )
        ''')


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

def export_excel(file):
    # Read SQL database, export into an excel spreadsheet
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()
    entries = preferences.read_json(4)
    row = 0
    col = 0
    headings = ["Entry #", "Date", "Activity 1", "Hours", "Minutes", "Activity 2", "Hours", "Minutes", "Activity 3", "Hours", "Minutes"]
    timelist = [3, 4, 6, 7, 9, 10]
    for item in (headings):
        worksheet.write(row, col, item)
        col += 1
    row = 0
    for x in range(entries + 1):
        row += 1
        col = 0
        x += 1
        rawdata = str(db.execute("SELECT * FROM times WHERE id = ?", x))
        counter = 0
        data = []
        rawdata = rawdata.strip('"[]}{')
        data = rawdata.split(',')
        for x in data:
            string = str(data[counter])
            split = string.split(':')
            item = str(split[1])
            item = item.replace("'", '')
            item = item.strip()
            data[counter] = item
            if counter in timelist:
                data[counter] = int(data[counter])
            counter += 1

        for item in (data):
            worksheet.write(row, col, item)
            col += 1

    workbook.close()