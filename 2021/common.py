import re

def get_lines_as_numbers(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line))
    return lines

def get_lines(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(line)
    return lines

def get_lines_as_array(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            numList = [int(digit) for digit in str(line)]
            lines.append(numList)
    return lines

def get_line_as_numbers(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            x = line.split(',')
            for y in x:
                lines.append(int(y))         
    return lines

def get_lines_as_number_arrays(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            myLine = []
            x = line.split(',')
            for y in x:
                myLine.append(int(y))   
            lines.append(myLine)      
    return lines

def get_bingo_boards(filename):
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

def get_line_split_on_many_chars(filename, charsToSplitOn):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            res = re.split(charsToSplitOn, line)    
            lines.append(list(map(int,res)))
    return lines


def get_line_split_on_char(filename, charSplit):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            res = line.split(charSplit) 
            lines.append(res)   
    return lines

def get_lines_as_array_with_split(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            res = line.split(' | ')
            part_one = res[0].split(" ")
            part_two = res[1].split(" ")
            lines.append([part_one, part_two])
            
    return lines
    