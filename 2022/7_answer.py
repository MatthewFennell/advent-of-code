from common import get_lines

def add_file(dic, path, file):
    temp_dic = dic
    for x in path:
        temp_dic = temp_dic[x]
    temp_dic['files'].append(file)
    temp_dic['immediate_filesize'] += file['filesize']
    return dic

def increment_total_filesize(dic, path, size):
    temp_dic = dic
    for x in path:
        temp_dic = temp_dic[x]
    temp_dic['total_filesize'] += size
    return dic

def set_total(dic, path, size):
    temp_dic = dic
    for x in path:
        temp_dic = temp_dic[x]
    temp_dic['total_size'] = size
    return dic

def add_new_field(dic, path, new_entry):
    temp_dic = dic
    for x in path:
        temp_dic = temp_dic[x]
    temp_dic[new_entry] = {"files": [], "immediate_filesize": 0, "total_filesize": 0}
    return dic

def build_directories(lines):
    current_path = []
    folder_structure = {"files": [], "immediate_filesize": 0, "total_filesize": 0}
    is_file = False
    for line in lines:            
        if line.startswith("$"):
            is_file = False
            line = line.replace("$ ", "")
            if line == "cd /":
                pass
            elif line.startswith('cd'):
                line = line.replace('cd ', '')
                
                if line == "..":
                    current_path.pop()
                else:
                    current_path.append(line)
            elif line == 'ls':
                is_file = True
        elif line.startswith('dir'):
            line = line.replace('dir ', '')
            folder_structure = add_new_field(folder_structure, current_path, line)
        elif is_file:
            filesize, filename = line.split(' ')
            folder_structure = add_file(folder_structure, current_path, {"filename": filename, "filesize": int(filesize)})
            for x in range(len(current_path)+1):
                folder_structure = increment_total_filesize(folder_structure, current_path[:x], int(filesize))
    return folder_structure

def find_small_directories(dic, limit, tempKey=None):
    other_dicts = [key for key in dic.keys() if key != 'files' and key != 'immediate_filesize' and key != 'total_filesize']
    if len(dic.keys()) == 3:
        filesize = dic['total_filesize']
        return filesize if filesize <= limit else 0
    active_sum = dic['total_filesize']
    actual_sum = active_sum if active_sum <= limit else 0
    return actual_sum + sum(find_small_directories(dic[key], limit) for key in other_dicts)

def find_smallest_directory_to_delete(dic, limit):
    smallest = dic['total_filesize']

    other_dicts = [key for key in dic.keys() if key != 'files' and key != 'immediate_filesize' and key != 'total_filesize']
    
    other_results = [find_smallest_directory_to_delete(dic[key], 1) for key in other_dicts]
    other_results.append(smallest)
    return min(x for x in other_results if x >= limit)

def get_all_totals(dic):
    other_dicts = [key for key in dic.keys() if key != 'files' and key != 'immediate_filesize' and key != 'total_filesize']
    result = [get_all_totals(dic[key]) for key in other_dicts]
    flat_list = [item for sublist in result for item in sublist]
    return [dic['total_filesize'], *flat_list]

def part_one():
    lines = get_lines('7_input.txt')
    directories = build_directories(lines)
    total_sum = find_small_directories(directories, 100000)
    print("Part One:", total_sum)

def part_two():
    lines = get_lines('7_input.txt')
    directories = build_directories(lines)
    total_size = directories['total_filesize']
    unusued_space = 70000000 - total_size
    amount_required_to_delete = 30000000 - unusued_space
    print("The total size:", total_size)
    print("usunsed space:", unusued_space)
    print("amount to delete", amount_required_to_delete)
    # smallest = find_smallest_directory_to_delete(directories, amount_required_to_delete)
    # print("Part Two:", smallest)

    all_totals = get_all_totals(directories)
    min_to_delete = min(x for x in all_totals if x >= amount_required_to_delete)
    print("min to delete", min_to_delete)

a = [1,2,3]

b = [*a]

part_one()
part_two()

# dic = {"files": [], "immediate_filesize": 100, "b": {"files": [], "immediate_filesize": 110}}
# score = combined_filesize(dic)
# print(score)
