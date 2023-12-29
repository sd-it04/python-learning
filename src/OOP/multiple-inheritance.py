class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows) -> None:
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attack with no of arrows {self.arrows}')

    def run(self):
        print('run very fast')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard_1 = Wizard('sid', 100)
archer_1 = Archer('pari', 40)
print(wizard_1.attack())
print(archer_1.attack())

# multiple inheritance

print('___ Multiple Inheritance __')
hb1 = Hybrid('borgi', 88, 999)
print(hb1.arrows)
print(hb1.power)
print(hb1.sign_in())
