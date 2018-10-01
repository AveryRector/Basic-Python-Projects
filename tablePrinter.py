
tableData = [
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'mooose', 'goose']
            ]

def printTable(dataList):

    colWidth = [0] * len(dataList)

    for i in colWidth:
        colWidth = max(dataList[i], key=len)

    y = len(colWidth)

    for x in range(len(dataList[0])):
        print(str(dataList[0][x]).rjust(y) + str(dataList[1][x]).rjust(y) + str(dataList[2][x]).rjust(y))

printTable(tableData)
