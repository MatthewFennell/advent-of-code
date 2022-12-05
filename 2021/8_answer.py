from common import get_lines_as_array_with_split

# array = [
#     [[...one]],  [...two]]
# ]

testInput = [[['acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab'], [
'cdfeb','fcadb','cdfeb','cdbaf']],
[['be','cfbegad','cbdgef','fgaecd','cgeb','fdcge','agebfd','fecdb','fabcd','edb'], [
'fdgacbe', 'cefdb', 'cefbgd', 'gcbe']],
[['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'],[
'fcgedb', 'cgb', 'dgebacf', 'gc']],
[['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'], [
'cg', 'cg', 'fdcagb', 'cbg']],
[['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega', ], [
'efabcd', 'cedba', 'gadfec', 'cb']],
[['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga', ], [
'gecf', 'egdcabf', 'bgf', 'bfgea']],
[['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf', ], [
'gebdcfa', 'ecba', 'ca', 'fadegcb']],
[['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf', ], [
'cefg', 'dcbef', 'fcge', 'gbcadfe']],
[['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd', ], [
'ed', 'bcgafe', 'cdgba', 'cbgef']],
[['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg', ], [
'gbdfcae', 'bgc', 'cg', 'cgb']],
[['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc', ], [
'fgae', 'cfgab', 'fg', 'bagce']]]

# print(testInput)

def part_one():
    lines = get_lines_as_array_with_split('8_input.txt')
    # print(lines)
    count = 0
    for x in lines:
        for y in x[1]:
            length = len(y)
            if length == 2 or length == 3 or length == 4 or length == 7:
                count += 1
    print ("Part One", count)

    # testCount = 0
    # for x in testInput:
    #     # print(x)
    #     # print(x[1])
    #     print("")
    #     for y in x[1]:
    #         length = len(y)
    #         print("Length", length)
    #         if length == 2 or length == 3 or length == 4 or length == 7:
    #             testCount += 1
    # print ("Part One Test", testCount)

a = {
    2: 0,
    3: 1,
    4: 0,
    5: 3,
    6: 3,
    7: 1,
    'letter': 'a'
}
b = {
    2: 0,
    3: 0,
    4: 1,
    5: 1,
    6: 3,
    7: 1,
    'letter': 'b'
}
c = {
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 1,
    'letter': 'c'
}
d = {
    2: 0,
    3: 0,
    4: 1,
    5: 3,
    6: 2,
    7: 1,
    'letter': 'd'
}
e = {
    2: 0,
    3: 0,
    4: 0,
    5: 1,
    6: 2,
    7: 1,
    'letter': 'e'
}
f = {
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 3,
    7: 1,
    'letter': 'f'
}
g = {
    2: 0,
    3: 0,
    4: 0,
    5: 3,
    6: 3,
    7: 1,
    'letter': 'g'
}


def findMyLetter(digit, chars):
    objs = [a,b,c,d,e,f,g]
    for x in objs:
        allEqual = True
        for y in range(2, 8):
            if x[y] != chars[y]:
                allEqual = False
                break
        if (allEqual):
            return x['letter']

def part_two():
    lines = get_lines_as_array_with_split('8_input.txt')
    testCount = 0
    totalTotalSum = 0
    for x in lines:
        myChars = {
            'a': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
            'b': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
            'c': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
            'd': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
            'e': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
            'f': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
            'g': {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0
            },
        }
        for y in x[0]:
            length = len(y)
            for char in y:
                myChars[char][length] += 1

        previousMappings = {
            0: 'abcefg', 
            1: 'cf',
            2: 'acdeg',
            3: 'acdfg',
            4: 'bcdf',
            5: 'abdfg',
            6: 'abdefg',
            7: 'acf',
            8: 'abcdefg',
            9: 'abcdfg'
        }

        mappings = {}
        for digit in myChars.keys():
            actualLetter = findMyLetter(digit, myChars[digit])
            mappings[actualLetter] = digit
        myMappings={}
        for key in previousMappings.keys():
            val = previousMappings[key]
            temp = []
            for char in val:
                temp.append(mappings[char])
            temp.sort()
            temp = ''.join(temp)
            myMappings[temp] = key

        totalNum = ''
        for y in x[1]:
            input = ''.join(sorted(y))
            totalNum += str(myMappings[input])
        totalTotalSum += int(totalNum)
    print("Part Two:", totalTotalSum)

                



    

part_one()
part_two()
