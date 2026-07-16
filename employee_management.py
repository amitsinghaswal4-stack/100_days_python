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