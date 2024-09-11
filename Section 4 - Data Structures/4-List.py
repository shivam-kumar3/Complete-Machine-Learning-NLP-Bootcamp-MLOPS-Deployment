'''
Introduction to lists
list are ordered, mutable collection of items
they can contain items of different data types

'''

'''
Video Outline:
1- Introduction of list
2- Creating list
3- Accessing list elements
4- Modifying list elements
5- List methods
6- Slicing lists
7- Iterating over lists
8- List comprehensions
9- Nested list
10 - Practice questions


'''
lst = []

print(type(lst))

name = ["shivam", 423,342.4,True]

print(name)

# accessing list elements

fruits = ['Apple', "Banana", "Cherry", 'kiwi', "gauva"]

print(fruits[-1])

# add the new value into specific index
fruits.insert(0,"Watermelon")

print(fruits)


# add the value at the end of the list
fruits.append("Orange")
print(fruits)

# remove and return the last item
fruits.pop()
print(fruits)

# print the index of the value
print(fruits.index('Banana'))

# sorting the list
print(fruits.sort())

fruits.remove("Watermelon")

print(fruits)


# slicing the list 

num = [1,2,3,4,5,6,7,8]
print(num[2:5])
print(num[:5])
print(num[5:])
print(num[::2])
print(num[::-1])
print(num[::-2])


# iterating over list

for i in num:
    print(i)

# iterating over list with index using enumerate function

for index, numbers in enumerate(num):
    print(index,numbers)

# list comprehension
# basic Syntax [expresion for item in iterable]

lst = []
for x in range(10):
    lst.append(x**2)
print(lst)

lst2 = [x**2 for x in range(10)]

print(lst2)


# basic list comprehension 
# sqaure of all the numbers

sqaure = [x**2 for x in range (20)]
print(sqaure)

# list comprehension with condition 
lstt = []
for i in range (10):
    if i % 2 == 0:
        lstt.append(i)
print(lstt)

# using list comprehension

even = [i for i in range(10) if i%2 == 0]

print(even)

# Nested list comprehension
# [expression for item1 in iterable1 for item2 in iterable2]

lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']

pair = [[i,j] for i in lst1 for j in lst2]

print(pair)

# list comprehension with function call
words = ["Python","World","hello", "list","Comprehension"]
length = [len(word) for word in words]
print(length)



