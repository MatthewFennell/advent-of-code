from common import get_lines

def get_signal_strength(X, cycle):
    return X * cycle

def part_one():
    lines = get_lines('10_input.txt')
    cycle_num = 0
    X = 1
    sum_of_signals = 0
    cycle_nums_of_interest = [20, 60, 100, 140, 180, 220]

    for command in lines:
        # print("command", command, "cycle num", cycle_num, "X", X)
        if command == 'noop':
            cycle_num += 1
            if cycle_num in cycle_nums_of_interest:
                sum_of_signals += get_signal_strength(X, cycle_num)
                # print("adding result", get_signal_strength(X, cycle_num))
        else:
            operations = command.split('addx ')
            amount = int(operations[1])
            # Value during
            cycle_num += 1

            if cycle_num in cycle_nums_of_interest:
                sum_of_signals += get_signal_strength(X, cycle_num)

            # Value after
            cycle_num += 1
            if cycle_num in cycle_nums_of_interest:
                sum_of_signals += get_signal_strength(X, cycle_num)
            X += amount
    print("Part One:", sum_of_signals)

def get_row_to_work_on(cycle_num):
    if cycle_num <= 40:
        return 0
    elif cycle_num <= 80:
        return 1
    elif cycle_num <= 120:
        return 2
    elif cycle_num <= 160:
        return 3
    elif cycle_num <= 200:
        return 4
    else:
        return 5

def get_starting_grid(width, height):
    grid = [['.'] * width for i in range(height)]
    return grid

def part_two():
    lines = get_lines('10_input.txt')
    cycle_num = 0
    X = 1 # position of the middle of the sprite that is 3 wide

    grid = get_starting_grid(0, 6)

    for command in lines:
        if command == 'noop':
            cycle_num += 1
            index = (cycle_num-1)% 40
            row = get_row_to_work_on(cycle_num)
            if index == X or index == X-1 or index == X+1:
                grid[row].append('#')
            else:
                grid[row].append('.')

        else:
            operations = command.split('addx ')
            amount = int(operations[1])
            # Value during
            cycle_num += 1
            # print("Start cycle", cycle_num, ": beging executing", command)

            row = get_row_to_work_on(cycle_num)
            index = (cycle_num-1)% 40
            if index == X or index == X-1 or index == X+1:
                grid[row].append('#')
                # print("During cycle", cycle_num, ": CRT draws pixel # in position", cycle_num-1)
            else:
                grid[row].append('.')
                # print("During cycle", cycle_num, ": CRT draws pixel . in position", cycle_num-1)
            # print("Current CRT row:", grid[row])
            # print("")

            # Value after
            cycle_num += 1            

            index = (cycle_num-1)% 40
            row = get_row_to_work_on(cycle_num)
            if index == X or index == X-1 or index == X+1:
                # print("During cycle", cycle_num, ": CRT draws pixel # in position", cycle_num-1)
                # grid[row][cycle_num-1] = "#"
                grid[row].append('#')
            else:
                # print("During cycle", cycle_num, ": CRT draws pixel . in position", cycle_num-1)
                grid[row].append('.')
            X += amount
            # print("Current CRT row:", grid[row])
            # print("End of cycle", cycle_num, ": finishing executing", command, "(Register X is now", X, ")")
    print("Part Two:")
    for x in grid:
        print(x)    

part_one()
part_two()