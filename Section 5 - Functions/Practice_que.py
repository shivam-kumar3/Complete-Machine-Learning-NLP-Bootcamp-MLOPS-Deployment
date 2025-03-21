# Write a function to calculate and return the sq of a number

def Square(n):
    return n ** 2


print(Square(2))

# Create a function that takes two numbers as parameters and returns their sum

def Sum(a,b):
    return a + b


print(Sum(54,33))


# write a function multiply that multiplies two numbers but can also accept and multiply strings

def Multiply(a,b):
    return a * b


print(Multiply("a",9))


# create a function that return both the area and circumference of a circle given its radius 

def Area_stats(radius):
    area = 3.14 * radius ##2
    circum = 2 * 3.14 * radius

    return f"Area of the Circle is : {area},\nCircumference of the Circle is : {circum}"


print(Area_stats(2))


# write a function that greets a user. if no name is provided, it should greet with default name


def Greet(name = "User"):
    return f"Good Morning, {name}"


print(Greet("Shivam"))


# create a lambda function to compute the cube of a number

cube = lambda a : a**3

print(cube(2))


# *agrs - write a function that takes variable number of arguments and return their sum 

def SumAll(*args):
    return sum(args)


print(SumAll(1,2,3,4,5,6,7,7,42))


def greet():
    print("Hello")
    greet()


 