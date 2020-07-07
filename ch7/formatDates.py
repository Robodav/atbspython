#! python3
# formatDates.py - Finds all dates on the clipboard and gives them the same format

import pyperclip, re

dateRegex = re.compile(r'''(
    (\d{1,4})    # First number
    (\.|-|/)            # Separator
    (\d{1,2})              # Second number
    (\.|-|/)            # Separator
    (\d{1,4})    # Third number
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in dateRegex.findall(text):
    dateValues = [groups[1], groups[3], groups[5]]
    newDate = '-'.join(dateValues)
    matches.append(newDate)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found.')