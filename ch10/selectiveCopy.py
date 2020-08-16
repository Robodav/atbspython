#! python3
# selectiveCopy.py - copies files with a specified extension to a specified folder

import os, shutil
from pathlib import Path
import pyinputplus as pyip

def selectiveCopy():
    # Walk through copyFrom folder tree and store paths
    copyFrom = pyip.inputFilepath(prompt='Enter the path of the folder to copy from:\n', mustExist=True)
    extension = pyip.inputRegex('[a-zA-Z]', prompt='Enter a file extension:\n')
    filePaths = []
    for root, dirs, files in os.walk(copyFrom):
        print(f'Checking {root}...')
        for f in files:
            if f.endswith(extension):
                filePath = Path(root) / f
                print(f'Copying {filePath}...')
                filePaths.append(filePath)

    # TODO: Copy files at stored paths to copyTo folder

selectiveCopy()