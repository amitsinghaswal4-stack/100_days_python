class BankAccount:
  def __init__(self):
      self.__balance = 0  # private variable

  def deposit(self, amount):
      self.__balance += amount

  def get_balance(self):
      return self.__balance


# Bank account 

class BankAccount:
    def __init__(self):
        self.__balance = 1000  # hidden, private — like the ATM's cash

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Not enough balance")

    def check_balance(self):
        return self.__balance