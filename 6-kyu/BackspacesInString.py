"""
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""


def clean_string(s):
    cleaned = []

    for char in s:
        if char != '#':
            cleaned.append(char)
        elif cleaned:
            # if list is not empty
            # dont use remove or it will delete all same char from the list
            cleaned.pop()

    return ''.join(cleaned)
