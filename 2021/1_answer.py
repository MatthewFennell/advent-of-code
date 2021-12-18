from common import getLinesAsNumbers

def partOne():
    lines = getLinesAsNumbers('1_input.txt')
    numberOfIncreases = 0
    for i in range(0, len(lines)):
        if (i > 0 and lines[i] > lines[i-1]):
            numberOfIncreases += 1
    print ("Part One: " + str(numberOfIncreases))

def partTwo():
    lines = getLinesAsNumbers('1_input.txt')
    windows = []
    numberOfIncreases = 0
    for i in range(2, len(lines)):
        windows.append(lines[i-2] + lines[i-1] + lines[i])
    
    for i in range(0, len(windows)):
        if (windows[i] > windows[i-1]):
            numberOfIncreases += 1
    print ("Part Two: " + str(numberOfIncreases))


partOne() # 1316
partTwo() # 1344

