#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any line
#                  that matches a user-specified regex

from pathlib import Path
import pyinputplus as pyip
import re
# Find all text files in a specified directory
directory = Path(pyip.inputFilepath(prompt='Enter a valid directory:\n', mustExist=True))
textFiles = list(directory.glob('*.txt'))

# Get a regex input from the user
reg = pyip.inputRegexStr(prompt='Enter a regex to match:\n')

# Find all matches in all text documents and print to the screen
for t in textFiles:
    pattern = re.compile(reg)

    searching = open(t)
    searchingContent = searching.read()
    searching.close()

    matches = pattern.findall(searchingContent)
    if len(matches) == 0:
        print(f'No matches found in {t}.')
    else:
        print(f'Matches found in {t}:')
        for match in matches:
            print(match)
