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
