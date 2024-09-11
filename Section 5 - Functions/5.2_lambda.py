'''
Lambda functions in python

lambda functions are small anonymous functions defined using the lambda keyword. they can have any numbers of arguments but only one expression. they are commonly used for short operations or as arguments to higher order functions.

syntax
lambda arguments : expression

'''

def addition(a,b):
    print(a+b)

addition(543,34)

add = lambda a,b : a+b

print(add(234,423))

even = lambda x: x%2==0

print(even(21))

