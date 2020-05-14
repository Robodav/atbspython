def displayInventory(inventory):
    if type(inventory) != dict:
        return 'Please pass a dictionary as an inventory.'
    totalItems = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print("Total number of items: " + str(totalItems))

inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inventory1)