#! python3
# findURLs.py - Finds all website URLs on the clipboard and copies them

import pyperclip, re

urlRegex = re.compile(r'''(
    (http://|https://)?     # protocol
    (www.)?
    [a-zA-Z0-9-]+           # site name
    (\.[a-zA-Z]{2,4})       # dot something
    (\.[a-zA-Z]{2,4})?      # optional dot something
)''', re.VERBOSE)