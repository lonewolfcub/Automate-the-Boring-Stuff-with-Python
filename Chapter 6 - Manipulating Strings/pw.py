#! /usr/bin/env python3

# pw.py - An insecure password locker program

PASSWORDS = {'email': 'password', 'blog': 'anotherbadpassword', 'luggage': '12345'}

import pyperclip
import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
