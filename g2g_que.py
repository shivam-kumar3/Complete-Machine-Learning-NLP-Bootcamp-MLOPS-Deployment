# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).
'''
Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4

'''
arr = []


for i in range(1,7):
    if i % 2 != 0:
        arr.append(i)

print(arr)



output = []

for i in range(1,7):
    if i & 2 == 0:
        output.append(i)
    else:
        continue
print(output)





'''
def convertfive(n):
    n = str(n)
    new = []
    for i in n:
        if i == "0":
            new.append('5')
        else:
            continue
    new = int(new)
    print(new)


convertfive(1100)
'''


a = 'this is the question'

print(a.split())

for i in a.split():
    print(i)

# find the length of a given string without using the len()function

def length(str):
    size = 0
    for i in str:
        size += 1 

    print(size)


length('shivaaaaaaaaaaaa')


# extract username from a given email
#  if the email is shivam@gmail.com then the username should be shivam


def username(email):
    user = ""
    for i in email:
        if i == "@":
            break
        else:
            user += i
    print(user)


username('shivamkumar1957@gmail.com')


# write a program that can check whether a given string is palindrome or not

def checker(str):
    if str == str[::-1]:
        print('String is palindrome')
    else:
        print('String is not palindrom')


checker('shivam')
checker('wow')
checker('malayalam')