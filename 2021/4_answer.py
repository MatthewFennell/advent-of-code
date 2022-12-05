from common import get_line_as_numbers, get_bingo_boards

def part_one(): 
    lines = get_line_as_numbers('4_numbers.txt')
    # print(lines)

    bingoBoards = get_bingo_boards('4_input.txt')
    # print(bingoBoards)

    myDict = {}

    # [i, j, k] represents board i, row j, column k    
    # stop when any board row or column count = 5

    rowCounts = {}
    columnCounts = {}

    for i in range(0, len(bingoBoards)):
        rowCounts[i] = [0,0,0,0,0]
        columnCounts[i] = [0,0,0,0,0]


    for i in range(0, len(bingoBoards)):
        for j in range(0, 5):
            for k in range(0, 5):
                bingoBoardValue = bingoBoards[i][j][k]
                if bingoBoardValue in myDict:
                    myDict[bingoBoardValue].append([i, j, k])
                else:
                    myDict[bingoBoardValue] = [[i,j,k]]
    for bingoNumber in lines:
        array = myDict[bingoNumber]
        for x in range(0, len(array)):
            dimensions = array[x]
            bingoBoards[dimensions[0]][dimensions[1]][dimensions[2]] = -1
            rowCounts[dimensions[0]][dimensions[1]] += 1
            columnCounts[dimensions[0]][dimensions[2]] += 1    
            if (rowCounts[dimensions[0]][dimensions[1]] == 5 or columnCounts[dimensions[0]][dimensions[2]] == 5):
                board = bingoBoards[dimensions[0]]
                flat_list = [item for sublist in board for item in sublist]                
                sum = 0
                for x in flat_list:
                    if (x != -1):
                        sum += x
                return sum * bingoNumber
                
def part_two(): 
    lines = get_line_as_numbers('4_numbers.txt')
    # print(lines)

    bingoBoards = get_bingo_boards('4_input.txt')
    # print(bingoBoards)

    myDict = {}

    # [i, j, k] represents board i, row j, column k    
    # stop when any board row or column count = 5

    rowCounts = {}
    columnCounts = {}
    finishedBoards = {}

    for i in range(0, len(bingoBoards)):
        rowCounts[i] = [0,0,0,0,0]
        columnCounts[i] = [0,0,0,0,0]


    for i in range(0, len(bingoBoards)):
        for j in range(0, 5):
            for k in range(0, 5):
                bingoBoardValue = bingoBoards[i][j][k]
                if bingoBoardValue in myDict:
                    myDict[bingoBoardValue].append([i, j, k])
                else:
                    myDict[bingoBoardValue] = [[i,j,k]]
    for bingoNumber in lines:
        array = myDict[bingoNumber]
        for x in range(0, len(array)):
            dimensions = array[x]
            bingoBoards[dimensions[0]][dimensions[1]][dimensions[2]] = -1
            rowCounts[dimensions[0]][dimensions[1]] += 1
            columnCounts[dimensions[0]][dimensions[2]] += 1    
            if (rowCounts[dimensions[0]][dimensions[1]] == 5 or columnCounts[dimensions[0]][dimensions[2]] == 5):
                numberOfFinishedBoard = len(finishedBoards.keys())
                if (dimensions[0] not in finishedBoards and numberOfFinishedBoard == len(bingoBoards)-1):
                    board = bingoBoards[dimensions[0]]
                    flat_list = [item for sublist in board for item in sublist]                
                    sum = 0
                    for x in flat_list:
                        if (x != -1):
                            sum += x
                    return sum * bingoNumber
                finishedBoards[dimensions[0]] = True

                


print("Part one:", part_one())
print("Part two:", part_two())