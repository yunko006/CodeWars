def array_diff(a, b):
    not_list = a.copy()
    # print(not_list)
    for x in a:
        for i in b:
            if i in not_list:
                not_list.remove(i)

    return not_list


# A better solution

def array_diff(a, b):

    return [x for x in a if x not in b]
