from abc import ABC, abstractmethod

#Abstraction
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name             
        self._salary = salary         # protected (single underscore)
        self.__bonus = 0              

    @abstractmethod
    def work(self):
        pass                       

    #Encapsulation
    def set_bonus(self, amount):
        if amount > 0:
            self.__bonus = amount
        else:
            print("Bonus must be positive!")

    def get_salary(self):
        return self._salary + self.__bonus


#Inheritance
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)   
        self.language = language

    # Polymorphism
    def work(self):
        print(f"{self.name} writes code in {self.language}.")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    #Polymorphism
    def work(self):
        print(f"{self.name} manages a team of {self.team_size} people.")


# Using classes 
emp1 = Developer("Aarav", 50000, "Python")
emp2 = Manager("Priya", 70000, 8)

emp1.set_bonus(5000)
emp2.set_bonus(10000)

employees = [emp1, emp2]   

for emp in employees:
    emp.work()                                   
    print(f"Total salary: {emp.get_salary()}")
    print("-" * 30)


#Another example to clarify the oops concept


from abc import ABC, abstractmethod



class BankAccount(ABC):
    def __init__(self, owner, balance=0):
        self._owner = owner          # protected attribute
        self.__balance = balance     # private attribute (ENCAPSULATION)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def account_type(self):
        """Each account type must define itself."""
        pass

    def display_info(self):
        print(f"Owner: {self._owner} | Type: {self.account_type()} | Balance: ₹{self.get_balance()}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=4):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def account_type(self):
        return "Savings"

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ₹{interest:.2f} added.")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=5000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self):
        return "Current"

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            self._BankAccount__balance = self.get_balance() - amount  # adjusting private var via name mangling
            print(f"Withdrew ₹{amount} (overdraft allowed). New balance: ₹{self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit!")


def demo_polymorphism(accounts):
    for acc in accounts:
        acc.display_info()
        
if __name__ == "__main__":
    savings = SavingsAccount("Riya", balance=10000, interest_rate=5)
    current = CurrentAccount("Aman", balance=2000, overdraft_limit=3000)

    print("----- Initial Info -----")
    demo_polymorphism([savings, current])

    print("\n----- Transactions -----")
    savings.deposit(2000)
    savings.add_interest()

    current.withdraw(4000)   # uses overdraft
    current.withdraw(5000)   # exceeds limit should fail

    print("\n----- Final Info -----")
    demo_polymorphism([savings, current])