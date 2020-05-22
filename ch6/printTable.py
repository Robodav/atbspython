def printTable(tableData):
    colWidths = [0] * len(tableData) # Store the lenghts of the longest strings
    for i in range(len(colWidths)): 
        largest = 0
        for val in tableData[i]:
            if len(val) > largest:
                largest = len(val)
                colWidths[i] = len(val)
    
    longestList = 0 # Find the longest list for iteration
    for i in range(len(tableData)):
        if len(tableData[i]) > longestList:
            longestList = len(tableData[i])

    for i in range(longestList):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print('\n')
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)