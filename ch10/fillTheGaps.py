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
prefixregex = re.compile(rf'({prefix}[0]*)(\d+)(.*)')

# Loop through the directory, saving information to a dictionary
files = os.listdir(organizing)
fileData = {}
for f in files:
    matched = prefixregex.match(f)
    if matched is not None:
        fileData[matched.group(2)] = [matched.group(1), matched.group(3)]

# Strip and sort all numbers matched, saving them to a list
fileNums = list(fileData.keys())
for i in range(len(fileNums)):
    fileNums[i] = int(fileNums[i].lstrip('0'))
fileNums.sort()

# Loop through saved numbers and find gaps, renaming associated files
for i in range(len(fileNums)-1):
    if not fileNums[i+1] == fileNums[i] + 1:
        renaming = fileNums[i+1]
        rootPath = Path(organizing)
        prefix = fileData[str(renaming)][0]
        extension = fileData[str(renaming)][1]
        oldPath = rootPath / f'{prefix}{renaming}{extension}'
        newPath = rootPath / f'{prefix}{fileNums[i] + 1}{extension}'
        print(f'Renaming {oldPath} to {newPath}')
        # shutil.move(oldPath, newPath) # uncomment after testing
        fileNums[i+1] = fileNums[i] + 1