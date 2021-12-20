from common import getLinesAsArray

myUpdates = []

def updateFlashes(row, col, lines, updates):
    # print("row col val", row, col, lines[row][col])
    # print(updates)
    numRows = len(lines)  - 1
    numCols = len(lines[0])  - 1
    if (row > 0):
        # above
        lines[row-1][col] +=1
        # print("Increasing above")
        if (lines[row-1][col]) == 10:
            updateFlashes(row-1, col, lines, updates + [[row-1, col]])
            # myUpdates = myUpdates + [[row-1, col]]
        
        # up left
        if (col > 0):
            # print("Increasing left above")
            lines[row-1][col-1] += 1
            if (lines[row-1][col-1] == 10):
                updateFlashes(row-1, col-1, lines, updates + [[row-1, col-1]])
                # myUpdates += [[row-1, col-1]]
                
        # up right
        if (col < numCols):
            # print("Increasing right above")
            lines[row-1][col + 1] += 1
            if (lines[row-1][col+1] == 10):
                updateFlashes(row-1, col+1, lines, updates + [[row-1, col+1]])
                # myUpdates += [[row-1, col+1]]

    # left
    if (col > 0):
        # print ("increasing left")
        lines[row][col-1] += 1
        if (lines[row][col-1] == 10):
            updateFlashes(row, col-1, lines, updates + [[row, col-1]])
            # myUpdates += [[row, col-1]]

    # right
    if (col < numCols):
        # print("increasing right")
        lines[row][col+1] += 1
        if (lines[row][col+1] == 10):
            updateFlashes(row, col+1, lines, updates + [[row, col+1]])
            # myUpdates += [[row1, col+1]]

    if (row < numRows):
        # below
        lines[row+1][col] +=1
        # print("Increasing below")
        if (lines[row+1][col]) == 10:
            updateFlashes(row+1, col, lines, updates + [[row+1, col]])
            # myUpdates += [[row+1, col]]
        
        # down left
        if (col > 0):
            # print("Increasing left down")
            lines[row+1][col-1] += 1
            if (lines[row+1][col-1] == 10):
                updateFlashes(row+1, col-1, lines, updates + [[row+1, col-1]])
                # myUpdates += [[row+1, col-1]]
        # down right
        if (col < numCols):
            # print("Increasing right down")
            lines[row+1][col + 1] += 1
            if (lines[row+1][col+1] == 10):
                updateFlashes(row+1, col+1, lines, updates + [[row+1, col+1]])
                # myUpdates += [[row+1, col+1]]

    return lines, updates
            

def partOne():
    # lines =[[5,4,8,3,1,4,3,2,2,3],
    #         [2,7,4,5,8,5,4,7,1,1],
    #         [5,2,6,4,5,5,6,1,7,3],
    #         [6,1,4,1,3,3,6,1,4,6],
    #         [6,3,5,7,3,8,5,4,7,8],
    #         [4,1,6,7,5,2,4,6,4,5],
    #         [2,1,7,6,8,4,1,7,2,1],
    #         [6,8,8,2,8,8,1,1,3,4],
    #         [4,8,4,6,8,4,8,5,5,4],
    #         [5,2,8,3,7,5,1,5,2,6]]

    # lines =[[1,1,1,1,1],
    #         [1,9,9,9,1],
    #         [1,9,1,9,1],
    #         [1,9,9,9,1],
    #         [1,1,1,1,1]]

    lines = getLinesAsArray('11_input.txt')
    
    numberOfPhases = 10000
    numberOfFlashes = 0
    for phase in range(0, numberOfPhases):
        updates = []
        allUpdates = []
        for row in range(0, len(lines)):
            for col in range(0, len(lines[row])):
                lines[row][col] = lines[row][col] + 1
                if (lines[row][col] == 10):
                    lines, updates = updateFlashes(row, col, lines, [[row, col]])
        
        totalThisPhase = 0
        for x in range(0, len(lines)):
            for y in range(0, len(lines[x])):
                if lines[x][y] > 9:
                    lines[x][y] = 0
                    numberOfFlashes += 1
                    totalThisPhase += 1
        if (totalThisPhase == len(lines) * len(lines[0])):
            return phase
        
    print("Part One:", numberOfFlashes)

    # for x in lines:
    #     print(x)

a = partOne()
print("Part Two:", (a+1))