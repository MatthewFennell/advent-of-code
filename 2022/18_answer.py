from common import get_lines_as_numbers


def add_entry(x,y,z, locations):

    if x not in locations:
        locations[x] = {}
        locations[x][y] = {}
        locations[x][y][z] = True
        return locations

    if y not in locations[x]:
        locations[x][y] = {}
        locations[x][y][z] = True
        return locations
    
    if z not in locations[x][y]:
        locations[x][y][z] = True
        return locations

def is_field_present(x,y,z,locations):
    return x in locations and y in locations[x] and z in locations[x][y]

def get_num_neighbours(x,y,z,locations):
    num_neighbours = 0
    # left/right (x) | up/down (y) | forwards/backwards (z)

    # Look left / right
    if not is_field_present(x-1,y,z,locations):
        num_neighbours += 1
    if not is_field_present(x+1,y,z,locations):
        num_neighbours += 1

    # Look up / down
    if not is_field_present(x,y+1,z,locations):
        num_neighbours += 1
    if not is_field_present(x,y-1,z,locations):
        num_neighbours += 1

    # Look forwards/backwards
    if not is_field_present(x,y,z+1,locations):
        num_neighbours += 1
    if not is_field_present(x,y,z-1,locations):
        num_neighbours += 1

    return num_neighbours


def part_one():
    lines = get_lines_as_numbers('18_input.txt')
    locations = {}

    for line in lines:
        x,y,z = line
        locations = add_entry(x,y,z, locations)

    total = 0
    
    for x in locations.keys():
        for y in locations[x].keys():
            for z in locations[x][y].keys():
                total += get_num_neighbours(x,y,z,locations)

    print("total", total)


part_one()