class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'my name is {self.name} , and I am {self.age} years old!')


player1 = PlayerCharacter('sid', 36)
print(player1.speak())
