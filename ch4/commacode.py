def commacode(l):
    listlen = len(l)
    if listlen >= 1:
        liststring = ''
        for i in range(listlen):
            item = ''
            if i == listlen - 1:
                if listlen > 1:
                    item += 'and ' + str(l[i])
                else:
                    item += str(l[i])
            else:
                item += str(l[i]) + ', '
            liststring += item
    else:
        return "ERROR: Tried to use an empty list!"
    return liststring

l1 = []
l2 = [1, 2, 3]
l3 = ['1', '2', '3']
l4 = ['eggs']
l5 = ['spam', 'eggs', 'bacon', 'nachos']

print(commacode(l1))
print(commacode(l2))
print(commacode(l3))
print(commacode(l4))
print(commacode(l5))