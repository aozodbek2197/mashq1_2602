# 1-masala
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def area(self):
        return self.pi * self.r ** 2

    def perimeter(self):
        return 2 * self.pi * self.r

c = Circle(3)
print(f"Yuza: {c.area()}")
print(f"Perimetr: {c.perimeter()}")
# 2-masala
from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def move(self):
        print("Mashina yo'lda harakatlanmoqda")

class Bike(Transport):
    def move(self):
        print("Velosiped pedallar yordamida harakatlanmoqda")

c = Car()
c.move()

b = Bike()
b.move()
# 3-masala
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Vov vov")

class Cat(Animal):
    def make_sound(self):
        print("Miyov")

d = Dog()
c = Cat()
d.make_sound()
c.make_sound()
# 4-masala
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        return f"Naqd to'lov: {amount} so'm"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Karta orqali to'lov: {amount} so'm"

cash = CashPayment()
card = CardPayment()
print(cash.pay(100000))
print(card.pay(100000))
# 5-masala
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 5000000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000 * 40

full_time_e = FullTimeEmployee()
part_time_e = PartTimeEmployee()
print(full_time_e.calculate_salary())
print(part_time_e.calculate_salary())
