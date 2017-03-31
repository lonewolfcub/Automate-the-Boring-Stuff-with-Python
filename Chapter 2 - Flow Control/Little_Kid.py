print('Hello World!')
print('What is your name?')
name = input()
if name == ('Alice'):
    print('Hi, Alice.')
else:
    print('Hi, ' + name)
    print('What is your age?:')
    age = input()
    if int(age) < 12:
        print('You are not Alice, Kiddo')
    else:
        print('You are neither Alice nor a little Kid')
        
