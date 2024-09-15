'''
Magic methods 

Magic mathods in python, also knows as dunder methods (double underscore methods) are special methods that start and end with double underscores. 
these methods enable you to define the behaviour of objects for build in operation such as arithmetic operations, comparisons and more 


magic methods

magic methods are predefined functions in python that you can override to change the behaviour of your objects. 

some common  magic methods includes

__init__ : initialize a new instance of a class
__str__ : Return a string representation of an object
__repr__ : return an official stringg representation of an object

'''
# basic methods
class Person:
    def __init__ (self,name,age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} years old'
    def __repr__(self):
        return f'Person name : {self.name}, Age = {self.age}'
    
    
person = Person("Shivam",29)

print(person)
print(repr(person))
