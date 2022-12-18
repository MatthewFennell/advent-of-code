from common import get_lines_as_array

def get_starting_grid(width, height):
    grid = [[' '] * width for i in range(height)]
    return grid

shape_one = [
    ['@', '@', '@', '@'],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
]

shape_two = [
    [' ', '@', ' ', ' '],
    ['@', '@', '@', ' '],
    [' ', '@', ' ', ' '],
    [' ', ' ', ' ', ' '],
]

#  upside down
shape_three = [
    ['@', '@', '@', ' '],
    [' ', ' ', '@', ' '],
    [' ', ' ', '@', ' '],
    [' ', ' ', ' ', ' '],
]

shape_four = [
    ['@', ' ', ' ', ' '],
    ['@', ' ', ' ', ' '],
    ['@', ' ', ' ', ' '],
    ['@', ' ', ' ', ' '],
]

shape_five = [
    ['@', '@', ' ', ' '],
    ['@', '@', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
]

# >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
# RightLeftLeftLeftRightRightLeftRightRightRightLeftLeftLeftRightRightRightLeftLeftLeftRightLeftLeftLeftRightRightLeftRightRightLeftLeftRightRight
def find_max_height(grid):
    # print("INSPECTION", grid)
    for row in range(len(grid)-1, -1, -1):
        for y in range(0, len(grid[row])):
            if grid[row][y] == '#':
                return row + 1
    return 0

# temporarily grow the grid by 3
def put_shape_in_starting_position(shape, grid):
    start_column = 2
    max_row_with_piece = find_max_height(grid)
    # print("max row with piece", max_row_with_piece)
    starting_row = max_row_with_piece + 3
    # print("STARTING ROW", starting_row)
    number_of_rows_to_add = starting_row - len(grid)
    # print("number of rows to add", number_of_rows_to_add)
    for row_to_add in range(0, number_of_rows_to_add):
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])

    if shape == shape_one:
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])

    if shape == shape_two:
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])

    if shape == shape_three:
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
    
    if shape == shape_four:
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])

    if shape == shape_five:
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])


    # print("Before creating shape")
    # for z in grid:
    #     print(z)

    min_row_set = len(grid)-1

    for row in range(starting_row, min(len(grid), starting_row + 4)):
        for column in range(0, 4):
            grid[row][start_column+column] = shape[row-starting_row][column]
            if shape[row-starting_row][column] == '@' and row < min_row_set:
                min_row_set = row

    return grid, min_row_set, start_column

shapes = [shape_one, shape_two, shape_three, shape_four, shape_five]

def move_shape(grid, direction, start_row, start_column, number_of_rocks_dropped):
    # right
    if direction == '>':
        word = 'RIGHT'
    elif direction == '<':
        word = 'LEFT'
    else:
        word = 'DOWN'
    # print("start row", start_row, "start column", start_column, word)
    if direction == '>':
        for row in range(start_row, min(len(grid), start_row + 4)):
            for column in range(min(6, start_column+3), start_column-1, -1):
                # print("row", row, "column", column)
                if column + 1 > 6 and grid[row][column] == '@':
                    # print("Can't move right. Out of bounds")
                    return grid, start_row, start_column, number_of_rocks_dropped
                if grid[row][column] == '@' and grid[row][column+1] == '#':
                    # print("Cant move right. Blocking piece")
                    return grid, start_row, start_column, number_of_rocks_dropped

        for row in range(start_row, min(len(grid), start_row + 4)):
            for column in range(min(6, start_column+4), start_column, -1):
                if grid[row][column-1] == '@':
                    grid[row][column] = grid[row][column-1]
                    grid[row][column-1] = ' '
        start_column += 1
    # left
    elif direction == '<':
        for row in range(start_row, min(len(grid), start_row + 4)):
            for column in range(start_column, min(6, start_column+4)+1):
                if column -1 < 0 and grid[row][column] == '@':
                    # print("Can't move left. Out of bounds")
                    return grid, start_row, start_column, number_of_rocks_dropped
                if grid[row][column-1] == '#' and grid[row][column] == '@':
                    # print("Cant move left. Blocking piece")
                    return grid, start_row, start_column, number_of_rocks_dropped

        for row in range(start_row, min(len(grid), start_row + 4)):
            for column in range(start_column, min(6, start_column+4)+1):
                if grid[row][column] == '@':
                    grid[row][column-1] = grid[row][column]
                    grid[row][column] = ' '
        start_column -= 1

    else:
        # print("start row", start_row, "start column", start_column)
        for row in range(start_row, len(grid)):
            for column in range(start_column, min(6, start_column + 4)+1):
                if (row - 1 < 0 or grid[row-1][column] == '#') and grid[row][column] == '@':
                    for row in range(start_row, min(len(grid), start_row + 4)):
                        for column in range(start_column, min(6, start_column + 4)+1):
                            if grid[row][column] == '@':
                                grid[row][column] = '#'
                    # print("Reached the bottom or piece beneath")
                    return grid, start_row, start_column,number_of_rocks_dropped+1
        for row in range(start_row, min(len(grid), start_row + 4)):
            for column in range(start_column, min(6, start_column + 4)+1):
                if grid[row][column] == '@':
                    grid[row-1][column] = grid[row][column]
                elif grid[row-1][column] != '#':
                    grid[row-1][column] = ' '
                if row == min(len(grid), start_row + 4) -1 and grid[row][column] != '#':
                    grid[row][column] = ' ' 
        start_row -= 1
        
        found_hash = False
        for x in grid[len(grid)-1]:
            if x == '#':
                found_hash = True
        if not found_hash:
            grid.pop()

    return grid, start_row, start_column, number_of_rocks_dropped

def air_movement(grid, movement, start_row, start_column):
    grid = move_shape(grid, movement, start_row, start_column)
    return grid

def drop_shape(grid):
    return grid

def part_one():
    lines = get_lines_as_array('17_input.txt')[0]
    number_of_rocks_dropped = 0

    grid = get_starting_grid(7, 1)
    number_of_rocks_to_drop = 1000000
    iteration = 0
    dropped_rocks={}

    while number_of_rocks_dropped < number_of_rocks_to_drop:        
        if number_of_rocks_dropped not in dropped_rocks:
            grid, start_row, start_column = put_shape_in_starting_position(shapes[number_of_rocks_dropped%5], grid)
            dropped_rocks[number_of_rocks_dropped] = True
        # big_copy =[]
        # for d in grid:
        #     big_copy.append(d[:])
        grid, start_row, start_column, number_of_rocks_dropped = move_shape(grid, lines[iteration % len(lines)], start_row, start_column, number_of_rocks_dropped)

        # for z in range(0, len(grid)):
        #     big_copy[z].append('|')
        #     big_copy[z] += grid[z]
        grid, start_row, start_column, number_of_rocks_dropped = move_shape(grid, 'DOWN', start_row, start_column, number_of_rocks_dropped)
        iteration += 1
        # for z in range(0, len(grid)):
        #     big_copy[z].append('|')
        #     big_copy[z] += grid[z]
        # print("| PLACE |  AIR  | DOWN |")
        # for d in range(len(big_copy)-1, -1, -1):
        #     big_copy[d].append('|')
        #     big_copy[d].insert(0, '|')
        #     print(''.join(big_copy[d]))

    print("Part One:", len(grid))

        
    


part_one()
