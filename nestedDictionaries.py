allGuest = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}#,
            #'Dog': 'None'
            }

def totalBrought(guest, item):
    numBrought = 0
    for k, v in guest.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Apples: ' + str(totalBrought(allGuest, 'apples')))
print('Cups: ' + str(totalBrought(allGuest, 'cups')))
print('Cakes: ' + str(totalBrought(allGuest, 'cakes')))
print('Ham Sandwiches: ' + str(totalBrought(allGuest, 'ham sandwiches')))
print('Apple pies: ' + str(totalBrought(allGuest, 'apple pies')))
