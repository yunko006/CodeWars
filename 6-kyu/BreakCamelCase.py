"""
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    l = list(s)
    l_copy = l.copy()
    count = 0

    for i, c in enumerate(l):
        if c.isupper():
            l_copy.insert(i + count, " ")
            count += 1

    return "".join(l_copy)

