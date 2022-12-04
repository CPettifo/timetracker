#This will have the functions for timing, and show popups
import time

start = time.time()
minutes = 0
tensecs = time.time()
while True:
    if time.time() - start > 60:
        minutes += 1
        print(f"{minutes} minutes have passed")
        start = time.time()
    if time.time() - tensecs > 10:
        print('Ten seconds have passed')
        tensecs = time.time()