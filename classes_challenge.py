from typing import Any


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        x = self.length * self.width
        return f" The area is {x}"
    def perimeter(self):
        y = (self.length + self.width) * 2
        return f"The perimeter is {y}"


rectangle = Rectangle(6, 8)
print(rectangle.area())
print(rectangle.perimeter())
        
# Task 2

class Bank_Account:
    def __init__(self, balance, deposit, withdraw):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        
    def deposit_money(self):
        return self.balance + self.deposit
    def withdraw_money(self):
        return self.balance - self.withdraw

account1 = Bank_Account(1000,100, 250 )
print(account1.deposit_money())
print(account1.withdraw_money())

#Task 3

class Car:
    def __init__(self, make, model,year):
        self.make = make
        self.model =model
        self.year = year
    def get_make(self):
        return self.make
    def set_make(self, value):
        self.make = value
    def get_model(self):
        return self.model
    def set_model(self, value):
        self.model = value
    def get_year(self):
        return self.year
    def set_year(self, value):
        self.year = value

car1 = Car("Honda", "Civic", 2019)
car1.set_make("Toyota")
print(car1.make)
print(car1.model)

# Task 4
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
product1 = Product("Shampoo", 10, 10)
print(product1.total_price())