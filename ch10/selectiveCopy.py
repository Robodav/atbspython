#! python3
# selectiveCopy.py - copies files with a specified extension to a specified folder

import os, shutil
from pathlib import Path
import pyinputplus as pyip

def selectiveCopy():
    # Walk through copyFrom folder tree and store paths
    copyFrom = pyip.inputFilepath(prompt='Enter the path of the folder to copy from:\n', mustExist=True)
    extension = pyip.inputRegex('[a-zA-Z]', prompt='Enter a file extension:\n')
    copyTo = Path(pyip.inputFilepath(prompt='Enter the path of the folder to copy to:\n'))
    if not Path.is_dir(copyTo):
        os.makedirs(copyTo) # make the destination directory
    filePaths = []
    for root, dirs, files in os.walk(copyFrom):
        print(f'Checking {root}...')
        for f in files:
            if f.endswith(extension):
                filePath = Path(root) / f
                filePaths.append(filePath)

    # Copy files at stored paths to copyTo folder
    for filePath in filePaths:
        print(f'Copying {filePath}...')
        shutil.copy(filePath, copyTo)

selectiveCopy()