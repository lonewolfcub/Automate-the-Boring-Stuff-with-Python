import re

#regex for selecting word
selectStringRegex = re.compile(r'\s*(\S+(\s\S+)*)\s*')

#prompt for input
print('Please input a string:')
userString = input()

stripped = selectStringRegex.search(userString)
print(stripped.group(1))
