from common import get_number_list

def add_tree(trees, row, column):
    if row in trees:
        trees[row][column] = True
    else:
        trees[row] = {}
        trees[row][column] = True
    return trees

def total_num_visible_trees(trees):
    num_trees = 0
    for x in trees.keys():
        num_trees += len(trees[x].keys())
    return num_trees

def part_one():
    lines = get_number_list('8_input.txt')
    visible_trees = {}
    for row in range(0, len(lines)):
        # Left to right
        largest_left = lines[row][0]
        column = 1
        visible_trees = add_tree(visible_trees, row, 0)
        while column < len(lines[row]):
            next_tree_height = lines[row][column]
            if next_tree_height > largest_left:
                largest_left = next_tree_height
                visible_trees = add_tree(visible_trees, row, column)
            column += 1

        # Right to left
        found_largest_tree = False
        largest_right = lines[row][len(lines[row])-1]
        column = len(lines[row])-2
        visible_trees = add_tree(visible_trees, row, len(lines[row])-1)
        while column >= 0 and not found_largest_tree:
            next_tree_height = lines[row][column]
            if next_tree_height > largest_right:
                largest_right = next_tree_height
                visible_trees = add_tree(visible_trees, row, column)
                if next_tree_height == largest_left:
                    found_largest_tree = True
            column -= 1

    for column in range(0, len(lines[0])):
        # Top to bottom
        largest_top = lines[0][column]
        row = 1
        visible_trees = add_tree(visible_trees, 0, column)
        while row < len(lines):
            next_tree_height = lines[row][column]
            if next_tree_height > largest_top:
                largest_top = next_tree_height
                visible_trees = add_tree(visible_trees, row, column)
            row += 1

        # Bottom to top
        found_largest_tree = False
        largest_bottom = lines[len(lines[column])-1][column]
        row = len(lines[column])-2
        visible_trees = add_tree(visible_trees, len(lines)-1, column)
        while row >= 0 and not found_largest_tree:
            next_tree_height = lines[row][column]
            if next_tree_height > largest_bottom:
                largest_bottom = next_tree_height
                visible_trees = add_tree(visible_trees, row, column)
                if next_tree_height == largest_top:
                    found_largest_tree = True
            row -= 1

    
    num_trees = total_num_visible_trees(visible_trees)
    print("Part One:", num_trees)

part_one()