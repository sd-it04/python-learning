# OOP
class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def run(self):
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy', num1+num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1+num2


# player1 = PlayerCharacter('player1', 20)
print(PlayerCharacter.adding_things(5, 3))
