#! python3
# bulletPointAdder.py - Adds Wikimedia bullet points to the start
# o feach line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
text = '\n'.join(lines)
pyperclip.copy(text)
