'''
Video Outline:
1- Introduction to dictionaries
2- Creating Dict
3- Accessing dict elements
4- Modifying dictionary elements
5- dict methods
6- iterating over dictt
7- nested dict
8- dict comprehensions
9- practical examples and common errors

'''

# dict are unordered collection of items. they store data in key:values pairs.keys must be unique and immutable 

empt_dict = {}
print(type(empt_dict))

students = {"Name":"Shivam","Age": 28,"Grade":"A"}

print(students)

# accessing dict elements 
print(students["Name"])
print(students["Age"])
print(students.get("Grade"))
print(students.get("last name","NAN"))


# modifying dict elements
# dicts are mutable, so we can add, update or delete elements

print(students)

students['lastname'] = "shahi"

print(students)

del students['lastname']

print(students)

# dict methods

keys = students.keys()

print(keys)

values = students.values()
print(values)

items =students.items()

print(items)


# shallow copy

student_new = students.copy()

print(students)
print(student_new)


students['Name'] = "Brand"

print(students)
print(student_new)

# iterating over dict

for keys,values in students.items():
    print(keys,values)

for keys in students.keys():
    print(keys)

for values in students.values():
    print(values)

