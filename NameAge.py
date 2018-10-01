userName = input('Enter your name: ')
userAge = int(input('Enter your age: '))
number = int(input('How many times would you like this? '))

def hello(name, age):
    return 'Hello %s you are %d years old' % (name, age)

for i in range(number):
    print(hello(userName, userAge))
