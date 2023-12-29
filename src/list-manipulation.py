# list is mutable
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0::3])


# adding
basket = [1, 2, 3, 4, 5]
print('_____ Adding ______')
new_list = basket.insert(2, 100)
print(basket)
print(new_list)

extended_list = basket.extend([101, 102])
print(basket)
print(f'extended_list: {extended_list}')

# removing
print('_____ Removing ______')
basket.pop()
print(basket)

basket.remove(2)
print(basket)

# manipulation 2
print('_____ Index ______')
basket = ['a', 'b', 'c', 'd']
print(basket.index('d'))
print('x' in basket)
print('Count:', basket.count('d'))

# manipulation 3
print('_____ Sort ______')
basket = ['a', 'b', 'c', 'd', 'e', 'd']
basket.sort()
print('Original:    ', basket)
print('List.sort(): ', basket)
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print('Original:    ', basket)
print('sorted():    ', sorted(basket))
print('_____ Reverse & Copy ______')
basket = ['a', 'b', 'c', 'd', 'e', 'd']
basket.reverse()
print('Original:    ', basket)
print('revese():    ', basket)
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# unpacking
print('_____ Unpacking ______')
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
print(b)
print(c)
print(other)
print(d)
