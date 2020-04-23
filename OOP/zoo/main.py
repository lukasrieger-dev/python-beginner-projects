# An example of OOP, inheritance, polymorphy and dynamic binding in Python

__author__ = 'codinglukas'


class Animal:
    """
    Animal is the super class which provides basic functionality.
    We want to extend it in the base classes to add species specific code.
    """

    def __init__(self, species, is_mammal):
        self.species = species
        self.is_mammal = is_mammal
        self.energy = 100
        self.position = (0, 0)

    def __repr__(self):
        return f'{self.species}, is mammal: {self.is_mammal}, energy: {self.energy}, position: {self.position}'

    def walk(self, x=0, y=0):
        self.energy -= 1
        self.position = x, y

    def eat(self, amount):
        print(f'{self.species} is eating')
        if self.energy + amount > 100:
            self.energy = 100
        else:
            self.energy += amount


class Owl(Animal):
    """
    The class Owl has all the functionality from the base class Animal
    and defines additional attributes and methods for owls.
    """

    def __init__(self, name):
        # call the super class's constructor
        super(Owl, self).__init__('Owl', False)
        self.name = name

    def fly(self, x=0, y=0):
        # flying costs more energy
        self.energy -= 2
        # use inherited method
        self.walk(x, y)


class Frog(Animal):
    def __init__(self, name):
        # call the super class's constructor
        super(Frog, self).__init__('Frog', False)
        self.name = name

    def jump(self, x=0, y=0):
        self.energy -= 1
        self.walk(x, y)

    def eat(self, amount):
        """
        Our frogs need more food, they have to eat
        twice the amount of an owl to get back the energy.
        Class Frog overrides the inherited method eat().
        """
        print(f'{self.name} is eating - overridden method')
        a = amount // 2
        if self.energy + a > 100:
            self.energy = 100
        else:
            self.energy += a


def feed_animals(amount):
    """
    Since all animals inherit from the base class, we can
    treat them as instances of class Animal (polymorphy).
    However, the eat() method executes the most specific implementation,
    so that we get another output for a call of eat() on a frog than on
    an owl. This is called dynamic binding.
    """
    for animal in zoo:
        animal.eat(amount)


# Instantiate the Animals
o1 = Owl('Gerry')
o2 = Owl('Alice')
f = Frog('Bob')

# Check the animals' data
print(f.name, f)
print(o1.name, o1)
print(o2.name, o2)

# zoo is a list of animals
zoo = [o1, o2, f]

# some activities going on in the zoo
o1.fly(2, 3)
o2.walk(1, 4)
o1.fly(3, 6)
f.jump(1, 5)
o1.fly(2, 3)
o1.walk(3, 3)
f.jump(1, 9)
f.jump(3, 9)
o2.fly(5, 5)

# check the animals' data again
print(f.name, f)
print(o1.name, o1)
print(o2.name, o2)

# feed the animals, energy levels go up
feed_animals(4)

# animals' data again, check if energy levels have increased
print(f.name, f)
print(o1.name, o1)
print(o2.name, o2)

