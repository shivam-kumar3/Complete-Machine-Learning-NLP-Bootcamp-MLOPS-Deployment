'''
The filter function contructs an iterator from elements of an iterable for which a function return true. it is used to filter out items from a list (or any other iterable) based on a condition 

'''

number = [1,2,3,4,5,6,7,8,9,10]

def even(num):
    return num % 2==0

evenn = list(filter(even,number))
print(evenn)