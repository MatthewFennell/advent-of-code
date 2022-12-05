from common import get_line_split_on_char

def flatten(t):
    return [item for sublist in t for item in sublist]

def combineToPaths(paths):
    allPaths = []
    curPath = []
    for x in paths:
        if x == 'end':
            curPath.append(x)
            allPaths.append(curPath)
            curPath=[]
        else:
            curPath.append(x)
    return allPaths

def findRoutes(start, currentRoute, options, visited):
    # print("start", start)
    if start == 'end':
        return currentRoute
    
    paths = []
    # print ("Options", options[start])
    # print("visited", visited.keys())
    for x in options[start]:
        if x not in visited or x.isupper():
            # print("Visiting", x, " from", currentRoute)
            paths.append(findRoutes(x, [*currentRoute, x], options, {**visited, x: True}))
    return flatten(paths)

def part_one():
    options = {}
    lines = get_line_split_on_char('12_input.txt', '-')

    for x in range(0, len(lines)):
        start = lines[x][0]
        destination = lines[x][1]
        if start in options:
            options[start].append(destination)
        else:
            options[start] = [destination]
        if destination in options:
            options[destination].append(start)
        else:
            options[destination] = [start]
    paths = findRoutes('start', ['start'], options, {'start': True})
    # print(paths)
    allPaths = combineToPaths(paths)
    print("Part One:", len(allPaths))

def findRoutesTwo(start, currentRoute, options, visited, visitedSmall):
    # print("start", start)
    if start == 'end':
        return currentRoute
    
    paths = []
    # print ("Options", options[start])
    # print("visited", visited.keys())
    for x in options[start]:
        if x not in visited or x.isupper() or (x in visited and x.islower() and x != 'start' and x!= 'end' and not visitedSmall):
            # print("Visiting", x, " from", currentRoute)
            paths.append(findRoutesTwo(x, [*currentRoute, x], options, {**visited, x: True}, visitedSmall or(x in visited and x.islower() and x != 'start' and x!= 'end')))
    return flatten(paths)

def part_two():
    options = {}
    lines = get_line_split_on_char('12_input.txt', '-')

    for x in range(0, len(lines)):
        start = lines[x][0]
        destination = lines[x][1]
        if start in options:
            options[start].append(destination)
        else:
            options[start] = [destination]
        if destination in options:
            options[destination].append(start)
        else:
            options[destination] = [start]
    paths = findRoutesTwo('start', ['start'], options, {'start': True}, False)
    allPaths = combineToPaths(paths)
    print("Part Two:", len(allPaths))

part_one()
part_two()