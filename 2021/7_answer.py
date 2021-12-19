from common import getLineAsNumbers

def partOne():
    lines = getLineAsNumbers('7_input.txt')
    # lines=[16,1,2,0,4,2,7,1,2,14]
    
    numberAtEachPosition = {}

    minNum = min(list(lines))
    maxNum = max(list(lines))
    

    for x in range(0, len(lines)):
        if lines[x] in numberAtEachPosition:
            numberAtEachPosition[lines[x]] += 1
        else:
            numberAtEachPosition[lines[x]] = 1
    
    totalMovementCosts = {}

    for position in numberAtEachPosition.keys():
        numberAtPos = numberAtEachPosition[position]

        for y in range(minNum, maxNum+1):
            fuelCostToMove = abs(position - y)
            if y in totalMovementCosts:
                totalMovementCosts[y] += fuelCostToMove * numberAtEachPosition[position]
            else:
                totalMovementCosts[y] = fuelCostToMove * numberAtEachPosition[position]

    minCost = min(list(totalMovementCosts.values()))
    print("Part One:", minCost)


def partTwo():
    lines = getLineAsNumbers('7_input.txt')
    # lines=[16,1,2,0,4,2,7,1,2,14]
    
    numberAtEachPosition = {}

    minNum = min(list(lines))
    maxNum = max(list(lines))

    fuelCosts = {}

    cost = 0
    for x in range(minNum, maxNum+1):
        cost += x
        fuelCosts[x] = cost

    for x in range(0, len(lines)):
        if lines[x] in numberAtEachPosition:
            numberAtEachPosition[lines[x]] += 1
        else:
            numberAtEachPosition[lines[x]] = 1
    
    totalMovementCosts = {}

    for position in numberAtEachPosition.keys():
        numberAtPos = numberAtEachPosition[position]

        for y in range(minNum, maxNum+1):
            fuelDistance = abs(position - y)
            fuelCostToMove = fuelCosts[fuelDistance]
            if y in totalMovementCosts:
                totalMovementCosts[y] += fuelCostToMove * numberAtEachPosition[position]
            else:
                totalMovementCosts[y] = fuelCostToMove * numberAtEachPosition[position]

    minCost = min(list(totalMovementCosts.values()))
    print("Part Two:", minCost)
        

partOne()
partTwo()