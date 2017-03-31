#Load Madlib file

madlib = open('./madlib.txt')
madContent = madlib.read()

#Enter value for adjective
print('Enter an Adjective:')
userAdjective1 = input()
#Enter value for nounLazy
print('Enter a Noun:')
userNoun1 = input()
#Enter value for verb
print('Enter a verb:')
userVerb1 = input()
#Enter value for noun
print('Enter a noun:')
userNoun2 = input()

#Replace values
madContent = madContent.replace('ADJECTIVE', userAdjective1, 1)
madContent = madContent.replace('NOUN', userNoun1, 1)
madContent = madContent.replace('VERB', userVerb1, 1)
madContent = madContent.replace('NOUN', userNoun2, 1)

#Save to file
madlibResultFile = open('madlibsResult.txt', 'w')
madlibResultFile.write(madContent)
madlibResultFile.close()

#Print madlib
print(madContent)
