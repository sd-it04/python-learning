class User:
    def __init__(self, email) -> None:
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email) -> None:
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack with the power of {self.power}')


class Archer(User):
    def __init__(self, name, no_of_arrows, email) -> None:
        super()
        self.name = name
        self.no_of_arrows = no_of_arrows

    def attack(self) -> None:
        print(f'attack with no of arrows {self.no_of_arrows}')


wizard_1 = Wizard('sid', 100, 'wizard@email.com')
archer_1 = Archer('pari', 40, 'super@email.com')
print(wizard_1.attack())
print(archer_1.attack())

# super usage
print(wizard_1.email)
