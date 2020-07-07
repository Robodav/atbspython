#! python3
# formatDates.py - Finds all dates on the clipboard and gives them the same format

import pyperclip, re

dateRegex = re.compile(r'''(
<<<<<<< HEAD
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
=======
    ^(\d{1,2}|\d{1,4})    # First number
    (\s|\.|-)            # Separator
    (\d{1,2})              # Second number
    (\s|\.|-)            # Separator
    (\d{1,2}|\d{1,4})    # Third number
)''', re.VERBOSE)

#TODO: Find matches in clipboard text and re-format

#TODO: Copy results to the clipboard
>>>>>>> f51c025bfec0074b42b6ed5d07a723b4509b3e8c
