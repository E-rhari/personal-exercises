# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:18:58 2023

@author: Evandro Rhari
"""


# Base copiada do livro Curso Intensivo de Python, de Eric Matthes
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
        
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + + self.make + " " + self.model
        return long_name.title()
    
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")
        
    
    def  update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles



class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")
        
        
    def get_range(self):
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270
            
        message = "This car can go approximadetely " + str(car_range)
        message += " miles on a full charge"
        print(message)
        
        
    def upgrade_battery(self):
        if self.battery_size <85:
            print("Your battery is upgraded from " + str(self.battery_size) + 
                  " to 85-kWh") 
            self.battery_size = 85
        else:
            print("Your battery is more powerful than we can get it")
        


class ELetricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
        
car = ELetricCar("tesla", "model s", 2016)
car.battery.get_range()

car.battery.upgrade_battery()
car.battery.get_range()