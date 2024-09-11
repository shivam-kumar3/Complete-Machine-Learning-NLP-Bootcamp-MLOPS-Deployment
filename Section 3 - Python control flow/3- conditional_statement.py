'''
1- Introduction to conditional statements
2- if statements
3- else statements
4- elif statements
5- nested conditional statements
6- practical examples
7- common errors and best practices


'''

# if statements
age = 20 

if age >= 20:
    print("Age is greater then 20")


# else statements
#  the else statement executes a block of code if the condition in the if statement is false


age = 19

if age >= 20:
    print("Age is greater then 20")
else:
    print("Age is less then 20")


# elif 
#  the elif statement allows you to check multiple conditions. it stands for "else if"

age = 30

if age < 13:
    print("you are a child")
elif age <18:
    print("You are a teenager")
else:
    print("You are an adult")


# nested conditional statements
# we can place one or more if, elif, or else statement inside another if, elif, else statements

num = int(input("Enter the number:- "))

if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("the number is even")
    else:
        print(f"The number {num} is odd")
else:
    print("The number is 0 or negative")

# PRACTICAL EXAMPLES 
# Determine if a year is a leap year using nested conditional statement

year = int(input("Enter a year:- "))

if year % 4 == 0 and year % 400 == 0:
    if year % 400 == 0:
        if year % 100 == 0:
            print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not leap year")

# assigments
#  simple calculator program


def calculator():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))

    operation = input("choose your operation to perform\n+ , - , *, /")

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1/num2)
    else:
        print("Invalid operator \nChoose the operator from the given list")

calculator()


# Determine the ticket price based on age and whether the person is a student or not

def Ticketprice():
    age = int(input("Enter your age"))
    is_student = input("Are you a student?").lower()
    ticket_price = 0
    if age < 10:
        ticket_price = 0
        print("The ticket is free for the under 10 child")
    elif age < 15 and is_student == "yes":
        ticket_price += 100
        ticket_price -= 50
        print(f"The price for {age} years old child is {ticket_price}")
    elif age < 18 and is_student == "yes":
        ticket_price += 200
        ticket_price -= 50
        print(f"The price for {age} years old person is {ticket_price}")
    elif age >= 18 and is_student == "yes":
        ticket_price += 300
        ticket_price -= 50
        print(f"The price for {age} years old person is {ticket_price}")
    elif age >= 30 and is_student == "yes":
        ticket_price += 500
        ticket_price -= 50
        print(f"The price for {age} years old person is {ticket_price}")

Ticketprice()
    

