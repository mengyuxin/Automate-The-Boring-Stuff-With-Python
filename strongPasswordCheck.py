# python3
# strongPasswordCheck.py

import re

print('Enter a password:')
password = input()

regex = re.match(r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,}$', password)

print(regex)

