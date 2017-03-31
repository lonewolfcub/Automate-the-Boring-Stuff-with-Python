#! /usr/bin/env python3

import os

def findLargeFiles(folder):
    # iterate over search folder
    for dirpath, dirnames, filenames in os.walk(folder):
        # check each file to see if over 100mb
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            filesize = os.path.getsize(filepath)
            if filesize > 13107200:
                print (filepath + ' ' + str(filesize) + ' bytes')

# define search folder
print('Please enter the folder you wish to search:')
folder = input()

findLargeFiles(folder)
