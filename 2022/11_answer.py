import math
from common import get_lines_with_empty_lines

def get_monkey_info(block):
    monkey_number = int(block[0].replace('Monkey ', '').replace(':', ''))
    starting_items = [int(e) if e.isdigit() else e for e in block[1].split(': ')[1].split(', ')]
    operation_op = block[2].replace('  Operation: new = old ', '').split(' ')[0]
    operation_num = block[2].replace('  Operation: new = old ', '').split(' ')[1]
    test_num = int(block[3].replace('  Test: divisible by ', ''))
    true_scenario = int(block[4].replace('    If true: throw to monkey ', ''))
    false_scenario = int(block[5].replace('    If false: throw to monkey ', ''))
    return {
        "monkey_number": monkey_number,
        "starting_items": starting_items,
        "operation_op": operation_op,
        "operation_num": operation_num,
        "test_num": test_num,
        "true_scenario": true_scenario,
        "false_scenario": false_scenario,
        "number_of_inspections": 0
    }

# {'monkey_number': 0, 'starting_items': [79, 98], 'operation_op': '*', 'operation_num': '19', 'test_num': 23, 'true_scenario': 2, 'false_scenario': 3}
# {'monkey_number': 1, 'starting_items': [54, 65, 75, 74], 'operation_op': '+', 'operation_num': '6', 'test_num': 19, 'true_scenario': 2, 'false_scenario': 0}
# {'monkey_number': 2, 'starting_items': [79, 60, 97], 'operation_op': '*', 'operation_num': 'old', 'test_num': 13, 'true_scenario': 1, 'false_scenario': 3}
# {'monkey_number': 3, 'starting_items': [74], 'operation_op': '+', 'operation_num': '3', 'test_num': 17, 'true_scenario': 0, 'false_scenario': 1}

def get_most_active_monkeys(monkeys):
    inspections = sorted([monkeys[x]['number_of_inspections'] for x in monkeys.keys()])
    return inspections[-1] * inspections[-2]

def part_one():
    lines = get_lines_with_empty_lines('11_input.txt')
    num_rounds = 20
    monkeys = {}
    for line in range(0, len(lines), 6):
        monkeys[line/6] = get_monkey_info(lines[line:line+6])

    num_monkeys = len(monkeys.keys())
    for round in range(num_rounds):
        for monkey_key in range(num_monkeys):
            print("")
            print(f"Monkey {monkey_key}:")
            monkey_info = monkeys[monkey_key]
            for item in monkey_info['starting_items']:
                print("  Monkey inspects an item with a worry level of", item)
                monkeys[monkey_key]['number_of_inspections'] += 1
                operation_num = item if monkey_info['operation_num'] == 'old' else int(monkey_info['operation_num'])
                new_worry_level = eval(f"{item} {monkey_info['operation_op']} {operation_num}")
                print(f"    Worry level is {monkey_info['operation_op']} by {operation_num} to {new_worry_level}")
                worry_after_division = new_worry_level // 3
                print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_after_division}.")

                new_monkey = monkey_info['true_scenario'] if worry_after_division % monkey_info['test_num'] == 0 else monkey_info['false_scenario']
                monkeys[new_monkey]['starting_items'].append(worry_after_division)
                print(f"    Item with worry level {worry_after_division} is thrown to monkey {new_monkey}.")


            monkeys[monkey_key]['starting_items'] = []
    most_active_monkeys = get_most_active_monkeys(monkeys)
    print("Part One:", most_active_monkeys)

def part_two():
    lines = get_lines_with_empty_lines('11_input.txt')
    num_rounds = 10000
    monkeys = {}
    for line in range(0, len(lines), 6):
        monkeys[line/6] = get_monkey_info(lines[line:line+6])

    divisor_total = math.prod([monkeys[x]['test_num'] for x in monkeys.keys()])

    num_monkeys = len(monkeys.keys())
    for round in range(num_rounds):
        for monkey_key in range(num_monkeys):
            monkey_info = monkeys[monkey_key]
            for item in monkey_info['starting_items']:
                monkeys[monkey_key]['number_of_inspections'] += 1
                operation_num = item if monkey_info['operation_num'] == 'old' else int(monkey_info['operation_num'])
                new_worry_level = eval(f"{item} {monkey_info['operation_op']} {operation_num}")
                # print(f"    Worry level is {monkey_info['operation_op']} by {operation_num} to {new_worry_level}")
                worry_after_division = new_worry_level % divisor_total
                # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_after_division}.")

                new_monkey = monkey_info['true_scenario'] if worry_after_division % monkey_info['test_num'] == 0 else monkey_info['false_scenario']
                monkeys[new_monkey]['starting_items'].append(worry_after_division)
                # print(f"    Item with worry level {worry_after_division} is thrown to monkey {new_monkey}.")


            monkeys[monkey_key]['starting_items'] = []
    most_active_monkeys = get_most_active_monkeys(monkeys)
    print("Part Two:", most_active_monkeys)

part_one()
part_two()