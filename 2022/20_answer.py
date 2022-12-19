from common import get_lines

def figure_out_new_index(index, number, length):
    

def perform_swap(index, numbers, old_index):
    old_value = numbers[old_index]["value"]
    numbers.insert(index, numbers.pop(old_index))
    # print(old_value, "moves between", numbers[index-1]["value"], "and", numbers[index+1]["value"])
    previous_index = (index-1) % len(numbers)
    next_index = (index+1) % len(numbers)
    numbers[index]['has_moved'] = True
    return numbers

def move_index(index, numbers):
    value_at_index = numbers[index]['value']
    new_index = (value_at_index + index)

    if value_at_index < 0 and new_index == 0:
        new_index = len(numbers)

    numbers = perform_swap(new_index, numbers, index)
    print_numbers(numbers)

    return numbers, max(0, index-1)

def print_numbers(numbers):
    nums = [x["value"] for x in numbers]
    print(nums)

def part_one():
    lines = get_lines('20_input.txt')

    has_moved_list = []

    for x in lines:
        has_moved_list.append({
            "value": int(x),
            "has_moved": False
        })

    current_index = 0
    numbers_moved = 0

    while numbers_moved < len(has_moved_list):
        print("")
        if has_moved_list[current_index]["has_moved"] == True:
            current_index += 1
        else:
            has_moved_list, current_index = move_index(current_index, has_moved_list)
            numbers_moved += 1
    print_numbers(has_moved_list)

part_one()

print(-2%8)