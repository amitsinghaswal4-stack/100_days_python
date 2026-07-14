from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def service_cost(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def service_items(self):
        pass

    def service_report(self):
        print(f"\n{'='*45}")
        print(f"  🔧 SERVICE REPORT")
        print(f"{'='*45}")
        print(f"  Vehicle  : {self.brand} {self.model} ({self.year})")
        print(f"  Fuel     : {self.fuel_type()}")
        print(f"\n  Service Items:")
        for item in self.service_items():
            print(f"    ✔ {item}")
        print(f"\n  Total Cost : INR {self.service_cost()}")
        print(f"{'='*45}\n")


class PetrolCar(Vehicle):
    def fuel_type(self):
        return "Petrol"

    def service_cost(self):
        return 3500

    def service_items(self):
        return [
            "Engine Oil Change",
            "Oil Filter",
            "Air Filter",
            "Spark Plug Check",
            "Brake Inspection"
        ]


class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

    def service_cost(self):
        return 1500

    def service_items(self):
        return [
            "Battery Health Check",
            "Software Update",
            "Tyre Rotation",
            "Brake Fluid Check",
            "AC Filter Clean"
        ]


class Motorcycle(Vehicle):
    def fuel_type(self):
        return "Petrol"

    def service_cost(self):
        return 800

    def service_items(self):
        return [
            "Engine Oil Change",
            "Chain Lubrication",
            "Brake Adjustment",
            "Tyre Pressure Check"
        ]


# Service center processing all vehicles
vehicles = [
    PetrolCar("Honda", "City", 2021),
    ElectricCar("Tata", "Nexon EV", 2023),
    Motorcycle("Royal Enfield", "Classic 350", 2022)
]

for vehicle in vehicles:
    vehicle.service_report()