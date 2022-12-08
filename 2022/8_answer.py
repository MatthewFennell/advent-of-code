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

def time_since_seen_larger(what_ive_seen, column_number, tree_height, is_reverse, total_length):
    last_seen_keys = what_ive_seen.keys()
    keys_in_dict = [x for x in last_seen_keys if x in what_ive_seen and x >= tree_height]
    if len(keys_in_dict) == 0:
        if is_reverse:
            return total_length - column_number - 1
        return column_number
    if is_reverse:
        return min(what_ive_seen[x] for x in keys_in_dict) - column_number
    return column_number - max(what_ive_seen[x] for x in keys_in_dict)

def find_max_score(results):
    max_score = 0
    for key in results.keys():
        for key_two in results[key].keys():
            val = results[key][key_two]
            result = val['view_left'] * val['view_right'] * val['view_above'] * val['view_below']
            if result > max_score:
                max_score = result
    return max_score

def part_two():
    lines = get_number_list('8_input.txt')
    results = {}
    for row in range(0, len(lines)):
        results[row] = {}
        last_seen = {}

        for column in range(0, len(lines[row])):
            results[row][column] = {}
            tree_height = lines[row][column]            
            
            # left to right
            if column == 0:
                results[row][column]['view_left'] = 0
            elif lines[row][column] <= lines[row][column-1]:
                results[row][column]['view_left'] = 1
            else:
                num_trees_can_see_to_left = time_since_seen_larger(last_seen, column, tree_height, False, len(lines[row]))
                results[row][column]['view_left'] = num_trees_can_see_to_left
            last_seen[tree_height] = column

        last_seen = {}
        for column in range(len(lines[row])-1, -1, -1):
            tree_height = lines[row][column]            
            
            # right to left
            if column == len(lines[row])-1:
                results[row][column]['view_right'] = 0
            elif lines[row][column] <= lines[row][column+1]:
                results[row][column]['view_right'] = 1
            else:
                num_trees_can_see_to_right = time_since_seen_larger(last_seen, column, tree_height, True, len(lines[row]))
                results[row][column]['view_right'] = num_trees_can_see_to_right
            last_seen[tree_height] = column

        
    for column in range(0, len(lines[0])):
        last_seen = {}
        for row in range(0, len(lines)):
            tree_height = lines[row][column]            
            
            # top_to_bottom
            if row == 0:
                results[row][column]['view_above'] = 0
            elif lines[row][column] <= lines[row-1][column]:
                results[row][column]['view_above'] = 1
            else:
                num_trees_can_see_above = time_since_seen_larger(last_seen, row, tree_height, False, len(lines))
                results[row][column]['view_above'] = num_trees_can_see_above
            last_seen[tree_height] = row

        last_seen = {}
        for row in range(len(lines)-1, -1, -1):
            tree_height = lines[row][column]            
            
            # bottom_to_top[]
            if row == len(lines)-1:
                results[row][column]['view_below'] = 0
            elif lines[row][column] <= lines[row+1][column]:
                results[row][column]['view_below'] = 1
            else:
                num_trees_can_see_above = time_since_seen_larger(last_seen, row, tree_height, True, len(lines))
                results[row][column]['view_below'] = num_trees_can_see_above
            last_seen[tree_height] = row

    max_score = find_max_score(results)
    print("Part Two:", max_score)

part_one()
part_two()
