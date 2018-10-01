import copy

spam = [1, 2, 3, 4]
eggs = copy.copy(spam)

eggs[1] = 'Holy fuck'

print(spam)
print(eggs)
