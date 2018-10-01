def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        newNum = num * 3 + 1
        print(newNum)
        return newNum


print('Enter number:')
num = int(input())

while num != 1:
    num = collatz(num)
