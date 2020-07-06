#! python3
# formatDates.py - Finds all dates on the clipboard and gives them the same format

import pyperclip, re

dateRegex = re.compile(r'''(
    ^(\d{1,2}|\d{1,4})    # First number
    (\s|\.|-)            # Separator
    (\d{1,2})              # Second number
    (\s|\.|-)            # Separator
    (\d{1,2}|\d{1,4})    # Third number
)''', re.VERBOSE)

#TODO: Find matches in clipboard text and re-format

#TODO: Copy results to the clipboard