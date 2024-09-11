'''
Video outline 
1- introduction to tuple
2- creating tuples
3- accessing tuples elements
4- tuples operations
5- immutable nature of tuples
6- tuple methods
7- packing unpacking tuples
8- nested tuples
9- practical examples and common errors



'''
# introduction to tuples
# tuples are ordered collection of items that are immutables

# creating a tuple

empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

num = tuple([1,2,3,4,5,6,7])

print(num)
print(type(num))


mixed_tuple = (12,34,"shivam")

print(mixed_tuple)

# accessing tuples elements

print(num[0])
print(num[2])
print(num[-1])

# slicing

print(num[0:2])
print(num[0:3])
print(num[0:-1])


# tuples operations
# concatinations

new = num +mixed_tuple

print(new)

print(num *3 )

# immutable nature of tuples 
# tuples are immutable meaning their elements cannot be changed once assigned

# the only way we can change the value of tuples is to convert it in list then change it then again change it to tuples

# tuples methods

print(num.count(1))
print(num.index(3))


# packing and unpacking tuples

packed_tuple = "shivam",32,121,"shahi"

print(packed_tuple)
print(type(packed_tuple))

# unpackingg a tuples

a,b,c,d=packed_tuple

print(a)
print(b)
print(c)

# unpacking with *

numbers = (1,2,3,4,5,6)

first,*middle,last = numbers
print(first)
print(middle)
print(last)



# nested list
lst = [[1,2,3,4],[6,7,8,9],[1,"shivam",3.14,"c"]]

print(lst[2][1:4:2])

# nested tuples

tup = ((1,2,3),("a","TOP G","c"),(True,False))

print(tup[1][1])

# iterating over nested tuples

for i in tup:
    for j in i:
        print(j)

        