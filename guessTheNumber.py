import random

secretNum = random.randint(1, 20)
count = 0
print('I am thinking of a number between 1 and 20')

while True:
    print('Take a guess.')
    count += 1
    guessNum = int(input())

    if guessNum > secretNum:
        print('Too high')
    elif guessNum < secretNum:
        print('Too low')
    else:
        break

print('Good job you guesed my number in ' + str(count) + ' guesses!')
