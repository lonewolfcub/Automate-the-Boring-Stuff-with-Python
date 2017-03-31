
print('Hello World!')
print('What is your name?')
myName = input()
if myName == 'Alice':
    print('Hi, Alice.')
else:
    print('It is good to meet you, ' + myName)
    print('What is your age?')
    myAge = input()
    if int(myAge) < 12:
        print ('You are not Alice, kiddo.')
    elif int(myAge) > 2000:
        print ('Unlike you, Alice is not an undead, immortal vampire.')
    elif int(myAge) > 100:
        print ('You are not Alice, Grannie.')
