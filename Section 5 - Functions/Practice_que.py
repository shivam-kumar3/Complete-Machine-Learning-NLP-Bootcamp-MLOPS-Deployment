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

    return ("Area of the Circle is :" ,area, "Circumference of the Circle is ", circum)


print(Area_stats(2))