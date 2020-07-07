import re

#TODO: Define multiple regex's for password strength
regTest1 = re.compile(r'^(([a-z]{1,8})?|([a-z]{8,})?)$')
regTest2 = re.compile(r'^(([a-zA-Z]{1,8})?|([a-zA-Z]{8,})?)$')
regTest3 = re.compile(r'^(([a-zA-Z0-9]{1,8})?|([a-zA-Z0-9]{8,})?)$')

#TODO: Determine strength based on regex matching