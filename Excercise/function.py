'''
Ex. 1
write a python function that takes a list and return a new list with unique elements of the first list

eg. input - [1,2,2,2,3,4,5,5,5,6,6,7]
output - [1,2,3,4,5,6,7]
'''

def unique(lst):
    new = set(lst)
    newlst = list(new)
    print(newlst) 

# another method
def Unique_result(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


lst = [1,2,2,2,3,4,5,5,5,6,6,7]

unique(lst)
print(Unique_result(lst))

'''
Ex. 2 - Write a python function that accepts a hyphen - separated sequence of words as per 

'''