#! python3
# censorConfidential.py - censors social security and credit card numbers

import pyperclip, re

# Finds social security numbers
socialRegex = re.compile(r'''(
    (\d{3})    # First 3 numbers
    (\s|-|/)   # Separator
    (\d{2})    # Middle 2 numbers
    (\s|-|/)  # Separator
    (\d{4})    # Last 4 numbers
)''', re.VERBOSE)

# Finds credit card numbers
cardRegex = re.compile(r'''(
    (\d{4})     # First 4 numbers
    (\s|-|/)?   # Separator
    (\d{4})     # Second 4 numbers
    (\s|-|/)?   # Separator
    (\d{4})     # Third 4 numbers
    (\s|-|/)?   # Separator
    (\d{4})     # Last 4 numbers
)''', re.VERBOSE)

text = str(pyperclip.paste())

newText = socialRegex.sub('***-**-****', text)
newerText = cardRegex.sub('****-****-****-****', newText)

pyperclip.copy(newerText)
print('Copied to clipboard: ' + newerText)