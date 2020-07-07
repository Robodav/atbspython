import re

#TODO: Write function to isolate regex characters
def regexStrip(text, removing=' '):
    removingReg = re.compile(r'[%]')
