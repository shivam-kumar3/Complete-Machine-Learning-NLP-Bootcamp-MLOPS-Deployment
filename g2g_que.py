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

