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
    for match in matches:
        if checkDate(match):
            print("VALID: " + match[0])
        else:
            print("INVALID: " + match[0])

def checkDate(date):
    try:
        day = int(date[1])
        month = int(date[2])
        year = int(date[3])
    except:
        print('Please enter a valid date')
        return False
    if month in [4,6,9,11]:
        if day > 30:
            return False
    elif month == 2:
        if day > 28:
            if day == 29: # February 29 only on leap years
                if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    return False
            else:
                return False
    else:
        if day > 31:
            return False
    return True

text = "01/01/1999, 02/03/2000, 05/20/1970, 2/4/40, 09/09/0004"
dateDetection(text)