def deposit():
    while True:
        try:
            amt = int(input("What would you like to deposit? "))
            if amt > 0:
                break  # Break if a valid amount is entered
            else:
                print("Amount must be greater than 0")
        except ValueError as e:
            print('Kindly enter digits only.')
    return amt



def main():
    balance = deposit()

main()