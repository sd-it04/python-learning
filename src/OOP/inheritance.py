class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power
        # super().__init__()t()

    def attack(self):
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, no_of_arrows) -> None:
        self.name = name
        self.no_of_arrows = no_of_arrows
        # super().__init__()t()

    def attack(self) -> None:
        print(f'attack with no of arrows {self.no_of_arrows}')


wizard_1 = Wizard('sid', 100)
archer_1 = Archer('pari', 40)
print(wizard_1.sign_in())
print(archer_1.sign_in())
print(wizard_1.attack())
print(archer_1.attack())

# instance of
print('isinstances checks')
print(isinstance(wizard_1, Wizard))
print(isinstance(wizard_1, User))
print(isinstance(wizard_1, object))
