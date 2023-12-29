# OOP
class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('player1', 20)
player2 = PlayerCharacter('player2', 30)

print(
    f'name: {player1.name} | age: {player2.age} | membership: {player1.membership}')
print(player2.name)
