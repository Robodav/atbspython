#! python3
# findURLs.py - Finds all website URLs on the clipboard and copies them

import pyperclip, re

urlRegex = re.compile(r'''(
    (http://|https://)?     # protocol
    (www\.)?
    ([a-zA-Z0-9-]+)           # site name
    (\.[a-zA-Z]{2,4})       # dot something
    (\.[a-zA-Z]{2,4})?      # optional dot something
    (/[a-zA-Z.-]+)?
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in urlRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URLs found.')