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
Ex. 2 - Write a python function that accepts a hyphen - separated sequence of words as parameter and return that words in a hyphen -seperated sequence after sorting them alphabetically

'''
def sort_sequence(n):
    '''
    user give the hypen seperated string as a argument and get sorted alphabetically as an output
    '''
    s = sorted(n.split('-'))
    print('-'.join(s))
    
# another method
def sorted_alpha(n):
    temp = []
    for i in sorted(n.split("-")):
        temp.append(i)
    return "-".join(temp)




n = 'shivam-zebra-shahi-kumar-data-scientist'
sort_sequence(n)
print(sorted_alpha(n))

'''
ex - 3
A dict contains following information about 5 employees
1. First name
2. Last name 
3. Age
4. Grade(skilled,semi-skilled,Highly Skilled)
write a program using map/filter/reduce to a list of employees(firstname + lastname) who are highly skilled
'''

employees = [{
            "fName" : 'Shivam',
            "Lname" : 'Kumar',
            "Age"   : 29,
            "Grade" : "Highly Skilled",
    },
    {
            "fName" : 'Rohan',
            "Lname" : 'Mishra',
            "Age"   : 30,
            "Grade" : "Semi Skilled",        

    },
    {
            "fName" : 'Pankaj',
            "Lname" : 'Kumar',
            "Age"   : 35,
            "Grade" : "Skilled",        

    },
    {
            "fName" : 'Gaurav',
            "Lname" : 'Kumar',
            "Age"   : 33,
            "Grade" : "Highly Skilled",        

    },
    {
            "fName" : 'Aditya',
            "Lname" : 'Jha',
            "Age"   : 30,
            "Grade" : "Skilled",        

    }
]

a = list(filter(lambda x :True if x['Grade'] == "Highly Skilled" else False, employees))

print(a)

# for extracting only fname and lastname
b = list(map(lambda x:x["fName"] + " " + x["Lname"],a ))

print(b)


def employee_filter(dict):
    # filter fuction to extract the first condition
    a = list(filter(lambda x: True if x['Grade'] == 'Highly Skilled' else False,dict))

    # map function to extract merged the name of the employee
    b = list(map(lambda x:x["fName"]+ ' ' + x['Lname'], a))

    print(b)


employee_filter(employees)