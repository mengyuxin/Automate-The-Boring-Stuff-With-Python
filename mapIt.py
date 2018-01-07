#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard.
    address = pyperclip.paste()

if address == '':
    webbrowser.open('http://map.baidu.com/')
else:
    webbrowser.open('http://map.baidu.com/?s=con%26from%3Dalamap%26tpl%3Dmapcity%26wd%3D' + address + '%26c%3D167')
