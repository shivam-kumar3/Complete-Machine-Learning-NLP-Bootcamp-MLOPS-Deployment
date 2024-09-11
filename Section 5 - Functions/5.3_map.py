# mapping - applies a function to all items in a list
# map() function applies a given function to all items in an input list (or any other iteerable) and return a map object (an iterator)
# this is particularly useful for transforming data in a list comprehensively 
num = [1,2,3,4,5,6]


def square(list):
    for i in list:
        print(i**2, end = " ")


square(num)

# lambda function

new = list(map(lambda x: x*x,num))
print(new)


# map multiple iterable 

num1= [1,2,3]
num2 = [4,5,6]

neww = list(map(lambda x,y:x+y,num1,num2))
print(neww)

# map to convert a list of string to int

strr= ["1","2","3","4"]

strr2 = list(map(int,strr))

print(strr2)

strr3 = list(map(str,strr2))

print(strr3)

fruits = ["apple","banana","cherry"]

fruit_new = list(map(str.upper,fruits))

print(fruit_new)

people = [
        {"name" : "shivam","age":28,"country":'india'},
        {"name" : "shahi","age":34,"country":'india'},
        {"name" : "raju","age":65,"country":'india'}
]

def get_name(person):
    return person['name'].upper()

yo = list(map(get_name,people))
print(yo)

