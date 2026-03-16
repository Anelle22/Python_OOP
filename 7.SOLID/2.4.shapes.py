from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area_calculator(self):
        pass


class Rectangle(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calculator(self):
        return self.width * self.height

class Triangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area_calculator(self):
        return (self.width * self.height) / 2

class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area_calculator()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
