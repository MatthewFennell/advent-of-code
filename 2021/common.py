def getLinesAsNumbers(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line))
    return lines

def getLines(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(line)
    return lines

def getLinesAsArray(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            numList = [int(digit) for digit in str(line)]
            lines.append(numList)
    return lines

def getLineAsNumbers(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            x = line.split(',')
            for y in x:
                lines.append(int(y))         
    return lines

def getBingoBoards(filename):
    lines = []
    currentBoard = []
    with open(filename) as file:
        for line in file:
            if (line == '\n'):
                lines.append(currentBoard)
                currentBoard = []
            else:                
                currentBoard.append(list(map(int, line.rstrip().split())))
        lines.append(currentBoard)
    return lines
    