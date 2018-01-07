#! python3
# printTable.py

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['Dalian', 'Beijing', 'Nanjing', 'Tokyo'],
             ['Red', 'Yellow', 'White', 'Black'],
             ['Accenture', 'IBM', 'HP', 'SAP']]

def colWidth(tableData):
    colWidths = [0]*len(tableData)
    for col in range(len(tableData)):
        for item in tableData[col]:
            if len(item) > colWidths[col]:
                colWidths[col] = len(item)
    return colWidths

def printTable(tableData):
    length = colWidth(tableData)

    print('row = ' + str(len(tableData[0])), end = ',')
    print('col = ' + str(len(tableData)))
    
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].ljust(length[col]), end = ' ')
        print('')

printTable(tableData)
    
