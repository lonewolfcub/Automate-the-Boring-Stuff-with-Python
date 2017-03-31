#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to the clipboard
#        py.exe mcb.pyw list - loads all keywords to the clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete keyword
elif len(sys.argv) == 3 and sys.argv[1].lower == 'delete' and sys.argv[2].lower in mcbShelf.keys():
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
# List keywords and load content
    if sysargv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
# Delete all keywords
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf
# Copy keyword value
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
