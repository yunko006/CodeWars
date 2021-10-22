"""
Examples:
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    # convert n to str

    result = 0

    for num in str(n):
        result += int(num)
        # print(len(str(result)))

    if len(str(result)) != 1:
        return digital_root(result)


    return result


a = digital_root(493193)
print(a)
