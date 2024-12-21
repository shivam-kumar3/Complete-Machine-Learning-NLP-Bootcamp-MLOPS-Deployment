'''
Write a python program which will keep adding a stream of numbers given by the user
the adding stops as soon as user presses q key on the keyboard

'''

def Kirana_calculator():
    print('Welcome to the store\nWhat would you like to add in the cart')

    sum = 0
    while True:
        enter_price = input("Enter the price of the product:-\n")
        
        if enter_price == 'q':
            break
        else:
            sum += int(enter_price)
    print(f"The total price of your cart is ₹{sum} ")
    print("Thankyou for shopping with us\n See you again")



Kirana_calculator()


'''
That was pretty easy project
'''
