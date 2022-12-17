from common import get_lines

def find_exclusion(x1,y1,x2,y2, row, exclusions):
    distance_away = abs(x1-x2) + abs(y1-y2)
    is_beacon_to_left = x2 < x1
    is_beacon_to_right = x1 < x2
    distance_to_target_row = abs(y1-row)

    max_length_along_target_row = distance_away - distance_to_target_row

    if is_beacon_to_left:
        exclusion_min = x1 - max_length_along_target_row + 1
        exclusion_max = x1 + max_length_along_target_row + 1

    elif is_beacon_to_right:
        exclusion_min = x1 - max_length_along_target_row - 1
        exclusion_max = x1 + max_length_along_target_row - 1

    else: 
        return exclusions

    for x in range(exclusion_min, exclusion_max+1):
        exclusions[x] = True

    return exclusions

def part_one():
    exclusions = {}
    lines = get_lines('15_input.txt')
    for x in lines:
        x1,y1,x2,y2 = [int(x) for x in x.replace('Sensor at x=', '').replace(' closest beacon is at x=', '').replace(' y=', '').replace(':', ',').split(',')]

    
    for x in lines:
        x1,y1,x2,y2 = [int(x) for x in x.replace('Sensor at x=', '').replace(' closest beacon is at x=', '').replace(' y=', '').replace(':', ',').split(',')]
        exclusions = find_exclusion(x1,y1,x2,y2,2000000,exclusions)
    print("Part One:", len(exclusions.keys()))

def add_field(x,y,fields):
    if x in fields:
        if y in fields[x]:
            fields[x][y] += 1
        else:
            fields[x][y] = 1
    else:
        fields[x] = {}
        fields[x][y] = 1
    return fields, fields[x][y] == 4

def add_field_custom(x,y,fields):
    if x in fields:
        fields[x][y] = True
    else:
        fields[x] = {}
        fields[x][y] = True
    return fields

def walk_along_edge(x1,y1,x2,y2, perimeter_locations, intersections):
    distance_away = abs(x1-x2) + abs(y1-y2)

    start_x = x1
    start_y = y1 - distance_away - 1

    right_x = x1 + distance_away + 1
    right_y = y1

    bottom_x = x1
    bottom_y = y1 + distance_away + 1

    left_x = x1 - distance_away - 1
    left_y = y1


    # top to right
    for d in range(0, distance_away + 1):
        top_right_x = start_x + d
        top_right_y = start_y + d

        bottom_right_x = right_x - d
        bottom_right_y = right_y + d

        bottom_left_x = bottom_x- d
        bottom_left_y = bottom_y -d

        top_left_x = left_x + d
        top_left_y = left_y - d

        # print("Walking top right", top_right_x, top_right_y)
        # print("Walking bottom right", bottom_right_x, bottom_right_y)
        # print("Walking bottom left", bottom_left_x, bottom_left_y)

        perimeter_locations, is_match = add_field(top_right_x, top_right_y, perimeter_locations)
        if is_match:
            intersections = add_field_custom(top_right_x, top_right_y, intersections)

        perimeter_locations, is_match = add_field(bottom_right_x, bottom_right_y, perimeter_locations)
        if is_match:
            intersections = add_field_custom(bottom_right_x, bottom_right_y, intersections)

        perimeter_locations, is_match = add_field(bottom_left_x, bottom_left_y, perimeter_locations)
        if is_match:
            intersections = add_field_custom(bottom_left_x, bottom_left_y, intersections)

        perimeter_locations, is_match = add_field(top_left_x, top_left_y, perimeter_locations)
        if is_match:
            intersections = add_field_custom(top_left_x, top_left_y, intersections)

    return perimeter_locations, intersections
    
def part_two():
    lines = get_lines('15_input.txt')
    intersections = {}
    perimeter_locations = {}
    for x in lines:
        xx1,yy1,xx2,yy2 = [int(x) for x in x.replace('Sensor at x=', '').replace(' closest beacon is at x=', '').replace(' y=', '').replace(':', ',').split(',')]
        perimeter_locations, intersections = walk_along_edge(xx1, yy1, xx2, yy2, perimeter_locations, intersections)


    for xx in intersections:
        for yy in intersections[xx]:

            is_further_away = True
            for line in lines:
                
                x1,y1,x2,y2 = [int(line) for line in line.replace('Sensor at x=', '').replace(' closest beacon is at x=', '').replace(' y=', '').replace(':', ',').split(',')]
                sensor_distance = abs(x1-x2) + abs(y1-y2)
                my_distance = abs(xx-x1) + abs(yy-y1)
                if my_distance <= sensor_distance:
                    is_further_away = False
                    break
                if xx > 4000000 or yy > 4000000 or xx < 0 or yy < 0:
                    is_further_away = False
                    break
            if is_further_away:
                print("Part 2:", xx * 4000000 + yy)

                    


# part_one()
part_two()

