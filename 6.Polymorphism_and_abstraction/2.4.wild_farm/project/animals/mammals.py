
from project.animals.animal import Animal, Bird, Mammal
from project.food import Food, Vegetable, Meat, Seed, Fruit

class Mouse(Mammal):

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @property
    def weight_increment(self) -> float:
        return 0.1

    @staticmethod
    def make_sound():
        return "Squeak"

class Dog(Mammal):

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.4

    @staticmethod
    def make_sound():
        return "Woof!"

class Cat(Mammal):

    @property
    def allowed_food(self):
        return [Vegetable, Meat]

    @property
    def weight_increment(self) -> float:
        return 0.3

    @staticmethod
    def make_sound():
        return "Meow"

class Tiger(Mammal):

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
