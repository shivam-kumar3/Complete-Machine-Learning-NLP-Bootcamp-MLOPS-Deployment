'''
Iterators 

Iterators are advanced python concepts that allow for effiecent looping and mmemory management.
Iterators provide a way to access elements of collection sequentially without exposing the underlying structure
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
