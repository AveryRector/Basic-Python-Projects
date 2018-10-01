
tableData = [
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'mooose', 'goose']
            ]

def printTable(dataList):

    colWidth = max(dataList[0], key=len)
    print(colWidth)

    y = len(colWidth)

    for x in range(len(dataList[0])):
        print(str(dataList[0][x]).rjust(y) + str(dataList[1][x]).rjust(y) + str(dataList[2][x]).rjust(y))

printTable(tableData)
