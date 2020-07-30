#! python3
# madlibs.py - madlibs game program using user input and text files

from pathlib import Path
import pyinputplus as pyip

#Read mad libs text file
selection = pyip.inputMenu(['1', '2', '3'])
madlibFile = open(Path.cwd() / f'madlibs{selection}.txt')
madlibContent = madlibFile.read()

#TODO: Find replacement occurrences and prompt user to write over them

#TODO: Print results to screen and save to new text file