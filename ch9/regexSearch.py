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

#TODO: Find all matches in all text documents and print to the screen