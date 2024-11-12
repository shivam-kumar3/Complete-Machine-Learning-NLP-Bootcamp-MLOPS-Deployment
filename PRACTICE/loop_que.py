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


# reverse a word
# write a program to print the word python in reverse using a for loop

word = 'python'
for i in word[::-1]:
    print(i, end= "")


'''
count vowels in a string 
que - Write a programe to count the number of vowels in the word 'education'

'''

word = 'education'
count = 0 
vowels = 'aeiou'

for i in word:
    if i in vowels:
        count += 1
print(count)




