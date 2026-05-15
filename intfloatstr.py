# Этап 2, Задача 6:
# Сделай полиморфную функцию print_moves(items),
# которая принимает список объектов и печатает результат move() каждого.
# Ожидаемый результат:
# Для списка из Vehicle, Car, Bike, ElectricCar печатаются их move() по порядку.
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand
    def move(self):
        return "moving"
    def info(self):
        return f"{self.brand}"

class Car(Vehicle):
    def __init__(self, brand: str, fuel: int):
        super().__init__(brand)
        self.fuel = fuel
    def info(self):
        return f'{self.brand}, fuel= {self.fuel}'
    def move(self):
        return "driving"

class Bike(Vehicle):
    def move(self):
        return "riding"

class ElectricCar(Car):
    def __init__(self, brand, battery, fuel):
        self.battery = battery
        super().__init__(brand,fuel)
    def info(self):
        return f'{self.brand}, fuel={self.fuel}, battery={self.battery}'
def print_moves(items):
    for item in items:
        print(item.move())
items = [Vehicle('Lada'), Car('lada',10), Bike('Honda'), ElectricCar('yamaha', 'eletro', 15)]
print(print_moves(items))



