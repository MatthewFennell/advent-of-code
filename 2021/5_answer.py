import numpy
from common import getLineSplitOnManyChars

def partOne():
    lines = getLineSplitOnManyChars('5_input.txt', ' -> |,')
    # lines = [
    #     [0,9,5,9],
    #     [8,0,0,8],
    #     [9,4,3,4],
    #     [2,2,2,1],
    #     [7,0,7,4],
    #     [6,4,2,0],
    #     [0,9,2,9],
    #     [3,4,1,4],
    #     [0,0,8,8],
    #     [5,5,8,2]
    # ]
    maxGridSize = 1000
    myMap = numpy.zeros(shape=(maxGridSize,maxGridSize))

    for i in range(0, len(lines)):
        x1 = lines[i][0]
        y1 = lines[i][1]
        x2 = lines[i][2]
        y2 = lines[i][3]

        if (x1 == x2):
            start = y1 if y1 < y2 else y2
            end = y1 + 1 if y1 > y2 else y2 + 1
            for y in range(start, end):
                myMap[y, x1] += 1

        elif (y1 == y2):
            start = x1 if x1 < x2 else x2
            end = x1 + 1 if x1 > x2 else x2 + 1
            for x in range(start, end):
                myMap[y1, x] += 1


    numberOfOverlaps = 0
    for i in range(0, maxGridSize):
        for j in range(0, maxGridSize):
            if myMap[i][j] > 1:
                numberOfOverlaps +=1
    print("Part One:", numberOfOverlaps)

def partTwo():
    lines = getLineSplitOnManyChars('5_input.txt', ' -> |,')
    # lines = [
    #     [0,9,5,9],
    #     [8,0,0,8],
    #     [9,4,3,4],
    #     [2,2,2,1],
    #     [7,0,7,4],
    #     [6,4,2,0],
    #     [0,9,2,9],
    #     [3,4,1,4],
    #     [0,0,8,8],
    #     [5,5,8,2]
    # ]
    maxGridSize = 1000
    myMap = numpy.zeros(shape=(maxGridSize,maxGridSize))

    for i in range(0, len(lines)):
        x1 = lines[i][0]
        y1 = lines[i][1]
        x2 = lines[i][2]
        y2 = lines[i][3]

        if (x1 == x2):
            start = y1 if y1 < y2 else y2
            end = y1 + 1 if y1 > y2 else y2 + 1
            for y in range(start, end):
                myMap[y, x1] += 1

        elif (y1 == y2):
            start = x1 if x1 < x2 else x2
            end = x1 + 1 if x1 > x2 else x2 + 1
            for x in range(start, end):
                myMap[y1, x] += 1

        else:
            numberOfIterations = 0
            maxNumberOfIterations = min(abs(x1-x2), abs(y1-y2))
            yIncrement = 1 if y2 > y1 else -1
            xIncrement = 1 if x2 > x1 else -1
            currentX = x1
            currentY = y1
            while (numberOfIterations <= maxNumberOfIterations):
                numberOfIterations += 1
                myMap[currentY][currentX] += 1
                currentX += xIncrement
                currentY += yIncrement


    numberOfOverlaps = 0
    for i in range(0, maxGridSize):
        for j in range(0, maxGridSize):
            if myMap[i][j] > 1:
                numberOfOverlaps +=1
    print("Part Two:", numberOfOverlaps)

    
partOne()

partTwo()