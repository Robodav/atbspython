import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Create list of 100 'heads' or 'tails' values
    flips = []
    for i in range(100):
        result = random.randint(0,1)
        if result == 0:
            flips.append('H')
        else:
            flips.append('T')
    # Check if there is a streak of 6 heads or tails in a row
    for j in range(95):
        # Define which character to exclude
        if flips[j] == 'H':
            diffchar = 'T'
        else:
            diffchar = 'H'
        if diffchar not in flips[j:j+6]:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))