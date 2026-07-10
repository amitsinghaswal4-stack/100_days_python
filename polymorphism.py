class Animal:

  def __init__(self, name):
      self.name = name          
  def speak(self):
     return


class Dog(Animal):

  def speak(self):              
      return f"{self.name} says: Woof! 🐶"


class Cat(Animal):

  def speak(self):          
      return f"{self.name} says: Meow! 🐱"


class Cow(Animal):
  def speak(self):
      return f"{self.name} says: Moo! 🐄"

print("=" * 45)
print("  EXAMPLE 1: Animals")
print("=" * 45)

animals = [
    Dog("Bruno"),
    Cat("Whiskers"),
    Cow("Daisy"),
]

for animal in animals:
    print(animal.speak())