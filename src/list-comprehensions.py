# list/set/dictionary comprehensions
# my_list = [param for param in iterable] 'hello'
my_list = [char for char in 'hello']
print(my_list)
my_list2 = [num for num in range(1, 100)]
my_list3 = [num**2 for num in range(1, 100)]
my_list4 = [num**2 for num in range(1, 100) if num % 2 == 0]
# print(my_list2)
# print(my_list3)
print(f'List Fourth: {my_list4}')

# Set
my_set4 = {num**2 for num in range(1, 100) if num % 2 == 0}
print(f'Set Fourth: {my_set4}')

# Dict
simple_dict = {'a': 1, 'b': 2}
my_dict = {k: v**2 for k, v in simple_dict.items()}
print(f'Dictitionary: {my_dict}')

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(f'Dictitionary2: {my_dict2}')

# Excersize - duplicate
some_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

duplicates = set([char for char in some_list if some_list.count(char) > 1])

print(f'Duplicate: {list(duplicates)}')
