import re

def getLinesAsNumbers(filename):
    lines = []
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

def getLines(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(line)
    return lines

