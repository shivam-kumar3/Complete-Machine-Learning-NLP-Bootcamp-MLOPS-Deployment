'''
Operator overloading 

Operator overloading allows you to define the behavior of operators (+,-,* etc) for custom objects.
You achieve this by overriding specific magic methods in your class
'''

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x +other.x , self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x , self.y - other.y)
    def __mul__(self,other):
        return Vector(self.x * other.x , self.y * self.y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
# creating objects of the vector clas

v1 = Vector(2,3) # this will be self object 
v2 = Vector(4,5) # this will consider as other object

print(v1+v2)
print(v1-v2)
print(v1*v2)