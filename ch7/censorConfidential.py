#! python3
# censorConfidential.py - censors social security and credit card numbers

import pyperclip, re

socialRegex = re.compile(r'''(
    (\d{3})    # First 3 numbers
    (\s|-|/)   # Separator
    (\d{2})    # Middle 2 numbers
    (\s|-|/)   # Separator
    (\d{4})    # Last 4 numbers
)''', re.VERBOSE)

#TODO: Credit card number regex

#TODO: Censor copied text

#TODO: Paste censored text to clipboard