#! python3
# madlibs.py - madlibs game program using user input and text files

from pathlib import Path
import pyinputplus as pyip
import re

# Read mad libs text file
selection = pyip.inputMenu(['1', '2', '3'])
madlibFile = open(Path.cwd() / f'madlibs{selection}.txt')
madlibContent = madlibFile.read()
madlibFile.close()

# Find replacement occurrences and prompt user to write over them
replacementRegex = re.compile(r'''(NOUN|ADJECTIVE|VERB|ADVERB)''')
splitLib = replacementRegex.split(madlibContent)
modifiedLib = ""
for word in splitLib:
    if word not in ["NOUN", "ADJECTIVE", "VERB", "ADVERB"]:
        modifiedLib += word
    else:
        replacement = pyip.inputStr(f'Enter a(n) {word.lower()}:\n') # Prompt user with part of speech
        modifiedLib += replacement

# Print results to screen and save to new text file
modifiedFile = open(f'modifiedLib{selection}.txt', 'w')
modifiedFile.write(modifiedLib)
modifiedFile.close()

print(modifiedLib)