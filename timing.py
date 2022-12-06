#This will have the functions for timing, and show popups
import time
import keyboard
import sys


#keyboard.add_hotkey('ctrl + shift + g', print, args =(False))

def quit():
    global exit_value
    exit_value = 1

exit_value = 0

def record_time(hotkey):
    global exit_value
    exit_value = 0
    start = time.time()
    minutes = 0
    tensecs = time.time()
    keyboard.add_hotkey(hotkey, quit)
    while exit_value == 0:
        if time.time() - start > 60:
            minutes += 1
            start = time.time()
        if time.time() - tensecs > 10:
            print (time.time() - start)
            tensecs = time.time()
    return minutes

#How to call the function    
#minutes = record_time('ctrl + shift + F1')

#print()
#print(f'{minutes} minutes elapsed')
