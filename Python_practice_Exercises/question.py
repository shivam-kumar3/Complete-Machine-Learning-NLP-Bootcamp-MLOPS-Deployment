'''
Exercise 1: Mailing Address
Create a program that displays your name and complete mailing address. 
The address should be printed in the format that is normally used in the area where you live. Your program does not need to read any input from the user.

'''

person1 = ['Shivam','Patna']

print(f'Name: {person1[0]}\nAddress {person1[1]}')

'''
Exercise 2: Hello

Write a program that asks the user to enter his or her name. The program should
respond with a message that says hello to the user, using his or her name


'''

def greeting():
    user = input("Enter your name:- ")
    print(f"Hello, {user}!\n Have a nice day ahead")


'''
Exercise 3: Area of a Room
Write a program that asks the user to enter the width and length of a room. Once these values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating-point numbers. Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.


'''

def Area_calculator():
    width = float(input("Enter the width of your room:- "))
    length = float(input("Enter the length of your room:- "))
    area = width * length

    print(f"The total area of your room is {area:.2f} square meters")




'''
Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

'''

def farmer_area():
    try:
        width = float(input("Enter the width of the field (in feet):- "))
        length = float(input("Enter the length of the field (in feet):- "))
        total_area = width * length
        total_acre = total_area / 43560  # 1 acre = 43,560 sq ft

        acre_word = "acre" if total_acre == 1 else "acres"  # Proper pluralization
        print(f"Hi user! \nYou have a total of {total_acre:.2f} {acre_word} of field.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")



'''
Exercise 5: Bottle Deposits
(Solved, 15 Lines)
In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and two digits to the right of the decimal point.

'''

# Get the number of containers from the user
small_containers = int(input("Enter the number of containers (1 liter or less): "))
large_containers = int(input("Enter the number of containers (more than 1 liter): "))

# Define deposit values
small_deposit = 0.10
large_deposit = 0.25

# Calculate the total refund
total_refund = (small_containers * small_deposit) + (large_containers * large_deposit)

# Display the result formatted to two decimal places
print(f"Total refund: ${total_refund:.2f}")

'''
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab

'''

import math

def main():
    # Read two integers from the user
    a = int(input("Enter the first integer (a): "))
    b = int(input("Enter the second integer (b): "))
    
    # Perform calculations
    sum_ab = a + b
    difference_ab = a - b
    product_ab = a * b
    quotient_ab = a / b if b != 0 else "Undefined (division by zero)"
    remainder_ab = a % b if b != 0 else "Undefined (modulo by zero)"
    log_a = math.log10(a) if a > 0 else "Undefined (logarithm of non-positive number)"
    power_ab = a ** b
    
    # Display results
    print(f"Sum: {sum_ab}")
    print(f"Difference: {difference_ab}")
    print(f"Product: {product_ab}")
    print(f"Quotient: {quotient_ab}")
    print(f"Remainder: {remainder_ab}")
    print(f"log10(a): {log_a}")
    print(f"a^b: {power_ab}")

if __name__ == "__main__":
    main()


'''
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.


'''


import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance

# User input
lat1 = float(input("Enter latitude of first point: "))
lon1 = float(input("Enter longitude of first point: "))
lat2 = float(input("Enter latitude of second point: "))
lon2 = float(input("Enter longitude of second point: "))

distance = haversine(lat1, lon1, lat2, lon2)
print(f"The distance between the points is {distance:.2f} km")


'''
Exercise 14: Height Units

Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.


'''

def height_to_cm(feet, inches):
    cm_per_inch = 2.54
    total_inches = feet * 12 + inches
    return total_inches * cm_per_inch

# User input
feet = int(input("Enter height in feet: "))
inches = int(input("Enter additional inches: "))

# Compute height in cm
height_cm = height_to_cm(feet, inches)

# Display result
print(f"Equivalent height: {height_cm:.2f} cm")

'''
Exercise 16: Area and Volume
(15 Lines)
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr2. The
volume of a sphere is computed using the formula volume = 4/3πr3.

'''
import math

# Read radius from user
r = float(input("Enter the radius: "))

# Compute area of the circle
area = math.pi * r**2

# Compute volume of the sphere
volume = (4/3) * math.pi * r**3

# Display results
print(f"Area of the circle: {area:.2f}")
print(f"Volume of the sphere: {volume:.2f}")


'''
Exercise 21: Area of a Triangle
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area =b × h /2
Write a program that allows the user to enter valuesforb andh. The program should
then compute and display the area of a triangle with base length b and height h.


'''
def calculate_triangle_area():
    length = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))

    area = (length * height) / 2

    print(f"The area of the triangle is {area:.2f}")

# Call the function
calculate_triangle_area()

'''
Exercise 24: Units of Time
(22 Lines)
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.

'''

def time_to_seconds(days, hours, minutes, seconds):
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

# Get user input
days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

# Compute total seconds
total_seconds = time_to_seconds(days, hours, minutes, seconds)

# Display result
print(f"Total duration in seconds: {total_seconds}")


'''
Exercise 28: Body Mass Index
(14 Lines)
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. 


'''

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Get user input
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Compute BMI
bmi = calculate_bmi(weight, height)

# Display result
print(f"Body Mass Index (BMI): {bmi:.2f}")



'''
Exercise 30: Celsius to Fahrenheit and Kelvin
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the Internet
'''

def temp():
    celsius = int(input("Enter the temp in celsius"))
    fah = celsius * (9/5) + 32
    kelvin = celsius + 273.15

    print(f'Fahrenheit {fah}\nKelvin {kelvin}')


temp()

'''
Exercise 38: Name That Shape
(Solved, 31 Lines)
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.



'''

# Get the number of sides from the user
num_sides = int(input("Enter the number of sides: "))

# Dictionary mapping number of sides to shape names
shapes = {
    3: "Triangle",
    4: "Quadrilateral",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon"
}

# Determine and display the shape name
if num_sides in shapes:
    print(f"A shape with {num_sides} sides is called a {shapes[num_sides]}.")
else:
    print("Error: Please enter a number between 3 and 10.")
'''

Exercise 41: Classifying Triangles
(Solved, 21 Lines)
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle’s type.

'''

# Get the lengths of the three sides from the user
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Check if the inputs can form a valid triangle
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")


'''
Exercise 58: Is It a Leap Year?
(Solved, 22 Lines)
Most years have 365 days. However, the time required for the Earth to orbit the Sun
is actually slightly more than that. As a result, an extra day, February 29, is included
in some years to correct for this difference. Such years are referred to as leap years.
The rules for determining whether or not a year is a leap year follow:
• Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year.
• Of the remaining years, any year that is divisible by 4 is a leap year.
• All other years are not leap years.
Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year.

'''

# Get user input
year = int(input("Enter a year: "))

# Check leap year conditions
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


'''
Exercise 59: Next Day
(50 Lines)
Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2019-11-18 then your program
should display a message indicating that the day immediately after 2019-11-18 is
2019-11-19. If the user enters values that represent 2019-11-30 then the program
should indicate that the next day is 2019-12-01. If the user enters values that represent
2019-12-31 then the program should indicate that the next day is 2020-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.


'''

def is_leap_year(year):
    """Returns True if the given year is a leap year, otherwise False."""
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def next_day(year, month, day):
    """Computes the next day's date."""
    # Days in each month (handle February separately for leap years)
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 
                     31, 31, 30, 31, 30, 31]
    
    # Move to the next day
    day += 1
    
    # If the day exceeds the month's days, reset day and move to the next month
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
    
    # If the month exceeds 12, reset month and move to the next year
    if month > 12:
        month = 1
        year += 1
    
    return year, month, day

# Get user input
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))

# Compute next day
new_year, new_month, new_day = next_day(year, month, day)

# Display result
print(f"The next day is {new_year}-{new_month:02d}-{new_day:02d}")

'''
Exercise 61: Is a License Plate Valid?
(Solved, 28 Lines)
In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three digits. When all of the license plates following that pattern had
been used, the format was changed to four digits followed by three uppercase letters.
Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate.


'''

import re

def validate_license_plate(plate):
    old_pattern = r'^[A-Z]{3}\d{3}$'  # Three letters followed by three digits
    new_pattern = r'^\d{4}[A-Z]{3}$'  # Four digits followed by three letters
    
    if re.fullmatch(old_pattern, plate):
        print("This is a valid older style license plate.")
    elif re.fullmatch(new_pattern, plate):
        print("This is a valid newer style license plate.")
    else:
        print("This is not a valid license plate format.")

# Get user input
plate = input("Enter a license plate: ").strip()
validate_license_plate(plate)


'''
Exercise 64: Discount Table
(18 Lines)
A particular retailer is having a 60 percent off sale on a variety of discontinued
products. The retailer would like to help its customers determine the reduced price
of the merchandise by having a printed discount table on the shelf that shows the
original prices and the prices after the discount has been applied. Write a program that
uses a loop to generate this table, showing the original price, the discount amount,
and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.

'''

original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount_rate = 0.60

print(f"{'Original Price':<15}{'Discount':<15}{'New Price':<15}")
print("-" * 45)

for price in original_prices:
    discount = price * discount_rate
    new_price = price - discount
    print(f"${price:<14.2f}${discount:<14.2f}${new_price:<14.2f}")


'''
xercise 66: No More Pennies
(Solved, 39 Lines)
February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
Mint. Now that pennies have been phased out retailers must adjust totals so that they
are multiples of 5 cents when they are paid for with cash (credit card and debit card
transactions continue to be charged to the penny). While retailers have some freedom
in how they do this, most choose to round to the closest nickel.
Write a program that reads prices from the user until a blank line is entered.
Display the total cost of all the entered items on one line, followed by the amount
due if the customer pays with cash on a second line. The amount due for a cash
payment should be rounded to the nearest nickel. One way to compute the cash
payment amount is to begin by determining how many pennies would be needed to
pay the total. Then compute the remainder when this number of pennies is divided
by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
the total up.


'''


import math

def round_to_nickel(amount):
    pennies = round(amount * 100)  # Convert to pennies
    remainder = pennies % 5
    
    if remainder < 2.5:
        rounded_pennies = pennies - remainder
    else:
        rounded_pennies = pennies + (5 - remainder)
    
    return rounded_pennies / 100  # Convert back to dollars

def main():
    total = 0.0
    while True:
        price = input("Enter item price (or blank to finish): ")
        if price == "":
            break
        try:
            total += float(price)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"Total cost: ${total:.2f}")
    cash_total = round_to_nickel(total)
    print(f"Cash payment amount: ${cash_total:.2f}")

if __name__ == "__main__":
    main()


'''
Exercise 72: Fizz-Buzz
(17 Lines)
Fizz-Buzz is a game that is sometimes played by children to help them learn about
division. The players are commonly arranged in a circle so that the game can progress
from player to player continually. The starting player begins by saying one, and then
play passes to the player to the left. Each subsequent player is responsible for the
next integer in sequence before play passes to the following player. On a player’s
turn they must either say their number or one of following substitutions:
• If the player’s number is divisible by 3 then the player says fizz instead of their
number.
• If the player’s number is divisible by 5 then the player says buzz instead of their
number.
A player must say both fizz and buzz for numbers that are divisible by both 3
and 5. Any player that fails to perform the correct substitution or hesitates before
answering is eliminated from the game. The last player remaining is the winner.
Write a program that displays the answers for the first 100 numbers in the FizzBuzz game. Each answer should be displayed on its own line


'''

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizz_buzz()
