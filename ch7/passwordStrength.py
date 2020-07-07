import re

regTest1 = re.compile(r'^(([a-z]{1,8})?|([a-z]{8,})?)$')
regTest2 = re.compile(r'^(([a-zA-Z]{1,8})?|([a-zA-Z]{8,})?)$')
regTest3 = re.compile(r'^(([a-zA-Z0-9]{1,8})?|([a-zA-Z0-9]{8,})?)$')

def passwordStrength(password):
    """Tests the given password on a 6-point scale"""
    match1 = regTest1.search(password) # Check lowest strength first since strong passwords won't match
    if match1 is not None:
        if match1.groups()[1] != None:
            return "Very weak..."
        elif match1.groups()[2] != None: # Slightly stronger if length longer than 8
            return "Weak."
    match2 = regTest2.search(password)
    if match2 is not None:
        if match2.groups()[1] != None:
            return "OK."
        elif match2.groups()[2] != None:
            return "Medium strength."
    match3 = regTest3.search(password)
    if match3 is not None:
        if match3.groups()[1] != None:
            return "Very strong!"
        elif match3.groups()[2] != None:
            return "Extremely strong!!!"

print(passwordStrength("lame"))
print(passwordStrength("abitlesslame"))
print(passwordStrength("Okay"))
print(passwordStrength("PrettyGood"))
print(passwordStrength("Great10"))
print(passwordStrength("SuperDuperGreat999"))