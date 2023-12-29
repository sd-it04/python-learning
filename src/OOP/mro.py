# Method Resolution Order (MRO)
class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
# Depth First Search algorithm
print(D.mro)
