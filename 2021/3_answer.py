from common import getLinesAsArray

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)

def partOne():
    lines = getLinesAsArray('3_input.txt')
    
    objOnes = {}
    objZeros = {}
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if (lines[i][j] == 1):
                if j in objOnes:
                    objOnes[j] += 1
                else:
                    objOnes[j] = 1
            else:
                if j in objZeros:
                    objZeros[j] +=1
                else:
                    objZeros[j] = 1
    
    keys = objOnes.keys()
    mostCommon = []
    leastCommon = []
    for i in range(0, len(keys)):
        if objOnes[i] > objZeros[i]:
            mostCommon.append(1)
            leastCommon.append(0)
        else:
            mostCommon.append(0)
            leastCommon.append(1)
    mostCommonNumInBinary = convert(mostCommon)
    mostCommonDec = int(str(mostCommonNumInBinary), 2)

    leastCommonNumInBinary = convert(leastCommon)
    leastCommonDec = int(str(leastCommonNumInBinary), 2)

    print ("Part One: " + str(mostCommonDec * leastCommonDec))

def recurseDown(lines, index, isTakingMax):
    startingWithZero = []
    startingWithOne = []
    totalNumberOfZero = 0
    totalNumberOfOne = 0

    if (len(lines) == 1):
        return lines[0]

    for i in range(0, len(lines)):
        if (lines[i][index] == 0):
            startingWithZero.append(lines[i])
            totalNumberOfZero += 1
        else:
            startingWithOne.append(lines[i])
            totalNumberOfOne += 1

    if (isTakingMax):

        if (totalNumberOfZero > totalNumberOfOne):
            return recurseDown(startingWithZero, index+1, isTakingMax)
        else:
            return recurseDown(startingWithOne, index+1, isTakingMax)

    else:
        if (totalNumberOfOne < totalNumberOfZero):
            return recurseDown(startingWithOne, index + 1, isTakingMax)
        else:
            return recurseDown(startingWithZero, index + 1, isTakingMax)
    
  

def partTwo():
    lines = getLinesAsArray('3_input.txt')
#     lines=[  [0,0,1,0,0],
# [1,1,1,1,0],
# [1,0,1,1,0],
# [1,0,1,1,1],
# [1,0,1,0,1],
# [0,1,1,1,1],
# [0,0,1,1,1],
# [1,1,1,0,0],
# [1,0,0,0,0],
# [1,1,0,0,1],
# [0,0,0,1,0],
# [0,1,0,1,0]]
    
    resultOxygen = recurseDown(lines, 0, True)
    resultCO = recurseDown(lines, 0, False)
    oxygenBinary= convert(resultOxygen)
    oxygenDec = int(str(oxygenBinary), 2)

    coBinary= convert(resultCO)
    coDec = int(str(coBinary), 2)
    print ("Part Two: " + str(oxygenDec * coDec))


partOne() # 3901196
partTwo() # 4412188