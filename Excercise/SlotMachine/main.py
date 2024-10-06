MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

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

def get_num_of_line():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1 - {MAX_LINE})"))
            if lines <= 1 or lines <= MAX_LINE:
                break
            else:
                print("Please enter a number between the given lines option")
        except ValueError as e:
            print('Kindly enter digits only.')
        
    return lines

def get_bet():
    while True:
        try:
            amt = int(input("ENTER THE BETTING AMOUNT"))
            if amt <= MIN_BET or amt  <= MAX_BET:
                break
            else:
                print("Please enter a number between the given lines option")
        except ValueError as e:
            print('Kindly enter digits only.')

def main():
    balance = deposit()
    lines = get_num_of_line()
    bet = get_bet()
    print(balance,lines)
main()