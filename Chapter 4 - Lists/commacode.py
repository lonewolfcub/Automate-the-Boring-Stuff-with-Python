#! /usr/bin/env python3
# commacode.py

def commacode(mylist):
    for i in mylist[0:-1]:
        print(i + ', ', end='')
    print('and ' + mylist[-1] + '.')
    
spam = ['apples', 'bananas', 'tofu', 'cats']

commacode(spam)
