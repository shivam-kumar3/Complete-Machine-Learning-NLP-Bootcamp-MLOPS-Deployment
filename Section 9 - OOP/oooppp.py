# 1st approach - Impretive approach
a = 6
b =  19

print(a+b)

#2nd approach - Functional approach

def add (a,b):
    print(a+b)

add(3,2)


# OOP  is a programming paradigm based on the concept of objects which can contain data attributes and code(methods)

class Addition:
    def __init__(self,a,b):
        print(a+b)

obj = Addition(12,34)
obj



class Factory:
    a = 14

    def welcome(self):
        print('Hello how are you')

    print('I am getting initialized')


print(Factory().a)