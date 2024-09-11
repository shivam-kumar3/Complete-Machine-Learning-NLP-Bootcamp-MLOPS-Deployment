'''
Class and objects 

OOP is a programming paradigm that uses objects to design applications and computer programme.
oop allows for modeling real world scenarios using classes and objects.
this lesson covers the basics of creating classes and objects, including instance variables and methods

object = variables for calling
methods = function
attributes = variables inside the class

'''
# A class is a blue print for creating objects, attributes and methods

class Car:
    pass

audi = Car()

bmw = Car()

print(audi)
print(bmw)

audi.window = 6

print(audi.window)


tata = Car()
tata.doors = 4

print(tata.doors)

print(dir(tata))


# instance variable and methods 

class Dog:
    # constructor 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} is barking')
    def sleeping(self):
        print(f'{self.name} is sleeping right now')
    def playing(self):
        print(f'{self.name} is playing right now')


tobby = Dog('Tobby',9)

print(tobby.name)
print(tobby.age)
tobby.bark()
tobby.playing()
tobby.sleeping()

# modelling a bank account

class Bank:
    def __init__(self,accno,balance):
        self.accno = accno
        self.balance = balance
    def deposit(self,amt):
        self.balance += amt
        print(f'Your current balance is {self.balance}')
    def withdraw(self,amt):
        self.balance -= amt
        print(f'Your current balance is {self.balance}')
    def balance_check(self):
        print(f'You current balance is {self.balance}')



person  = Bank(1234,23121)
print(person.accno)
person.deposit(12000)
person.withdraw(8799)
person.withdraw(21)
person.balance_check()