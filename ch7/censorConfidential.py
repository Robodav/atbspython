#! python3
# censorConfidential.py - censors social security and credit card numbers

import pyperclip, re

# Finds social security numbers
socialRegex = re.compile(r'''(
    (\d{3})    # First 3 numbers
    (\s|-|/)   # Separator
    (\d{2})    # Middle 2 numbers
    (\s|-|/)   # Separator
    (\d{4})    # Last 4 numbers
)''', re.VERBOSE)

cardRegex = re.compile(r'''(
    (\d{4})     # First 4 numbers
    (\s|-|/)?   # Separator
    (\d{4})     # Second 4 numbers
    (\s|-|/)?   # Separator
    (\d{4})     # Third 4 numbers
    (\s|-|/)?   # Separator
    (\d{4})     # Last 4 numbers
)''', re.VERBOSE)

#TODO: Censor copied text

#TODO: Paste censored text to clipboard