#! /usr/bin/env python3

# selectiveCopy.py - a program that walks through a folder tree and copies
# files with a specified extension to a new location

import shutil, os

def selectiveCopy(folder, extension, destination):

    # ensure folder is absolute
    src = os.path.abspath(folder)
    dst = os.path.abspath(destination)
    
    # iterate over search folder to identify files
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(extension):
                # copy files to new location
                print('Moving ' + file + ' from %s to %s...' % (src, dst))
                shutil.move(os.path.join(src, file), dst) # uncomment after test
    print('Done')

# Specify folder to search
print ('Please specify the folder you wish to search:')
folder = input()
# Specify extension to search for
print ('Please specify the file extension you wish to move:')
extension = input()
# Specify new location
print ('Please specify the folder you wish these files to be copied to:')
destination = input()

selectiveCopy(folder, extension, destination)

