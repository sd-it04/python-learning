# Dictionary not sorted | not ordered | key-value
# List is ordered | list of entries
dictionary = {
    123: [1, 2, 3],
    'b': 'hello',
    True: True
}

print(dictionary[123][1])

# dictonary methods
user = {
    'age': 30,
    'title': 'Mr.',
    'lastname': 'Bob',
}

print(user['age'])
print(user.get('name'))
print(user.get('name', 'Sid'))

# another way to create a dictionary

user2 = dict(name='MyName')
print(user2)
print('size' in user2)
print('name' in user2.keys())
print(user2.items())
print(user.items())
dictionary.pop(True)
print(dictionary)
user.popitem()
print(user)
