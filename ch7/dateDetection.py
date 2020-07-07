#! python3 
# dateDetection.py - detects dates in DD/MM/YYYY format and validates

import re

dateRegex = (r'''(
    [0-3][0-9]/    # Day
    [0-1][0-2]/    # Month
    [1-2][0-9]{3}    # Year
)''', re.VERBOSE)

#TODO: Store month/day/year into variables

#TODO: Detect if valid date