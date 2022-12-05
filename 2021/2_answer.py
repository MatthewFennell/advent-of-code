from common import get_lines

def part_one():
    horizontal = 0
    depth = 0
    lines = get_lines('2_input.txt')
    # lines = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    for i in range(0, len(lines)):
        row = lines[i].split()
        direction = row[0]
        amount = int(row[1])
        if (direction == "forward"):
            horizontal += amount
        elif (direction == "up"):
            depth -= amount
        else:
            depth += amount
    print ("Horizontal: " + str(horizontal))
    print ("Depth: " + str(depth))
    print ("Part One: " + str(horizontal*depth))
    print("")

def part_two():
    horizontal = 0
    depth = 0
    aim = 0
    lines = get_lines('2_input.txt')
    # lines = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    for i in range(0, len(lines)):
        row = lines[i].split()
        direction = row[0]
        amount = int(row[1])
        if (direction == "forward"):
            horizontal += amount
            depth += aim * amount
        elif (direction == "up"):
            aim -= amount
        else:
            aim += amount
    print ("Horizontal: " + str(horizontal))
    print ("Depth: " + str(depth))
    print ("Part Two: " + str(horizontal*depth)) 


part_one() # 1728414
part_two() # 1765720035