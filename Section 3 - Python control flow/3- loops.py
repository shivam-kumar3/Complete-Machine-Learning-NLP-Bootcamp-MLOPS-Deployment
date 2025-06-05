# LOOPS

'''
VIDEO OUTLINE
1- INTRODUCTION TO LOOPS
2- FOR LOOPS
3- WHILE LOOPS
4- LOOP CONTROL STATEMENTS 
5- NESTED LOOPS 
6- PRACTICAL EXAMPLES AND COMMON ERRORS

'''

# FOR LOOPS

for i in range(5):
    print("oochi gang")

name = "Shivam"

for i in name:
    print(i)

# while loops
count = 0 

while count <5:
    print(count)
    count += 1


# loop control statements
# break - break statement exits the loop prematurely

for i in range(6):
    if i == 4:
        break



# continue - continue statements skip the current iteration and continue with the next

for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

#  pass
#  the pass statement is a null operation it does nothing

for i in range(10):
    if i == 3:
        print("The number is , " ,i)
        pass
    print(i)

# nested loops
#  a loop inside a loop 

for i in range(3):
    for j in range(4):
        print(f'i :{i} and j: {j}')

# calculate the sum of first n natural number using a while and for loop

# using while loop
n = 10 
sum = 0
count = 0

while count <= n:
    sum += count
    count += 1
print(sum)

# using for loop

n = 10 
sum = 0

for i in range(11):
    sum += i
print(sum)

# display the prime number between 1 and 100

for i in range(1,101):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)



'''
Write a Python program that prints the sum of all even numbers from 1 to 100 (inclusive), using a loop.
'''
def sumofall(number):
    total = 0
    for i in range(number+1):
        if i % 2 == 0:
            total += i
    print(total)



sumofall(100)
# 




'''



conclusion 
loops are powerul constructs in python that allow you to executes a block of code multiple times .
by understanding and using for and while loops, along with looop control statement like break, continue and pass, we can handle wide range of programming task efficiently 

'''




