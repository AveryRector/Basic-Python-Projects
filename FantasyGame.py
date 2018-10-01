inventory = {'gold': 5, 'rope': 6, 'arrow': 35}

def displayInventory(bag):
    print('Inventory')
    totalItems = 0
    for k, v in bag.items():
        print(k + ' ' + str(v))
        totalItems += 1
    print('The total number of items %d' % totalItems)

def addToInventory(inv, addedItems):
    for item in addedItems:
        if item in inv.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1




dragonLoot = ['gold', 'dagger', 'gold', 'ruby']
#inventory = addToInventory(inventory, dragonLoot)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
print(inventory)
