from common import get_lines

default_points = {
    'X':1,
    'Y':2,
    'Z':3
}

results = {
    'X': {
        'A':3,
        'B':0,
        'C':6
    },
    'Y': {
        'A':6,
        'B':3,
        'C':0
    },
    'Z': {
        'A':0,
        'B':6,
        'C':3
    }
}

# A = ROCK
# B = PAPER
# C = SCISSORS

# X = LOSE
# Y = DRAW
# Z = WIN

# X = ROCK 
# Y = PAPER
# Z = SCISSORS
desired_outcomes = {
    'A': {
        'X': 'Z',
        'Y': 'X',
        'Z': 'Y'
    },
    'B': {
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
    },
    'C': {
        'X': 'Y',
        'Y': 'Z',
        'Z': 'X'
    }
}

def get_score(enemy_choice, my_choice):
    return default_points[my_choice] + results[my_choice][enemy_choice]


def figure_out(enemy_choice, desired_result):
    return desired_outcomes[enemy_choice][desired_result]


def part_one():
    lines = get_lines('2_input.txt')
    score = 0
    for round in lines:
        split = round.split(' ')
        score += get_score(split[0], split[1])
    print("Part One:", score)

def part_two():
    lines = get_lines('2_input.txt')
    score = 0
    for round in lines:
        split = round.split(' ')
        my_move = figure_out(split[0], split[1])
        score += get_score(split[0], my_move)
    print("Part Two:", score)


part_one()
part_two()