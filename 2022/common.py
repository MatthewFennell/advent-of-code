import re

def get_lines_as_numbers(filename):
    lines = []
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

def get_lines(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(line)
    return lines

def get_lines_with_empty_lines(filename):
    with open(filename, "r") as file:
        return [line.rstrip() for line in file if line.strip()]

def get_lines_as_array(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            num_list = [char for char in str(line)]
            lines.append(num_list)
    return lines

def get_line_split_on_char(filename, charSplit):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            res = line.split(charSplit) 
            lines.append(res)   
    return lines

def get_number_list(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            myLine = []
            x = list(line)
            for y in x:
                myLine.append(int(y))   
            lines.append(myLine)      
    return lines

def get_lines_as_number_arrays(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            myLine = []
            x = line.split('')
            for y in x:
                myLine.append(int(y))   
            lines.append(myLine)      
    return lines

def get_lines_as_numbers(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            myLine = []
            x = line.split(',')
            for y in x:
                myLine.append(int(y))   
            lines.append(myLine)      
    return lines