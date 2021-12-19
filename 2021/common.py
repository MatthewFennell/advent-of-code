import re

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

def getLineSplitOnManyChars(filename, charsToSplitOn):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            res = re.split(charsToSplitOn, line)    
            lines.append(list(map(int,res)))
    return lines


def getLinesAsArrayWithSplit(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            res = line.split(' | ')
            partOne = res[0].split(" ")
            partTwo = res[1].split(" ")
            lines.append([partOne, partTwo])
            
    return lines
    