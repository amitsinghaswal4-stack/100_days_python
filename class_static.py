class Circle:
  def __init__(self, radius):
      self.radius = radius

  def area(self):
      return 3.14 * self.radius ** 2

  def __str__(self):
      return f"Circle with radius {self.radius}"


# Using the class
c1 = Circle(5)

print(c1)              # Circle with radius 5
print(c1.area())        # 78.5
print(c1.radius)        # 5