from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("woof-woof")

class Cat(Animal):
    def make_sound(self):
        print("meow")

def make_sound(animals: list):
    for animal in animals:
        print(animal.animal_sound())


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()