menu = {
    'Coffee' : 120,
    "Sandwich" :70,
    'Pasta' : 100,
    "Pizza" : 150,
    "Burger" : 80,
}

def MyPlace():
    print('''Welcome to MyPlace Cafe\nPlease Order Your Meal
                Coffee      : 120
                Sandwich    : 70
                Pasta       : 100
                Pizza       : 150
                Burger      : 80

          ''')
    total_price =0
    item1 = input("Enter the food name ")
    if item1 in menu:
        total_price  += menu[item1]
        print(f'You ordered {item1}\nYour total price is {total_price} ')
    else:
        print("Sorry! This item is not available, Kindly order from the given Menu")

    another_item = input("Do you want to add another item? ").lower()
    if another_item == 'yes':
        item2 = input("Enter the food name ")
        if item2 in menu:
            total_price += menu[item2]
        else:
            print("Sorry! This item is not available, Kindly order from the given Menu")
    print(f'Your total bill is {total_price}\n Thankyou for Visitng ')

MyPlace()