#! python3
# madlibs.py - madlibs game program using user input and text files

from pathlib import Path
import pyinputplus as pyip
import re

# Read mad libs text file
selection = pyip.inputMenu(['1', '2', '3'])
madlibFile = open(Path.cwd() / f'madlibs{selection}.txt')
madlibContent = madlibFile.read()

# Find replacement occurrences and prompt user to write over them
replacementRegex = re.compile(r'''(NOUN|ADJECTIVE|VERB|ADVERB)''')
splitLib = replacementRegex.split(madlibContent)


#TODO: Print results to screen and save to new text file