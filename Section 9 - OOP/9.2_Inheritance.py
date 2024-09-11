'''
inheritance is a fundamental concept in OOP that allows a class to inherit attributes and methods from another class
this lesson covers single inheritance and multiple inheritance 
demonstrating how to create and use them in python

'''

class Car:
    def __init__(self,windows,doors,enginetpye):
        self.windows = windows
        self.doors = doors
        self.enginetypes = enginetpye
    def drive(self):
        print("The car is ready to drive")
    
car1 = Car(4,4,'Petrol')

car1.drive()