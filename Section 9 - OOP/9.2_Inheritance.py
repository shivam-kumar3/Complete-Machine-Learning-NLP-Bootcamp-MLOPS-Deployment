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

class Tesla(Car):
    def __init__(self,windows,doors,enginetype,EV):
        super().__init__(windows,doors,enginetype)
        self.ev = EV

    def selfDriving(self):
        print(f'This is the {self.ev} car')

# Multiple Inheritance 
# when a class inherits from more than one base class

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speak Now")

class Bird(Animal):
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type

    def eating(self):
        print("they are eating")

class All(Bird):
    def __init__(self,name,type,age):
        super().__init__(name,type)
        self.age = age
    
    def showAge(self):
        print(f"The {self.name} is {self.age} years old")
    
new = All('tobby','Dog',9)

print(new.name)
print(new.age)
new.eating()
new.showAge()
new.speak()

