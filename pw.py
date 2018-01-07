#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': '11111111111111111',
            'blog': '222222222222222',
            'web': '333333333333333333',
            'wexin': 'aaaaaaaaaaaaaaaaa'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
