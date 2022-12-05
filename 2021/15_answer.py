from common import get_lines_as_array
import math

def makeBiggerMap(myMap):
    numRows = len(myMap)
    numCopies = 5
    newMap = []
    for t in range(0, numCopies):
        for x in range(0, numRows):
            shift = []
            for y in range(0, numCopies):
                shift = [*shift, *myMap[x]]
            newMap.append(shift)  

    for row in range(0, len(newMap)):
        for col in range(0, len(newMap[0])):
            currentRowAddition = math.floor(row/len(myMap))
            currentColAddition = math.floor(col/len(myMap[0]))
            newVal = newMap[row][col] + currentRowAddition + currentColAddition
            if (newVal > 9):
                newVal = newVal % 10 + 1
            newMap[row][col] = newVal
    return newMap
def part_one():
    lines = get_lines_as_array('15_input.txt')
    lines = makeBiggerMap(lines)
    lines[0][0] = 0
    costs = []
    for row in range(0, len(lines)):
        temp = []
        for col in range(0, len(lines[0])):
            temp.append(0)
        costs.append(temp)
    
    sum = 0
    for x in range(1, len(lines[0])):
        sum += lines[0][x]
        costs[0][x] = sum

    sum = 0
    for y in range(1, len(lines)):
        sum += lines[y][0]
        costs[y][0] = sum

    costs[0][0] = 0

    for x in range(1, len(lines[0])):
        for y in range(1, len(lines)):
            costs[y][x] = min(costs[y-1][x] + lines[y][x], costs[y][x-1] + lines[y][x])
    

    numberOfFixAttempts = 300

    for x in range(0, numberOfFixAttempts):
        print ("fix", x)
        for row in range(0, len(costs)):
            for col in range(0, len(costs[0])):
                if row == 0 and col == 0:
                    pass
                else:
                    above = costs[row-1][col] if row > 0 else 999999999
                    below = costs[row+1][col] if row < len(costs)-1 else 99999999
                    left = costs[row][col-1] if col > 0 else 999999999
                    right = costs[row][col+1] if col < len(costs[0])-1 else 9999999
                    price = lines[row][col]
                    costs[row][col] = min(above+price, below+price, right+price, left+price)
            

    
    print("Part One:", costs[len(costs)-1][len(costs)-1])



part_one()