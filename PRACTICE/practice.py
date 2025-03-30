'''
Excercise 1
Find the minimum if 3 given number

'''

def minimum(a,b,c):
    if a > b and a > c:
        print(f'{a} is the biggest amoung all')
    elif b > a and b > c:
        print(f"{b} is the bigggest amoung all")
    else:
        print(f"{c} is the biggest among all")

minimum(50,2,1)

'''
Excercise 2
ATM machine menu

1.Pin change
2. Balance check
3. Withdraw
4. Deposit
5. Exit

'''

def ATM():
    pin = ''
    balance = 0
    withdraw = 0 
    deposit = 0
    print("WELCOME TO THE ATM")
    while True:
        menu = int(input('''\nSelect your choice
                1. Pin change
                2. Balance check
                3. Withdraw
                4. Deposit
                5. Exit        
            '''))
        if menu == 1:
            new_pin = int(input("Enter your new pin"))
            pin = new_pin
            print("Your pin has been changed")
        elif menu == 2:
            print(f'Your current balance is {balance}')
        elif menu == 3:
            amt = int(input("Enter the amount"))
            if amt > balance:
                print("You dont have a sufficient balance")
            else:
                print(f"{amt} is withdrawed from your account")
                balance -= amt
        elif menu == 4:
            amtt = int(input("Enter the amt"))
            print(f'{amtt} is depositted in your account')
            balance += amtt
        elif menu == 5:
            print("Thankyou for the visit")
            break
        else:
            print("Enter the choice from the options only")



transactions = [
    {"customer_id": 1, "item": "apple", "amount": 5},
    {"customer_id": 2, "item": "banana", "amount": 3},
    {"customer_id": 1, "item": "orange", "amount": 7},
    {"customer_id": 3, "item": "apple", "amount": 5},
    {"customer_id": 2, "item": "orange", "amount": 2},
    {"customer_id": 3, "item": "banana", "amount": 6},
]

for i in transactions:
    for keys, values in i.items():
        print(keys,values)



def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))



def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



# atm machine opp que

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
            return True
        else:
            print("Invalid deposit amount")
            return False

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return False
        elif amount <= 0:
            print("Invalid withdrawal amount")
            return False
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            return True

    def get_balance(self):
        return self.balance

class ATM:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts by account number

    def create_account(self, account_number, pin, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists")
        else:
            account = Account(account_number, pin, initial_balance)
            self.accounts[account_number] = account
            print("Account created successfully")

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        else:
            print("Authentication failed")
            return None

    def deposit(self, account, amount):
        return account.deposit(amount)

    def withdraw(self, account, amount):
        return account.withdraw(amount)

    def check_balance(self, account):
        return account.get_balance()

# Main script to simulate an ATM interaction
atm = ATM()

# Create a new account
atm.create_account("12345", "6789", 1000)  # account_number, pin, initial_balance

# Authenticate and perform operations
account = atm.authenticate("12345", "6789")
if account:
    print(f"Current Balance: {atm.check_balance(account)}")
    
    # Deposit
    atm.deposit(account, 500)
    print(f"Balance after deposit: {atm.check_balance(account)}")
    
    # Withdraw
    atm.withdraw(account, 300)
    print(f"Balance after withdrawal: {atm.check_balance(account)}")



# currency converstor programme 

def Currency_convertor():
    amt = int(input('Enter the amount:- '))
    choice = int(input('In which currency You want to convert into \n1- Doller\n2- INR\n'))

    if choice == 1:
        print(f'The total amt in doller is ${amt * 0.012}')
    elif choice == 2:
        print(f'The total amount in INR is {amt * 84.48}')


'''
write a python program that takes two int inputs from the user and prints their sum



'''
def sum(num1,num2):
    print(num1+num2)

sum(324,342)

'''
Extract a product name from a website URL  

URL -https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1

'''

url = 'https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'


name = url[22:44]
name = name.replace('-',' ')
print(name)


'''
simple authetication system for a secure faciltiy 
the system needs to verify the user's pin
they have a valid access code ie 4 digit numerical code 
or 
they are a member of the access list , which contains the following members [69,420,666,1337]

write a python program that prompts the user to enter their access code and  check whether they have access to the facility
display a message indicating whether access is granted or denied

'''

def access():
    print("Welcome to the world bank")
    members = [69,420,666,1337]
    user_pin = int(input("Enter your pin for the access:- "))

    if user_pin in members:
        print("Access Granted\nWelcome to world bank services")
    else:
        print("Access Denied")


'''
Create a python programme for generating a grocery list based on dietary preferencecs and given budget.


'''

def Grocery():
    pref = int(input("1- Vegetarian\n2- Non Vegetarian\n"))
    budget = int(input("Enter Your budget for the shopping\n"))
    cart = []

    if pref == 1:
        if budget >= 15:
            cart.extend(['Broccoli', 'Carrots', 'Bell Peppers', 'Tofu'])
        elif budget >= 10:
            cart.extend(['Broccoli', 'Carrots'])
        elif budget >= 5:
            cart.append('Broccoli')
    elif pref == 2:
        if budget >= 25:
            cart.extend(['Broccoli', 'Carrots', 'Bell Peppers', 'Chicken Breast', 'Eggs'])
        elif budget >= 20:
            cart.extend(['Broccoli', 'Carrots', 'Bell Peppers', 'Chicken Breast'])
        elif budget >= 15:
            cart.extend(['Broccoli', 'Carrots', 'Bell Peppers'])
        elif budget >= 10:
            cart.extend(['Broccoli', 'Carrots'])
        elif budget >= 5:
            cart.append('Broccoli')
    else:
        print("No products added due to preferences or budget constraints.")

    print(f'You have these products in your cart:\n{cart}')





'''
we have a list of names , we want to print the list of all names that have r/R in them.

'''

names = ['shirvam', 'rohan','radhRe','Ramesh', 'shahi']
names_with_r = []
for i in names:
    if 'R' in i or 'r' in i:
        names_with_r.append(i)
print(names_with_r)

# solve the above problem with list comprehension

name_r = [i for i in names if 'r' in i]
print(name_r)


'''
Exercise 115: List of Proper Divisors
(36 Lines)
A proper divisor of a positive integer, n, is a positive integer less than n which divides
evenly into n. Write a function that computes all of the proper divisors of a positive
integer. The integer will be passed to the function as its only parameter. The function
will return a list containing all of the proper divisors as its only result. Complete
this exercise by writing a main program that demonstrates the function by reading
a value from the user and displaying the list of its proper divisors. Ensure that your
main program only runs when your solution has not been imported into another file.

'''


def proper_divisors(n):
    """Return a list of all proper divisors of n."""
    return [i for i in range(1, n) if n % i == 0]


def main():
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer.")
        return
    
    divisors = proper_divisors(num)
    print(f"Proper divisors of {num}: {divisors}")


if __name__ == "__main__":
    main()


'''

Exercise 119: Below and Above Average
(44 Lines)
Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.
'''

def classify_numbers():
    numbers = []
    
    # Read numbers from the user
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if not numbers:
        print("No numbers were entered.")
        return
    
    # Calculate the average
    average = sum(numbers) / len(numbers)
    print(f"\nAverage: {average:.2f}\n")
    
    # Classify numbers
    below_avg = [num for num in numbers if num < average]
    equal_avg = [num for num in numbers if num == average]
    above_avg = [num for num in numbers if num > average]
    
    # Display results
    print("Below average values:", below_avg if below_avg else "None")
    print("Equal to average values:", equal_avg if equal_avg else "None")
    print("Above average values:", above_avg if above_avg else "None")

classify_numbers()

'''
Exercise 121: Random Lottery Numbers
(Solved, 28 Lines)
In order to win the top prize in a particular lottery, one must match all 6 numbers
on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
organizer. Write a program that generates a random selection of 6 numbers for a
lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
Display the numbers in ascending order.

'''

import random

def generate_lottery_numbers():
    numbers = random.sample(range(1, 50), 6)  # Generate 6 unique numbers
    numbers.sort()  # Sort in ascending order
    return numbers

lottery_numbers = generate_lottery_numbers()
print("Your lottery numbers are:", lottery_numbers)

'''
Exercise 136: Reverse Lookup
(Solved, 45 Lines)
Write a function named reverseLookup that finds all of the keys in a dictionary
that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program.
'''

def reverseLookup(d, value):
    """Finds all keys in the dictionary that map to a specific value."""
    return [key for key, val in d.items() if val == value]

def main():
    # Example dictionary
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3,
        'e': 2
    }
    
    # Test cases
    print("Keys mapping to 1:", reverseLookup(sample_dict, 1))  # Should return ['a', 'c']
    print("Keys mapping to 2:", reverseLookup(sample_dict, 2))  # Should return ['b', 'e']
    print("Keys mapping to 3:", reverseLookup(sample_dict, 3))  # Should return ['d']
    print("Keys mapping to 4:", reverseLookup(sample_dict, 4))  # Should return []

main()

'''
Exercise 141: Write out Numbers in English
(65 Lines)
While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors. The amount being
paid normally appears on a cheque twice, with one occurrence written using digits,
and the other occurrence written using English words. Repeating the amount in two
different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.
In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that
number. For example, if the parameter to the function is 142 then your function should
return “one hundred forty two”. Use one or more dictionaries to implement
your solution rather than large if/elif/else constructs. Include a main program that
reads an integer from the user and displays its value in English words.

'''

def number_to_words(n):
    """Converts an integer (0-999) to its English words representation."""
    if not (0 <= n <= 999):
        return "Number out of range"
    
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    else:
        return ones[n // 100] + " hundred" + (" " + number_to_words(n % 100) if n % 100 != 0 else "")

def main():
    num = int(input("Enter a number (0-999): "))
    print("In words:", number_to_words(num))

main()