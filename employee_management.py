from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name              # public attribute
        self._salary = salary         # protected (single underscore)
        self.__bonus = 0              # private (double underscore) -> Encapsulation

    @abstractmethod
    def work(self):
        pass                          # forces child classes to implement this

    # ---------- Encapsulation ----------
    def set_bonus(self, amount):
        if amount > 0:
            self.__bonus = amount
        else:
            print("Bonus must be positive!")

    def get_salary(self):
        return self._salary + self.__bonus


# ---------- Inheritance ----------
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)   # calling parent constructor
        self.language = language

    # ---------- Polymorphism (method overriding) ----------
    def work(self):
        print(f"{self.name} writes code in {self.language}.")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    # ---------- Polymorphism (method overriding) ----------
    def work(self):
        print(f"{self.name} manages a team of {self.team_size} people.")


# ---------- Using the classes (Objects) ----------
emp1 = Developer("Aarav", 50000, "Python")
emp2 = Manager("Priya", 70000, 8)

emp1.set_bonus(5000)
emp2.set_bonus(10000)

employees = [emp1, emp2]   # list of Employee objects

for emp in employees:
    emp.work()                                   # same method call, different behavior -> Polymorphism
    print(f"Total salary: {emp.get_salary()}")
    print("-" * 30)