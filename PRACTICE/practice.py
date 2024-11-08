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