class Shape:
  def area(self):
      raise NotImplementedError("Subclass must implement area()")

  def describe(self):
      return f"{self._class.name_} has area {self.area():.2f}"


class Circle(Shape):
  def _init_(self, radius):
      self.radius = radius

  def area(self):
      return 3.14159 * self.radius ** 2


class Rectangle(Shape):
  def _init_(self, width, height):
      self.width = width
      self.height = height

  def area(self):
      return self.width * self.height


class Triangle(Shape):
  def _init_(self, base, height):
      self.base = base
      self.height = height

  def area(self):
      return 0.5 * self.base * self.height


# Polymorphism in action: same method call, different behavior
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
  print(shape.describe())