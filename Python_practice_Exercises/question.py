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