import re

def getLinesAsNumbers(filename):
    lines = []
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

