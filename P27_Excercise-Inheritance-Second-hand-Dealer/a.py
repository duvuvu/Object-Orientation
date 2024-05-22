from abc import ABC # abstract class

class Vehicle(ABC): # inheritance of ABC renders this class abstract
    def __init__(self, year, brand, model, kilometres, asking_price):
        pass

class Van(Vehicle):
    def __init__(self, year, brand, model, kilometres, asking_price, payload):
        super().__init__(year, brand, model, kilometres, asking_price)

class Car(Vehicle):
    def __init__(self, year, brand, model, kilometres, asking_price, colour, seats):
        super().__init__(year, brand, model, kilometres, asking_price)

class Truck(Vehicle):
    def __init__(self, year, brand, model, kilometres, asking_price, axes):
        super().__init__(year, brand, model, kilometres, asking_price)