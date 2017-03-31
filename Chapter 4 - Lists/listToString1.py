def listToString(myList):
    for i in myList[0:-1]:
        print(i + ', ', end='')
    print('and ' + myList[-1])

myList = ['Spam', 'Eggs', 'Spam', 'Bacon', 'Spam', 'Ham', 'Spam']
listToString(myList)
