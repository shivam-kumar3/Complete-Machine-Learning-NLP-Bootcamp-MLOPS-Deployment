word_dict = {"Intelligent": "Hoshiyaar",
             "Poor" : "Gareeb",
             "Rich" : "Ameer",
             "Age" : 4
            }

print(word_dict.get((1,2,3)))

'''
Exercise 101: Random License Plate
(45 Lines)
In a particular jurisdiction, older license plates consist of three letters followed by
three digits. When all of the license plates following that pattern had been used, the
format was changed to four digits followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.

'''

import random
import string

# Function to generate old format license plate (3 letters followed by 3 digits)
def generate_old_license_plate():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits = ''.join(random.choices(string.digits, k=3))
    return letters + digits

# Function to generate new format license plate (4 digits followed by 3 letters)
def generate_new_license_plate():
    digits = ''.join(random.choices(string.digits, k=4))
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    return digits + letters

# Function to generate a random license plate
def generate_random_license_plate():
    # Randomly decide whether to generate an old or new format license plate
    if random.choice([True, False]):
        return generate_old_license_plate()
    else:
        return generate_new_license_plate()

# Main program
if __name__ == "__main__":
    license_plate = generate_random_license_plate()
    print(f"Random License Plate: {license_plate}")


'''
Exercise 102: Check a Password
(Solved, 40 Lines)
In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters long
and contains at least one uppercase letter, at least one lowercase letter, and at least
one number. Your function should return True if the password passed to it as its
only parameter is good. Otherwise it should return False. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure
that your main program only runs when your solution has not been imported into
another file.

'''

import string

# Function to check if a password is good
def is_good_password(password):
    if len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit

# Main program
if __name__ == "__main__":
    password = input("Enter a password: ")
    if is_good_password(password):
        print("Your password is good.")
    else:
        print("Your password is not strong enough.")
