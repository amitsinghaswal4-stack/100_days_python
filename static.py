class MathUtils:
  @staticmethod
  def add(a, b):
      return a + b

  @staticmethod
  def is_even(n):
      return n % 2 == 0


# Usage — no need to create an instance
result = MathUtils.add(5, 3)
print(result)  # 8

print(MathUtils.is_even(10))  # True