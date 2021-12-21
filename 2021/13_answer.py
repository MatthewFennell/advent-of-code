from common import getLinesAsNumberArrays, getLinesSplitOnChar
import numpy

def partOne():
    lines = getLinesAsNumberArrays('13_input.txt')
    folds = getLinesSplitOnChar('13_folds.txt', 'fold along ')
    temp=[]
    order=[]
    for x in folds:
        temp.append(x[1])
    for x in temp:
        s = x.split('=')
        num = int(s[1])
        order.append([s[0], num])
    myPaper = []
    maxX = 0
    maxY = 0
    for x in lines:
        maxX = max(maxX, x[0])
        maxY = max(maxY, x[1])
    myMap = []
    for row in range(0, maxY+1):
        tempRow = []
        for column in range(0, maxX+1):
            tempRow.append(0)
        myMap.append(tempRow)
    for x in lines:
        myMap[x[1]][x[0]] = 1

    for cut in order:
        if cut[0] == 'y':
            del myMap[cut[1]]

            numberOfOperations = min(cut[1], len(myMap)-cut[1])
            # print("Number of op", numberOfOperations)
            for y in range(0, numberOfOperations):
                for x in range(0, len(myMap[0])):
                    y_val = cut[1] + y
                    original_y = cut[1]-1-y
                    # print("")
                    # print ("number of rows", len(myMap))
                    # print("number of cols", len(myMap[0]))
                    # print("accessing", y_val, original_y, x)
                    myMap[original_y][x] = min(1, myMap[y_val][x] + myMap[original_y][x])
            myMap=myMap[0:cut[1]]

            numDots = 0
            for x in myMap:
                for y in x:
                    numDots += y
        if cut[0] == 'x':
            for x in range(0, len(myMap)):
                del myMap[x][cut[1]]
            numberOfOperations = min(cut[1], len(myMap[0])-cut[1])

            for x in range(0, numberOfOperations):
                for y in range(0, len(myMap)):
                    x_val = cut[1] + x
                    original_x = cut[1]-1-x
                    myMap[y][original_x] = min(1, myMap[y][x_val] + myMap[y][original_x])
            for x in range(0, len(myMap)):
                myMap[x] = myMap[x][0:cut[1]]

    numDots = 0
    result=[]
    for x in myMap:
        temp = []
        for y in x:
            if y == 0:
                temp.append(' ')
            else:
                temp.append('#')
        result.append(temp)
    print("Part One:", numDots)
    for x in result:
        print (x)
partOne()

#, , ,#, , , ,#,#, ,#,#,#, , ,#, , ,#, ,#,#,#,#, ,#, , ,#, ,#,#,#, , , ,#,#, , 
#, ,#, , , , , ,#, ,#, , ,#, ,#, ,#, , ,#, , , , ,#, , ,#, ,#, , ,#, ,#, , ,#, 
#,#, , , , , , ,#, ,#,#,#, , ,#,#, , , ,#,#,#, , ,#, , ,#, ,#,#,#, , ,#, , , , 
#, ,#, , , , , ,#, ,#, , ,#, ,#, ,#, , ,#, , , , ,#, , ,#, ,#, , ,#, ,#, ,#,#, 
#, ,#, , ,#, , ,#, ,#, , ,#, ,#, ,#, , ,#, , , , ,#, , ,#, ,#, , ,#, ,#, , ,#, 
#, , ,#, , ,#,#, , ,#,#,#, , ,#, , ,#, ,#,#,#,#, , ,#,#, , ,#,#,#, , , ,#,#,#, 