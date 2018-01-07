#! python3
# getFilenames.py - Get all of the current folder.
import os

for foldername, subfolders, filenames in os.walk('D:\Study'):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('SUBFOLDER of ' + foldername + ': ' + subfolder)
        
    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)
    print('')
