from common import getLines

def isMatchingBracket(cur, stack):
    if (len(stack) == 0):
        return False
    topStack = stack[-1]
    if (cur == ")"):
        return topStack == "("
    if (cur == "}"):
        return topStack == "{"
    if (cur == "]"):
        return topStack == "["
    if (cur == ">"):
        return topStack == "<"
    return False

def getMatching(b):
    if b == '(':
        return ')'
    elif b == '{':
        return '}'
    elif b == '[':
        return ']'
    elif b == '<':
        return '>'

def isOpeningBracket(b):
    return b == "(" or b == "{" or b == "[" or b == "<"

def partOne():
    scoreMappings = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    newScoreMappings = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    
    lines = getLines('10_input.txt')
    # lines=['[({(<(())[]>[[{[]{<()<>>']
    incorrectBrackets = []
    totalScore = 0
    allScores = []
    for x in lines:
        stack = []
        isGood = True
        for y in x:
            if (isOpeningBracket(y)):
                stack.append(y)
            else:
                isMatching = isMatchingBracket(y, stack)
                if (isMatching):
                    stack.pop()
                else:
                    totalScore += scoreMappings[y]
                    isGood = False
                    break
        if (isGood):
            reversedStack = stack[::-1]
            myStack = []
            for x in reversedStack:
                myStack.append(getMatching(x))
            myScore = 0
            for x in myStack:
                myScore = myScore * 5
                myScore += newScoreMappings[x]
            allScores.append(myScore)
    allScores.sort()
    middleIndex = round((len(allScores)-1) / 2)
    middle = allScores[middleIndex]
    print("Part One:", totalScore)
    print("Part Two:", middle)

partOne()
