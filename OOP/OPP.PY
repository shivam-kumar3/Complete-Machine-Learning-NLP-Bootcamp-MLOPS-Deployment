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
        print(f'Owner Details : {self.owner}')


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
print(doggy.owner.name)


'''
Lets make a email id organizer with private attributes

'''

from datetime import datetime
class User:
    def __init__(self,username,email,password):
        self.username = username
        self.__email = email
        self.__password = password


    def clean_email(self):
        return self.email.lower().strip()

    def get_email(self):
        print(f'Email accessed at {datetime.now()}')
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email


user1 = User('Shivam','SHivamKumar@gmail.com','1243')

print(user1.username)
print(user1.get_email())

user1.set_email("shivamm.py@gmail.com")

print(user1.get_email())



# python "Consenting Adults" in philosophy

