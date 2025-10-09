'''
POLYMORPHISM (multiple forms)

POLY is a core concept in oop that  allows objects of different classes to be treated as objects of a common superclass. it provides way to perform a single action in different forms. 

polymorphism is typically acheived through method overriding and interfaces

'''
# Method overriding
# Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class

# base class
class Animal:
    def speak(self):
        print('Sound of the animal')


# Derived class 1
class dog(Animal):
    def speak(self):
        print('woof')

# Derived class 2
class cat(Animal):
    def speak(self):
        print("Meoowww")


dogggy = dog()

dogggy.speak()

catty = cat()

catty.speak()


# polymorphism with functions and methods
# Base class

class shape:
    def area(self):
        return 'The area of the figure'

# derived class
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return f'The area of rectangle is {self.width * self.height}'

# derived class 2
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return f"The area of the circle is {3.14 * self.radius * self.radius}"

# function that demonstrates polymorphism 

def print_area(shape):
    print(f'The area is {shape.area()}')


rectangle = Rectangle(4,5)
circle = Circle(6)

print_area(rectangle)
print_area(circle)

'''
Polymorphism with abstract base class
abstract base class are used to define common methods for a group of related objects. They can enforce that derived classes implements particular methods, promoting consistency across different implementations

'''

from abc import ABC, abstractmethod

# define an abstract class

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# derived class 1
class Car(Vehicle):
    def start_engine(self):
        return 'Car engine started'
    
# derived class 2
class Bike:
    def start_engine(self):
        return 'Bike has been started'
    
toyota = Car()
hero = Bike()

print(toyota.start_engine())
print(hero.start_engine())


'''conclusion
it allows for flexibility and integration in code design. it enables a single function to handle objects of different classes, each with its own implementations of a method.
by understanding and applying polymorphism, you can create more entensible and maintainable object orientied programs
'''


