
from project.animals.animal import Animal, Bird, Mammal
from project.food import Food, Vegetable, Meat, Seed, Fruit

class Owl(Bird):

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

class Hen(Bird):

    @property
    def weight_increment(self) -> float:
        return 0.35

    @property
    def allowed_food(self):
        return [Vegetable, Fruit, Meat, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"





