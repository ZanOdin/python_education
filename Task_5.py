# -------------------------------------with lambda-------------------------------------
from functools import reduce

new_list = []
[new_list.append(elem) for elem in range(100, 1001, 2)]
print(new_list)
print(reduce(lambda a, b: a * b, new_list))
