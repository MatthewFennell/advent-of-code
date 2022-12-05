import math
from common import get_lines_as_array

def follow(row, col, s, data):
    for y, x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if (row + y, col + x) not in s:
            if row + y >= 0 and row + y < len(data):
                if col + x < len(data[0]) and col + x >= 0:
                    if data[row + y][col + x] != "9":
                        s.add((row + y, col + x))
                        follow(row + y, col + x, s, data)
    return s

def isLowPoint(row, col, grid):
    isLowPoint = True
    cell = grid[row][col]

    if (row > 0):
        if grid[row-1][col] <= cell:
            return False
    if (row < len(grid)-1):
        if grid[row+1][col] <= cell:
            return False
    if (col > 0):
        if grid[row][col-1] <= cell:
            return False
    if (col < len(grid[0])-1):
        if grid[row][col+1] <= cell:
            return False
    return True


def part_two():
    data = open("9_input.txt").read().strip().split("\n")
    lows = []
    basins = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            cur = int(data[row][col])
            n = int(data[row - 1][col]) if row > 0 else 9999
            s = int(data[row + 1][col]) if row < len(data) - 1 else 9999
            e = int(data[row][col + 1]) if col < len(data[0]) - 1 else 9999
            w = int(data[row][col - 1]) if col > 0 else 9999
            if cur < min([n, s, e, w]):
                basins.append(len(follow(row, col, {(row, col)}, data)))
    print(f"Part 2: {math.prod(sorted(list(basins), reverse=True)[:3])}")


def part_one():
    lines = get_lines_as_array('9_input.txt')

    # lines = [[2,1,9,9,9,4,3,2,1,0],
    #         [3,9,8,7,8,9,4,9,2,1],
    #         [9,8,5,6,7,8,9,8,9,2],
    #         [8,7,6,7,8,9,6,7,8,9],
    #         [9,8,9,9,9,6,5,6,7,8]]
    numRows = len(lines)
    numCols = len(lines[0])
    lowPoints = []
    for row in range(0, numRows):
        for col in range(0, numCols):
            isLow = isLowPoint(row, col, lines)
            if (isLow):
                lowPoints.append([row, col])

    totalLows = 0
    print(lowPoints)
    for x in lowPoints:
        totalLows += lines[x[0]][x[1]]+1
    print("Part One:", totalLows)



    

part_one()
part_two()