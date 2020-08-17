#! python3
# unneededFiles.py - Finds all files larger than a specified threshold
# in a directory walk and prints their paths to the screen

import os
from pathlib import Path
import pyinputplus as pyip 

# Get walking directory and min file size from user
walking = pyip.inputFilepath(prompt='Enter the directory to search:\n', mustExist=True)
fileSize = pyip.inputNum(prompt='Enter the minimum file size (mb):\n')
fileSize = fileSize * 1000000 # convert to bytes

# Walk directory and print file paths to screen
for root, dirs, files in os.walk(walking):
    for f in files:
        checkPath = Path(root) / f
        if os.path.getsize(checkPath) >= fileSize:
            print(checkPath)