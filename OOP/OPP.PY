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
    def __init__(self,name,breed,age,owner):
        self.name = name 
        self.breed = breed
        self.age = age
        self.owner = owner

    def Name(self):
        print(f'Dog Name : {self.name}')

    def Breed(self):
        print(f'Dog Breed: {self.breed}')
    
    def Age(self):
        print(f'Dog Age {self.age}')

    def Show_owner(self):
        print(f'Owner Details {self.owner}')


class Owner:
    def __init__(self,name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner_1= Owner('Shivam','Patna',8808886844)

doggy = Doggy('Tobby','Labrador',9,owner_1)

doggy.Name()
doggy.Age()
doggy.Breed()
doggy.Show_owner()