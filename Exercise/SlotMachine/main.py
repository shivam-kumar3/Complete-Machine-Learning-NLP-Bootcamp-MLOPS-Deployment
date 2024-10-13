import random
MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    'A' : 2,
    "B" : 4,
    'C' : 6,
    'D' : 8,
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    COLUMNS = [[],[],[]]

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
            lines = int(input(f"Enter the number of lines to bet on (1 - {MAX_LINE}):- "))
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
            amt = int(input("ENTER THE BETTING AMOUNT FOR EACH LINE:- "))
            if amt <= MIN_BET or amt  <= MAX_BET:
                break
            else:
                print("Please enter a number between the given lines option")
        except ValueError as e:
            print('Kindly enter digits only.')

    return amt

def main():
    balance = deposit()
    lines = get_num_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount\nYour current balance is {balance} ")
        else:
            break

    print(f'YOU ARE BETTING ${bet} ON {lines} lines. \nTOTAL BET IS EQUAL TO ${total_bet}')



main()

