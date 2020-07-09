import pyinputplus as pyip

breadchoices = ['wheat', 'white', 'sourdough']
bread = pyip.inputMenu(breadchoices, numbered=True)
print('Got it, ' + bread + ' bread.')

proteinchoices = ['chicken', 'turkey', 'ham', 'tofu']
protein = pyip.inputMenu(proteinchoices, numbered=True)
print('Okay, ' + protein + '.')

wantCheese = pyip.inputYesNo(prompt='Would you like cheese?\n')
if wantCheese:
    cheesechoices = ['cheddar', 'swiss', 'mozarella']
    cheese = pyip.inputMenu(cheesechoices, numbered=True)

wantMayo = pyip.inputYesNo(prompt='Do you want mayo?\n')
wantMustard = pyip.inputYesNo(prompt='Mustard?\n')
wantLettuce = pyip.inputYesNo(prompt='Lettuce?\n')
wantTomato = pyip.inputYesNo(prompt='Tomato?\n')

numSandwiches = 