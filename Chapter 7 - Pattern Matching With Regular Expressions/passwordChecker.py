#! /usr/bin/env python3
#This program checks the strength of a password

import re

#set regex patterns for relevant checks
uppercaseRegex = re.compile('[A-Z]+')
lowercaseRegex = re.compile('[a-z]+')
numberRegex = re.compile('[\d]+')

#define function to check password
def checkStrength(password):
#ensure password is at least 8 characters long
    if len(str(password)) <= 7:
        print('Your password must be at least 8 characters long.')
        return False
#ensure contains uppercase letter
    elif not uppercaseRegex.search(password):
        print('Your password must contain at least one uppercase letter.')
        return False
#ensure contains lowercase letter
    elif not lowercaseRegex.search(password):
        print('Your password muct contain at least one lowercase letter.')
        return False
#ensure contains number
    elif not numberRegex.search(password):
        print('Your password must contain at least one number.')
        return False
#if all checks passed
    else:
        return True

#prompt for password
print('Please enter the password you would like to check:')
password = input()

security = checkStrength(password)

#provide feedback
if security == False:
    print('Your password is not secure enough, please try again.')
else:
    print('Your password is acceptable.')
