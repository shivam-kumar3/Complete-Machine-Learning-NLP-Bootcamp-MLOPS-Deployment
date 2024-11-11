# we will solve 10 ques there of easy to hard level

# 1- print number from 1 to 5 

for i in range(1,6):
    print(i, end = " ")

# print sq of numbers from 1 to 5

for i in range(1,6):
    print (i ** 2, end = " ")


# print even numbers from 1 to 10 
for i in range (1,11):
    if i % 2 == 0:
        print(i)


# calculate sum of numbers from 1 to 10

sum = 0 
for i in range (1,11):
    sum += i 
print(sum)