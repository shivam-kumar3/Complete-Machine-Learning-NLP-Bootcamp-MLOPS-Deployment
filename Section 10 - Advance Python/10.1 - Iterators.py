'''
Iterators 

Iterators are advanced python concepts that allow for effiecent looping and mmemory management.
Iterators provide a way to access elements of collection sequentially without exposing the underlying structure

we use this for the efficient looping and memory management 
'''

mylist = [1,2,3,4,5,6]

for i in mylist:
    print(i)

print(type(mylist))

# iterator

it = iter(mylist)



# iterate through all the element

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

try:
    for i in it:
        print(next(it))
except StopIteration:
    print("Sorry the list ends here")


names = ['Shivam','shahi','rohan','sohan','mohan']

iterr = iter(names)

print(iterr)
print(next(iterr))

try:
    for i in next(iterr):
        print(next(iterr))
except StopIteration:
    print("The list of name finished")

my_string = 'shivam'

str_iter = iter(my_string)

try:
    while True:
        print(next(str_iter))
except StopIteration:
    print("The string alpha is ended here")


# another approach without try except 
for i in str_iter:
    print(i)
