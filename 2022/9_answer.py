from common import get_lines

def calculate_tail_position(head_row, head_col, tail_row, tail_col):
    if abs(head_row - tail_row) >= 2 or abs(head_col-tail_col) >= 2:
        if head_col == tail_col:
            # in the same column
            new_tail_row = tail_row + 1 if head_row > tail_row else tail_row - 1
            return new_tail_row, tail_col

        elif head_row == tail_row:
            # in the same row
            new_tail_col = tail_col + 1 if head_col > tail_col else tail_col - 1
            return tail_row, new_tail_col

        else:
            new_tail_row = tail_row + 1 if head_row > tail_row else tail_row - 1
            new_tail_col = tail_col + 1 if head_col > tail_col else tail_col - 1
            return new_tail_row, new_tail_col
    else:
        return tail_row, tail_col

def get_num_occupied_positions(positions):
    total = 0
    for key in positions.keys():
        total += len(positions[key].keys())
    return total

def part_one():
    lines = get_lines('9_input.txt')
    head_current_col = 0
    head_current_row = 0

    tail_current_col = 0
    tail_current_row = 0

    occupied_tail_positions = {0: {0: True}}
    
    for line in lines:
        movements = line.split(' ')
        direction = movements[0]
        amount = int(movements[1])

        for x in range(amount):

            if direction == 'R':
                head_current_col += 1
            elif direction == 'L':
                head_current_col -= 1
            elif direction == 'U':
                head_current_row += 1
            elif direction == 'D':
                head_current_row -= 1
            
            tail_current_row, tail_current_col = calculate_tail_position(head_current_row, head_current_col, tail_current_row, tail_current_col)
            if tail_current_row in occupied_tail_positions:
                occupied_tail_positions[tail_current_row][tail_current_col] = True
            else:
                occupied_tail_positions[tail_current_row] = {}
                occupied_tail_positions[tail_current_row][tail_current_col] = True

    total = get_num_occupied_positions(occupied_tail_positions)
    print("Part One:", total)

def part_two():
    lines = get_lines('9_input.txt')
    current_positions = [ # stored as [row, col]
        [0,0], # H
        [0,0], # 1
        [0,0], # 2
        [0,0], # 3
        [0,0], # 4
        [0,0], # 5
        [0,0], # 6
        [0,0], # 7
        [0,0], # 8
        [0,0], # 9
    ]

    occupied_tail_positions = {0: {0: True}}
    positions = []

    for line in lines:
        movements = line.split(' ')
        direction = movements[0]
        amount = int(movements[1])

        for x in range(amount):
            # move the head
            if direction == 'R':
                current_positions[0][1] += 1
            elif direction == 'L':
                current_positions[0][1] -= 1
            elif direction == 'U':
                current_positions[0][0] += 1
            elif direction == 'D':
                current_positions[0][0] -= 1

            for y in range(1, len(current_positions)):
                previous_row = current_positions[y-1][0]
                previous_col = current_positions[y-1][1]
                active_row = current_positions[y][0]
                active_col = current_positions[y][1]
                new_row, new_col = calculate_tail_position(previous_row, previous_col, active_row, active_col)
                current_positions[y][0] = new_row
                current_positions[y][1] = new_col

                if y == 9:
                    if len(positions) == 0 or ([new_row, new_col] != positions[-1]):
                        positions.append([new_row, new_col])
                    if new_row in occupied_tail_positions:
                        occupied_tail_positions[new_row][new_col] = True
                    else:
                        occupied_tail_positions[new_row] = {}
                        occupied_tail_positions[new_row][new_col] = True

    total = get_num_occupied_positions(occupied_tail_positions)
    print("Part Two:", total)

        


part_one()
part_two()