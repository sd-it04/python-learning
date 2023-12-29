from functools import reduce
my_list = [1, 2, 3]
print(f'Original list: {my_list}')
# map


def multiply_by_2(item):
    return item * 2


MAP = map(multiply_by_2, my_list)

print(f'Map: {list(MAP)}')

# filter


def only_odd(item):
    return item % 2 != 0


FILTER = filter(only_odd, my_list)
print(f'Filter: {list(FILTER)}')


# zip
your_list = [10, 20, 30]
ZIP = zip(my_list, your_list)

print(f'Zip: {list(ZIP)}')

# reduce


def accumulator(acc, item):
    return acc + item


REDUCE = reduce(accumulator, my_list, 0)
print(f'Reduce: {REDUCE}')
print(f'Original list: {my_list}')

# Excercise
print('Excersize: =>')
my_pet = ['sisi', 'bibi', 'titi', 'carla']

# capitalize all the pet and print the name


def capitalize(item):
    return item.upper()


MAP_E = map(capitalize, my_pet)
print(f'MyPets: {list(MAP_E)}')

# zip with sort
my_strings = ['a', 'b', 'c']
my_numbers = [5, 4, 3]


print(f'Zip: {list(zip(my_strings, sorted(my_numbers)))}')

# print all that pass over 50%

scores = [73, 20, 65, 19, 76, 100, 88]


def filter_scrores(item):
    return item > 50


print(f'Scores: {list(filter(filter_scrores, sorted(scores)))}')

# combine all the number on this list


def combine_accumulator(acc, item):
    return acc + item


print(
    f'Reduced Exc: {reduce(combine_accumulator, (my_numbers + scores))}')
