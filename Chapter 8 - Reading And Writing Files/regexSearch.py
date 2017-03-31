import re
import os

#prompt for input
print('Please enter the REGEX you wish to search for:')
userRegex = input()

#convert input to regex

searchRegex = re.compile(userRegex)

#open files in cwd

for i in os.listdir(os.getcwd()):
    if i.endswith('.txt'):
        open(i, 'r')
        for line in i:
            if searchRegex.search == True:
                print (line)             
                break
        else:
            print('Regex did not match in file ' + i)
#       print(i)
        

#search for regex in files

#capture lines where regex matches

#print lines to screen
