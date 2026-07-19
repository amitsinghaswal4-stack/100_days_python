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
print(len(b1))     # 412    (__len__)