from common import get_line_split_on_char

def part_one():
    lines = get_line_split_on_char('14_input.txt', ' -> ')
    mappings = {}
    startString = 'CFFPOHBCVVNPHCNBKVNV'
    numberOfRounds = 40
    for x in lines:
        mappings[x[0]] = x[1]

    for round in range(0, numberOfRounds):
        print("round", round)
        currentIndex = 1
        stringLength = len(startString)
        offset = 0
        for index in range(1, stringLength):
            charString = startString[index-1+offset] + startString[index+offset]
            charToInsert = mappings[charString]
            startString = startString[:index+offset] + charToInsert + startString[index+offset:]
            offset += 1
            stringLength += 1
    
    elements = {}
    for x in startString:
        if x in elements:
            elements[x] += 1
        else:
            elements[x] = 1
    
    maxNumber = 0
    minOccurence = 99999999999999999
    for key in elements.keys():
        if elements[key] > maxNumber:
            maxNumber = elements[key]
        if elements[key] < minOccurence:
            minOccurence = elements[key]
    print("Part One:", maxNumber - minOccurence)

def part_two():
    startString = 'CFFPOHBCVVNPHCNBKVNV'
    lines = get_line_split_on_char('14_input.txt', ' -> ')
    pairCounts = {}
    numberOfRounds = 40
    mappings = {}
    letterCounts = {}
    for x in lines:
        mappings[x[0]] = x[1]
    for x in startString:
        if x in letterCounts:
            letterCounts[x] += 1
        else:
            letterCounts[x] = 1

    for x in range(1, len(startString)):
        pair = startString[x-1] + startString[x]
        if pair in pairCounts:
            pairCounts[pair] += 1
        else:
            pairCounts[pair] = 1
    
    for x in range(0, numberOfRounds):
        pairCounts = {key: pairCounts[key] for key in pairCounts if pairCounts[key] > 0}
        extraPairs = {}
        for key in pairCounts:
            letterToAdd = mappings[key]
           
            newPairOne = key[0] + letterToAdd
            newPairTwo = letterToAdd + key[1]
            if letterToAdd in letterCounts:
                letterCounts[letterToAdd] += pairCounts[key]
            else:
                letterCounts[letterToAdd] = pairCounts[key]
            if newPairOne in extraPairs:
                extraPairs[newPairOne] += pairCounts[key]
            else:
                extraPairs[newPairOne] = pairCounts[key]
            if newPairTwo in extraPairs:
                extraPairs[newPairTwo] += pairCounts[key]
            else:
                extraPairs[newPairTwo] = pairCounts[key]
            pairCounts[key] = 0
        pairCounts = {key: pairCounts[key] for key in pairCounts if pairCounts[key] > 0}
        for x in extraPairs.keys():
            if x in pairCounts:
                pairCounts[x] += extraPairs[x]
            else:
                pairCounts[x] = extraPairs[x]
    maxVal = 0
    minVal = 99999999999999999999999999999999
    for x in letterCounts:
        if letterCounts[x] > maxVal:
            maxVal = letterCounts[x]
        if letterCounts[x] < minVal:
             minVal = letterCounts[x]
    print("Part Two:", maxVal - minVal)
# part_one()
part_two()
