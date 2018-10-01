
number = int(input('Enter a number and ill give you all of its divors: '))

for i in range(number / 2):
    if number % i == 0:
        print('|%d| '%i)
