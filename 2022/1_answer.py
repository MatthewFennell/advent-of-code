from common import getLinesAsNumbers

def part_one():
    lines = getLinesAsNumbers('1_input.txt')
    current_max = 0
    current_sum = 0
    for num in lines:
        if num == '':
            if current_sum > current_max:
                current_max = current_sum
            current_sum = 0
        else:
            current_sum += int(num)
    print('Part One:', current_max)

def part_two():
    lines = getLinesAsNumbers('1_input.txt')

    current_max = 0
    current_second = 0
    current_third = 0
    current_sum = 0

    for num in lines:
        if num == '':
            if current_sum > current_max:
                current_third = current_second
                current_second = current_max
                current_max = current_sum
            elif current_sum > current_second:
                current_third = current_second
                current_second = current_sum
            elif current_sum > current_third:
                current_third = current_sum
            current_sum = 0
        else:
            current_sum += int(num)

    if current_sum > current_max:
        current_third = current_second
        current_second = current_max
        current_max = current_sum
    elif current_sum > current_second:
        current_third = current_second
        current_second = current_sum
    elif current_sum > current_third:
        current_third = current_sum

    print('Part Two:', current_max + current_second + current_third)

part_one()
part_two()