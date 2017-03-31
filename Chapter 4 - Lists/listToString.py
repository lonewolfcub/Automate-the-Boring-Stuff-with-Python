def listToString(myList):
    for i in myList[0:-1]:
        print(i + ', ', end='')
    print('and ' + myList[-1])

myList = []
while input != '':
    listItem = input('Please define your List (Sumbit a blank entry to end):')
    myList.append(listItem)
if input == '':
    break
listToString(myList)
