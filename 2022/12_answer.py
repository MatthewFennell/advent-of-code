from common import get_lines_as_array

def find_vertex_min_dist(dist, vertices):
    min_vertex = 999999999+1
    min_row = None
    min_col = None
    for vertex in vertices:
        row, column = vertex
        if dist[row][column] < min_vertex:
            min_vertex = dist[row][column]
            min_row = row
            min_col = column
    return (min_row, min_col)

def can_climb_from_to(from_letter, to_letter, is_reversed):
    if from_letter == 'S':
        from_letter = 'a'
    if to_letter == 'E':
        to_letter = 'z'

    if is_reversed:
        if from_letter == 'E':
            from_letter = 'z'
        if to_letter == 'S':
            to_letter = 'a'

    if is_reversed:
        return ord(from_letter) - ord(to_letter) <= 1

    return ord(to_letter) - ord(from_letter) <= 1

def get_neighbours(graph, node, is_reversed):
    source_row, source_col = node

    # # top left
    # if source_row == 0 and source_col == 0:
    #     return [(0,1), (1,0)]

    # # top right
    # if source_row == 0 and source_col == len(graph[0]-1):
    #     return [(0, source_col-1), (1, source_col)]

    neighbours = []

    for row_buffer in range(-1, 2):
        for column_buffer in range(-1, 2):
            new_row = source_row + row_buffer
            new_col = source_col + column_buffer
            
            if (new_row >= 0 and new_col >= 0 and new_row < len(graph) and new_col < len(graph[0])) and (abs(row_buffer) - abs(column_buffer) != 0):
                if can_climb_from_to(graph[source_row][source_col], graph[new_row][new_col], is_reversed):
                    neighbours.append((new_row, new_col))
    return neighbours

    

def dijkstras(graph, source, is_reversed):
    dist = {}
    prev = {}
    queue = []
    for row in range(0, len(graph)):
        dist[row] = {}
        prev[row] = {}
        for column in range(0, len(graph[row])):
            dist[row][column] = 999999999
            prev[row][column] = None
            queue.append((row, column))

    dist[source[0]][source[1]] = 0
    
    while len(queue) > 0:
        row, col = find_vertex_min_dist(dist, queue)
        queue = [x for x in queue if x != (row, col)]

        neighbours = get_neighbours(graph, (row, col), is_reversed)
        for n in [x for x in neighbours if x in queue]:
            alt = dist[row][col] + 1
            new_row, new_col = n
            if alt < dist[new_row][new_col]:
                dist[new_row][new_col] = alt
                prev[new_row][new_col] = (new_row, new_col)

    return dist, prev

def find_node(graph, node):
    for row in range(0, len(graph)):
        for column in range(0, len(graph[row])):
            if graph[row][column] == node:
                return (row,column)

def part_one():
    lines = get_lines_as_array('12_input.txt')
    row, column = find_node(lines, 'S')
    target_row, target_column = find_node(lines, 'E')
    dist, prev = dijkstras(lines, (row, column), False)
    print("Part One:", dist[target_row][target_column])

def part_two():
    lines = get_lines_as_array('12_input.txt')
    row, column = find_node(lines, 'E')
    dist, prev = dijkstras(lines, (row, column), True)
    min_distance = 9999999999

    for row in range(0, len(lines)):
        for column in range(0, len(lines[0])):
            if lines[row][column] == 'a':
                if dist[row][column] < min_distance:
                    min_distance = dist[row][column]

    print("Part Two:", min_distance)


part_one()
part_two()