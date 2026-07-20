class Book:
  def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages

  def __str__(self):
      # Used by print() and str() -- human-friendly
      return f"{self.title} by {self.author}"

  def __repr__(self):
      # Used in debugging/console -- unambiguous, ideally re-creatable
      return f"Book({self.title!r}, {self.author!r}, {self.pages})"

  def __eq__(self, other):
      if not isinstance(other, Book):
          return NotImplemented
      return (self.title, self.author) == (other.title, other.author)

  def __len__(self):
      return self.pages


b1 = Book("Dune", "Frank Herbert", 412)
b2 = Book("Dune", "Frank Herbert", 412)

print(b1)          # Dune by Frank Herbert   (__str__)
print(repr(b1))    # Book('Dune', 'Frank Herbert', 412)  (__repr__)
print(b1 == b2)    # True   (__eq__)
print(len(b1))     # 412    (__len__

#Fraction class behaving like real number type
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator can't be zero")
        common = gcd(numerator, denominator)
        self.num = numerator // common
        self.den = denominator // common

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __add__(self, other):
        return Fraction(
            self.num * other.den + other.num * self.den,
            self.den * other.den
        )

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __neg__(self):          # unary minus: -frac
        return Fraction(-self.num, self.den)

    def __abs__(self):          # abs(frac)
        return Fraction(abs(self.num), self.den)

    def __float__(self):        # float(frac)
        return self.num / self.den

    def __bool__(self):         # if frac:
        return self.num != 0


a = Fraction(1, 2)
b = Fraction(1, 3)

print(a + b)          # 5/6        <- __add__ then __str__
print(a * b)          # 1/6        <- __mul__
print(a < b)          # False      <- __lt__
print(a == Fraction(2, 4))  # True <- __eq__ (auto-simplified, so 1/2 == 2/4)
print(-a)             # -1/2       <- __neg__
print(abs(Fraction(-3, 4)))  # 3/4 <- __abs__
print(float(a))       # 0.5        <- __float__
print(bool(Fraction(0, 5)))  # False <- __bool__