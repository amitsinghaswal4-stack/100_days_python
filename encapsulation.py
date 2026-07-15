class BankAccount:
  def __init__(self):
      self.__balance = 0  # private variable

  def deposit(self, amount):
      self.__balance += amount

  def get_balance(self):
      return self.__balance