from common import get_lines_as_array

def get_value(letter):
    if letter.isupper():
        return ord(letter)-38
    return ord(letter)-96

def find_overlap(left, right):
    items_in_left = {}
    for item in left:
        if item in items_in_left:
            items_in_left[item] += 1
        else:
            items_in_left[item] = 1
    
    for item in right:
        if item in items_in_left:
            return item
    return "ERROR"

def get_compartments(rucksack):
    length = int(len(rucksack)/2)
    return rucksack[0:length], rucksack[length:]

def part_one():
    lines = get_lines_as_array('3_input.txt')
    total_sum = 0
    for rucksack in lines:
        left,right = get_compartments(rucksack)
        overlap = find_overlap(left, right)
        total_sum += get_value(overlap)
    print("Part One:", total_sum)  

def get_common_badge(r1, r2, r3):
    letters = {}
    for letter in r1:
        letters[letter] = 1

    for letter in r2:
        if letter in letters:
            letters[letter] = 2

    for letter in r3:
        if letter in letters and letters[letter] == 2:
            return letter

def part_two():
    lines = get_lines_as_array('3_input.txt')
    total_sum = 0
    for i in range(0, len(lines), 3):
        common_badge = get_common_badge(lines[i], lines[i+1], lines[i+2])
        total_sum += get_value(common_badge)
    print("Part Two:", total_sum)

part_one()
part_two()