from common import getLineAsNumbers

def numberOfFish(fish, daysRemaining):
    if (daysRemaining == 0):
        return len(fish)
    
    for i in range(0, len(fish)):
        if (fish[i] == 0):
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
    return numberOfFish(fish, daysRemaining-1)

def partOne():
    lines = getLineAsNumbers('6_input.txt')
    # print(lines)

    numberOfDays = 80

    myObj = {
        1: numberOfFish([1], numberOfDays),
        2: numberOfFish([2], numberOfDays),
        3: numberOfFish([3], numberOfDays),
        4: numberOfFish([4], numberOfDays),
        5: numberOfFish([5], numberOfDays),
        6: numberOfFish([6], numberOfDays),
    }

    totalNumberOfFish = 0
    for x in lines:
        totalNumberOfFish += myObj[x]

def partTwo():
    lines = getLineAsNumbers('6_input.txt')
    # print(lines)

    numberOfDays = 256

    # myObj = {
    #     1: numberOfFish([1], numberOfDays),
    #     2: numberOfFish([2], numberOfDays),
    #     3: numberOfFish([3], numberOfDays),
    #     4: numberOfFish([4], numberOfDays),
    #     5: numberOfFish([5], numberOfDays),
    #     6: numberOfFish([6], numberOfDays),
    # }
    y= numberOfFish([6], 256)
    print(y)

    # totalNumberOfFish = 0
    # for x in lines:
    #     totalNumberOfFish += myObj[x]
    # print("Part Two:", totalNumberOfFish)

partOne()
partTwo()