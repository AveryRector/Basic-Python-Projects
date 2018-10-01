
nums = []

print('Enter numbers ill add them to a list just type 0 and ill know youre finished: ')
while True:
    number = int(input())
    if number == 0:
        break
    nums.append(number)

for i in nums:
    if i < 5:
        print(i, end='. ')
