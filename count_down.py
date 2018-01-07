#! python3
# count_down.py - A simple countdown script.

import time, subprocess

time_left = int(input('Enter a number:'))

while time_left > 0:
    print(time_left, end = ' | ')
    time.sleep(1)
    time_left -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
