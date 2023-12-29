
from functools import reduce
# lambda param: manipulation_action(param)
my_list = [1, 2, 3]
print(f'Original list: {my_list}')
MAP = map(lambda item: item*2, my_list)
print(f'Map: {list(MAP)}')
FILTER = filter(lambda item: item % 2 != 0, my_list)
print(f'Filter: {list(FILTER)}')
REDUCE = reduce(lambda acc, item: acc+item, my_list)
print(f'Reduce: {REDUCE}')

# Excersice
my_list = [5, 4, 3]
# Square
print(f'Square: {list(map(lambda item: item ** 2, my_list))}')

# Sort
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda i: i[1])
print(f'Sort: {a}')
