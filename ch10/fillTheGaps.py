#! python3
# fillTheGaps.py - finds all files with a given prefix and locates gaps in
# the numbering, filling them to fix the sequence

import os, shutil
from pathlib import Path
import pyinputplus as pyip 
import re

# Get the directory containing the files with the given prefix from the user
organizing = pyip.inputFilepath(prompt='Enter the folder to search:\n', mustExist=True)
prefix = pyip.inputStr(prompt='Enter the prefix of each file:\n')
prefixregex = re.compile(rf'{prefix}(\d+)')

# Loop through the directory, saving numbers to a list
files = os.listdir(organizing)
fileNums = []
for f in files:
    matched = prefixregex.match(f)
    if matched is not None:
        fileNums.append(int(matched.group(1).lstrip('0')))

fileNums.sort()
print(fileNums)