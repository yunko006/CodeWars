"""
pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
"""


def pyramid(n):
    pyramid_l = []
    i = 0

    while i != n:
        i += 1
        pyramid_l.append(i * [1])

    return pyramid_l
