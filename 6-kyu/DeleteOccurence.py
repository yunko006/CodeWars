"""
EXAMPLES:
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
"""


def delete_nth(order, max_e):
    simple = list()

    for i in order:
        if simple.count(i) < max_e:
            simple.append(i)

    return simple
