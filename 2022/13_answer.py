
a = [
    # [1,1,3,1,1],
    # [1,1,5,1,1],

    # [[1],[2,3,4]],
    # [[1],4],

    [9],
    [[8,7,6]],

    # [[4,4],4,4],
    # [[4,4],4,4,4],

    # [7,7,7,7],
    # [7,7,7],

    # [],
    # [3],

    # [[[]]],
    # [[]],

    # [1,[2,[3,[4,[5,6,7]]]],8,9],
    # [1,[2,[3,[4,[5,6,0]]]],8,9]
]

def make_comparison(left, right):
    print(left, right)
    if (isinstance(left[0], int) and isinstance(right[0], int)):
        print("a")
        return right >= left
    if (isinstance(left[0], list) and isinstance(right[0], list)):
        # both lists
        if len(left[0]) == 0 and len(right[0]) > 0:
            # left list has run out first
            return True
        for x in range(0, len(left[0])):
            if x >= len(right[0]):
                # right run out first
                return True
            left_element = left[0][x]
            right_element = right[0][x]
            # maybe need to check types again here if both arrays (recurse)?

            if left_element > right_element:
                print("false b")
                return False
        return True

def part_one():
    for pair in range(0, len(a), 2):
        left = a[pair]
        right = a[pair+1]
        b = make_comparison(left, right)
        print(b)

part_one()