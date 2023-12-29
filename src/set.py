# set
# unordered collections of unique objects
my_set = {1, 2, 3, 4, 5, 5, 5, 6, 4, 2, 1}
print(my_set)
my_set.add(-1)
my_set.add('my name')
print(my_set)

my_array = ['email1', 'email2', 'email1']
print(set(my_array))
print(list(set(my_array))[1])

# extra methods
# difference
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8, 9, 10}

print(f'difference: {set_1.difference(set_2)}')
print(f'          : {set_1}')
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8, 9, 10}
print(f'difference_update: {set_1.difference_update(set_2)}')
print(f'                 : {set_1}')
