name = 'Shivam'
age = 20

print(name.upper())
print(type(age))

class Dog:
    def bark(self):
        print('Whoof whoof')


dog1 = Dog()

dog1.bark()


class Doggy:
    def __init__(self,name,breed,age):
        self.name = name 
        self.breed = breed
        self.age = age

    def Name(self):
        print(self.name)

    def breed(self):
        
    
    def age(self):
        print(self.age)


doggy = Doggy('Tobby','Labrador',9)

doggy.Name()
doggy.age()