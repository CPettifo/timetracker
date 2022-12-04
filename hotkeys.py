# Keyboard module in Python
import keyboard

print ('press ctrl+shift+g to print "Hotkey Detected"')
keyboard.add_hotkey('ctrl + shift + g', print, args =('Hotkey', 'Detected'))


keyboard.wait('ctrl + shift + f1')