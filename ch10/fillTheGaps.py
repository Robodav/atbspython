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

# Loop through the directory, renaming files in the sequence
files = os.listdir(organizing)
for f in files:
    if f.startswith(prefix):
        print(f)