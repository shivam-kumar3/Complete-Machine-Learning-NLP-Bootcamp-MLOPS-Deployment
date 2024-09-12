'''
Encapsulation

Encapsulation involes bundling data and methods that operate on the data within a single unit.

Encapsulation is the concepts of wrapping data(variable) and methods(function) together as a single unit. it restricts direct access to some of the objects components, which is a mean of preventing accidental interference misuse of the data
'''

# getter and setter methods
# access variable - PUBLIC, PROTECTED AND PRIVATE VARIABLE

class Person:
    def __init__(self,name,age):
        self.name = name #public variable
        self.age = age  #public variables

def get_name(person):
    return person.name


person = Person("shivam",29)

print(person.age)
print(person.name)

(get_name(person))

# private varaible
class Person:
    def __init__(self,name,age):
        self.__name = name #Private variable
        self.__age = age  #Private variables

def get_name(person):
    return person.__name

person1 = Person('Shivam',28)

# print(person1.__name)

# private variable cannot be used outside the class
# protected variable cannot be used outside the class but we can access it with derived class



# Encapsulation with gatter and setter

class Person:
    def __init__(self,name,age):
        self.__name = name #private access modifier or variable
        self.__age  = age #private variable

    # getter method for name
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    #setter method for name
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")
        
person = Person('Shivam', 29)

# access and modify private variable using getter and setter

print(person.get_name())
print(person.get_age())

person.set_age(43)
print(person.get_age())

person.set_age(-23)

print(person.get_age())