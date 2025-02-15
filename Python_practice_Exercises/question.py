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

farmer_area()


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
