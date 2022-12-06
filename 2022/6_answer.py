from common import get_lines

def get_marker(line, buffer_rate):
    last_seen = {}
    buffer_length = 0
    for i in range(len(line)):
        if (line[i] in last_seen and last_seen[line[i]] <= i-buffer_rate) or line[i] not in last_seen:
            buffer_length += 1
            if buffer_length == buffer_rate:
                return i + 1
        else:
            buffer_length = min(max(1, i - last_seen[line[i]]), buffer_length+1)
        last_seen[line[i]] = i
    return i + 1

def part_one():
    line = get_lines('6_input.txt')[0]
    print('line', line)
    marker = get_marker(line, 4)
    print("Part One:", marker)

def part_two():
    line = get_lines('6_input.txt')[0]
    print('line', line)
    marker = get_marker(line, 14)
    print("Part Two:", marker)
  

part_one()
part_two()