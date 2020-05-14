def displayInventory(inventory):
    if type(inventory) != dict:
        print('Please pass a dictionary as an inventory.')
        return
    totalItems = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print("Total number of items: " + str(totalItems))

def addToInventory(inventory, addedItems):
    if type(inventory) != dict or type(addedItems) != list:
        print('Invalid arguments passed.')
        return
    for item in addedItems:
        inventory.setdefault(item, 0)
    for item in addedItems:
        inventory[item] += 1

inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inventory2 = 'hello!'

displayInventory(inventory1)
# displayInventory(inventory2)

adding1 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
adding2 = ['gold coin', 'dagger', 'dagger', 'bow', 'potion']
adding3 = 'hello!'

addToInventory(inventory1, adding1)
displayInventory(inventory1)

addToInventory(inventory1, adding2)
displayInventory(inventory1)

addToInventory(inventory1, adding3)
displayInventory(inventory1)    