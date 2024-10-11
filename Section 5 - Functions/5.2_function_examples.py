# tempreture conversion

def tempreture():
    temp = float(input("Enter your tempreture:- "))
    choice = int(input("in what unit u want to convert\n1-Calcius\n2-Fahrenheit"))

    if choice == 1:
        ans = round(temp-32*(5/9),2)
        print(f"The converted value is {ans}")

    elif choice == 2:
        ans = (temp *9/5)+32
        print(f"The converted value is {ans}")

    else:
        print("Enter the right choice")

# password strength checker 


def is_strong_password(password):
    '''This function check if the password is strong or not '''
    if len(password) < 8:
        print("Sorry password is not strong")

    if not any(i.isdigit () for i in password):
        print("Your password is weak because it doesnot have any digit")

    if not any(i.islower() for i in password):
        print("All the character is lower\nYou should include some upper letter for a strong password")
    if not  any(i.isupper() for i in password):
        print("All the letters are upper case")

    if not any(i in "!@#$%^&*()" for i in password):
        print("Your password dont have any special character")
    else:
        print("You have a strong password")

is_strong_password("Shivam2shahi@#")



# calculate the total cost of items in shopping cart
cart = [
    {"name":"Apple","Price":0.5, "Quantity": 4},
    {"name":"Orange","Price":1.5, "Quantity": 6},
    {"name":"Banana","Price":0.7, "Quantity": 8}
]


def calculate_total_cost(cart):
    total_cost = 0 
    for item in cart:
        total_cost = item["Price"] * item["Quantity"]
    print(f"The Billing amount is {total_cost}")


calculate_total_cost(cart)


# for item in cart:
#     print(item["name"],item["Price"]*item["Quantity"])

# check if a sting is palindrome

def is_palindrome(string):
    '''This function check if the string is palindrome or not'''
    if string == string[::-1]:
        print("The string is palindrome")
    else:
        print("The word is not palindrome")

is_palindrome('nmo')


# calculate the factorials of a number using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))


#  a function to read a file and count the frequenct of each word
