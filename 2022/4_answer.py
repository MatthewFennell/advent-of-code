from common import get_line_split_on_char, read_lines

def is_overlap(s1, s2):
    if s1[0] <= s2[0] and s1[1] >= s2[1]:
        return True

    if s2[0] <= s1[0] and s2[1] >= s1[1]:
        return True

    return False

def any_overlap(s1, s2):
    if s1[0] >= s2[0] and s1[0] <= s2[1]:
        return True
    if s1[1] >= s2[0] and s1[1] <= s2[1]:
        return True

    if s2[0] >= s1[0] and s2[0] <= s1[1]:
        return True
    if s2[1] >= s1[0] and s2[1] <= s1[1]:
        return True
    return False
    
def part_one():
    lines = get_line_split_on_char('4_input.txt', ',')
    total_overlaps = 0
    for line in lines:
        s1 = [int(x) for x in line[0].split('-')]
        s2 = [int(x) for x in line[1].split('-')]
        overlapping = is_overlap(s1, s2)
        if (overlapping):
            total_overlaps += 1
    print("Part One:", total_overlaps)
        
        
def part_two():
    lines = get_line_split_on_char('4_input.txt', ',')
    total_overlaps = 0
    for line in lines:
        s1 = [int(x) for x in line[0].split('-')]
        s2 = [int(x) for x in line[1].split('-')]
        overlapping = any_overlap(s1, s2)
        if (overlapping):
            total_overlaps += 1
    print("Part Two:", total_overlaps)


part_one()
part_two()