'''
sets are unordered
set dont allow duplicate values
sets are useful for membership test, eliminating duplicate entries and performing mathematical set operation like union, intersection, difference and symmetric difference
'''

lst = [1,2,3,4,4,4,5,6,67,67,65,65]


setted = set(lst)
print(setted)


# clear all the elements
setted.clear()
print(setted)


# set membership test

my_set = {1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)

# mathematical operations


