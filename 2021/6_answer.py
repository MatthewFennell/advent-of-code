from common import getLineAsNumbers

def numberOfFish(fish, daysRemaining, obj):
    if (daysRemaining == 0):
        return len(fish)

    if (daysRemaining == 128 and obj != {}):
        mySum = 0
        for x in fish:
            mySum += obj[x]
        return mySum
    
    for i in range(0, len(fish)):
        if (fish[i] == 0):
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
    return numberOfFish(fish, daysRemaining-1, obj)

obj_128 = {
    0: numberOfFish([0], 128, {}),
    1: numberOfFish([1], 128, {}),
    2: numberOfFish([2], 128, {}),
    3: numberOfFish([3], 128, {}),
    4: numberOfFish([4], 128, {}),
    5: numberOfFish([5], 128, {}),
    6: numberOfFish([6], 128, {}),
    7: numberOfFish([7], 128, {}),
    8: numberOfFish([8], 128, {}),
}

def partOne():
    lines = getLineAsNumbers('6_input.txt')
    numberOfDays = 80
    myObj = {
        1: numberOfFish([1], numberOfDays, {}),
        2: numberOfFish([2], numberOfDays, {}),
        3: numberOfFish([3], numberOfDays, {}),
        4: numberOfFish([4], numberOfDays, {}),
        5: numberOfFish([5], numberOfDays, {}),
        6: numberOfFish([6], numberOfDays, {}),
    }

    totalNumberOfFish = 0
    for x in lines:
        totalNumberOfFish += myObj[x]
    print("Part One", totalNumberOfFish)

def partTwo():
    lines = getLineAsNumbers('6_input.txt')

    numberOfDays = 256
    six= numberOfFish([6], 256, obj_128)
    five= numberOfFish([5], 129, obj_128)
    four= numberOfFish([4], 129, obj_128)
    three= numberOfFish([3], 129, obj_128)
    two= numberOfFish([2], 129, obj_128)
    one= numberOfFish([1], 129, obj_128)

    myObj = {
        1: numberOfFish([1], numberOfDays, obj_128),
        2: numberOfFish([2], numberOfDays, obj_128),
        3: numberOfFish([3], numberOfDays, obj_128),
        4: numberOfFish([4], numberOfDays, obj_128),
        5: numberOfFish([5], numberOfDays, obj_128),
        6: numberOfFish([6], numberOfDays, obj_128),
    }

    totalNumberOfFish = 0
    for x in lines:
        totalNumberOfFish += myObj[x]
    print("Part Two:", totalNumberOfFish)

partOne()
partTwo()