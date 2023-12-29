class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  # with '_' it considered to be logically private member
        self._age = age

    def speak(self):
        print(f'my name is {self._name} , and I am {self._age} years old!')


player1 = PlayerCharacter('sid', 36)
print(player1.speak())
