class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('cat_1', 1)
cat2 = Cat('cat_2', 2)
cat3 = Cat('cat_3', 3)

cats = [cat1.age, cat2.age, cat3.age]


def oldestCat(*args):
    return max(args)


print(f'oldest cat is {oldestCat(cat1.age, cat2.age, cat3.age)} years old.')
