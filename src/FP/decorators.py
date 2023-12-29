from time import time
# Decorator


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('******')
        func(*args, **kwargs)
        print('******')
    return wrapper


def decorator_performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Time taken {t2-t1} sec')
        return result
    return wrapper


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


print(hello('Not in mood!!!'))
print(hello('Awesome hello', ':*)'))


@decorator_performance
def long_calculation():
    for i in range(100000000):
        i ** 2


long_calculation()
