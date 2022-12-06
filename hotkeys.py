# Keyboard module in Python
import keyboard


def update_hotkey(act1, hot1, act2, hot2, act3, hot3):

    
print ('press ctrl+shift+g to print "Hotkey Detected"')
keyboard.add_hotkey('ctrl + shift + g', print, args =('Hotkey', 'Detected'))


keyboard.wait('ctrl + shift + f1')