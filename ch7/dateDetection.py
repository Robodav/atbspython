#! python3 
# dateDetection.py - detects dates in DD/MM/YYYY format and validates

import re

dateRegex = re.compile(r'''(
    ([0-3][0-9])/    # Day
    ([0-1][0-9])/    # Month
    ([1-2][0-9]{3})    # Year
)''', re.VERBOSE)

def dateDetection(text):
    matches = dateRegex.findall(text)
    print(matches)

#TODO: Detect if valid date

text = "01/01/1999, 02/03/2000, 05/20/1970, 2/4/40, 09/09/0004"
dateDetection(text)