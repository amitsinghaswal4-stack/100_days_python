from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass        

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):   
        print(f"I am a {self.__class__.__name__}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Circle Area      : {3.14 * self.radius ** 2}")

    def perimeter(self):
        print(f"Circle Perimeter : {2 * 3.14 * self.radius}")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Rectangle Area      : {self.length * self.width}")

    def perimeter(self):
        print(f"Rectangle Perimeter : {2 * (self.length + self.width)}")


class Triangle(Shape):
    def __init__(self, a, b, c, base, height):
        self.a = a  # three sides
        self.b = b
        self.c = c
        self.base = base
        self.height = height

    def area(self):
        print(f"Triangle Area      : {0.5 * self.base * self.height}")

    def perimeter(self):
        print(f"Triangle Perimeter : {self.a + self.b + self.c}")


shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(3, 4, 5, 4, 3)
]

for shape in shapes:
    shape.description()
    shape.area()
    shape.perimeter()
    print("---")