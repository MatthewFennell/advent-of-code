from common import get_lines

def decode_line(line):
    temp = line.split(' from ')
    first = int(temp[0].replace('move ', ''))
    temp_two = temp[1].split(' to ')
    second = int(temp_two[0])
    third = int(temp_two[1])
    return first, second, third

def mutate_stack(stacks,how_many,from_where,to_where):
    new_stacks = {**stacks}
    stuff_to_move = stacks[from_where][-how_many:]
    for i in range(0, len(stuff_to_move)):
        new_stacks[from_where].pop()
        new_stacks[to_where].append(stuff_to_move[len(stuff_to_move)-1-i])
    return new_stacks

def mutate_stack_part_two(stacks,how_many,from_where,to_where):
    new_stacks = {**stacks}
    stuff_to_move = stacks[from_where][-how_many:]
    new_stacks[from_where] = new_stacks[from_where][:len(new_stacks[from_where]) - how_many]
    new_stacks[to_where] += stuff_to_move
    return new_stacks

def part_one():
    # stacks = {
    #     1: ['Z', 'N'],
    #     2: ['M', 'C', 'D'],
    #     3: ['P']
    # }
    stacks = {
        1: ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
        2: ['M', 'Q', 'H'],
        3: ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
        4: ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
        5: ['M', 'T', 'H', 'P'],
        6: ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
        7: ['M', 'N', 'B', 'F', 'V', 'R'],
        8: ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
        9: ['P', 'D', 'B', 'C', 'N']
    }
    lines = get_lines('5_input.txt')
    for line in lines:
        a,b,c = decode_line(line)
        stacks = mutate_stack(stacks,a,b,c)

    final_str = ""
    for x in range(1,10):
        final_str += stacks[x][-1]
    print("Part One:", final_str)

def part_two():
    # stacks = {
    #     1: ['Z', 'N'],
    #     2: ['M', 'C', 'D'],
    #     3: ['P']
    # }
    stacks = {
        1: ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
        2: ['M', 'Q', 'H'],
        3: ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
        4: ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
        5: ['M', 'T', 'H', 'P'],
        6: ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
        7: ['M', 'N', 'B', 'F', 'V', 'R'],
        8: ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
        9: ['P', 'D', 'B', 'C', 'N']
    }
    lines = get_lines('5_input.txt')
    for line in lines:
        a,b,c = decode_line(line)
        stacks = mutate_stack_part_two(stacks,a,b,c)

    final_str = ""
    for x in range(1,10):
        final_str += stacks[x][-1]
    print("Part Two:", final_str)
    

part_one()
part_two()