import re

def regexStrip(text, removing=' '):
    """Same function as python's .strip() method, uses regex"""
    removingReg = re.compile(rf'{removing}*(.*?){removing}*$')
    matched = removingReg.search(text)
    return matched.group(1)

# test1 = "             boneless              "
# test2 = "           bone              less            "
# test3 = "0000000000bone00000000000000less00000000000000"
# test4 = "boneless"

# print(regexStrip(test1))
# print(regexStrip(test2))
# print(regexStrip(test3, '0'))
# print(regexStrip(test4))