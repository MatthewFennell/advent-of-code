from common import get_lines

def get_starting_terrain(width, height):
    grid = [['.'] * width for i in range(height)]
    return grid

def can_place_sand(row,column,terrain):
    return terrain[row][column] == '.'

def drop_sand(row, column, terrain, total_sand_dropped):
    if terrain[0][500] == 'O':
        return terrain, total_sand_dropped, False
    if row >= len(terrain)-1 or column >= len(terrain[0])-1:
        return terrain, total_sand_dropped, False
    if can_place_sand(row+1, column, terrain):
        return drop_sand(row+1, column, terrain, total_sand_dropped)
    elif can_place_sand(row+1, column-1, terrain):
        return drop_sand(row+1, column-1, terrain, total_sand_dropped)
    elif can_place_sand(row+1, column+1, terrain):
        return drop_sand(row+1, column+1, terrain, total_sand_dropped)
    else:
        terrain[row][column] = 'O'
        return terrain, total_sand_dropped + 1, True

def part_one():
    lines = get_lines('14_input.txt')
    max_row = 0
    max_col = 0

    for line in lines:
        split = [[int(z) for z in i.split(',')] for i in line.split(' -> ')]
        
        for position in range(0, len(split)):
            current_col, current_row = split[position]
            if current_col > max_col:
                max_col = current_col
            if current_row > max_row:
                max_row = current_row
    terrain = get_starting_terrain(max_col+1,max_row+1)
    for line in lines:
        split = [[int(z) for z in i.split(',')] for i in line.split(' -> ')]
        
        for position in range(0, len(split)-1):
            current_col, current_row = split[position]
            next_col, next_row = split[position+1]

            if current_col == next_col:
                smallest_row = current_row if current_row < next_row else next_row
                largest_row = current_row if current_row > next_row else next_row
                for row in range(smallest_row, largest_row+1):
                    terrain[row][current_col] = '#'

            if current_row == next_row:
                smallest_col = current_col if current_col < next_col else next_col
                largest_col = current_col if current_col > next_col else next_col
                for col in range(smallest_col, largest_col+1):
                    terrain[current_row][col] = '#'


    total_sand_dropped = 0
    keep_going = True
    while keep_going:
        terrain, total_sand_dropped, keep_going = drop_sand(0, 500, terrain, total_sand_dropped)
        

    print("Part One:", total_sand_dropped)

def part_two():
    lines = get_lines('14_input.txt')
    max_row = 0
    max_col = 0

    for line in lines:
        split = [[int(z) for z in i.split(',')] for i in line.split(' -> ')]
        
        for position in range(0, len(split)):
            current_col, current_row = split[position]
            if current_col > max_col:
                max_col = current_col
            if current_row > max_row:
                max_row = current_row
    terrain = get_starting_terrain(max_col+200,max_row+1)
    for line in lines:
        split = [[int(z) for z in i.split(',')] for i in line.split(' -> ')]
        
        for position in range(0, len(split)-1):
            current_col, current_row = split[position]
            next_col, next_row = split[position+1]

            if current_col == next_col:
                smallest_row = current_row if current_row < next_row else next_row
                largest_row = current_row if current_row > next_row else next_row
                for row in range(smallest_row, largest_row+1):
                    terrain[row][current_col] = '#'

            if current_row == next_row:
                smallest_col = current_col if current_col < next_col else next_col
                largest_col = current_col if current_col > next_col else next_col
                for col in range(smallest_col, largest_col+1):
                    terrain[current_row][col] = '#'

    extra_row = ['.'] * (max_col+200)
    extra_row_2 = ['#'] * (max_col+200)
    terrain.append(extra_row)
    terrain.append(extra_row_2)


    total_sand_dropped = 0
    keep_going = True
    while keep_going:
        terrain, total_sand_dropped, keep_going = drop_sand(0, 500, terrain, total_sand_dropped)
    
    print("Part Two:", total_sand_dropped)


part_one()
part_two()

