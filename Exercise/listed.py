sqaure = [i ** 2 for i in range (5)]

print(sqaure)

# Question:
# Write a list comprehension that creates a list of all numbers between 1 and 50 that are divisible by both 3 and 5.
cube = [i**3 for i in range (1,10) if i % 2 != 0]

print(cube)


# Write a list comprehension that creates a list of all numbers between 1 and 50 that are divisible by both 3 and 5.

out = [i for i in range(1,50) if i % 3 == 0 and i % 5 == 0]
print(out)

# Question:
# Write a list comprehension that generates a list of the lengths of each word in the following list:

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

length = [len(i) for i in words]
print(length)

# Write a list comprehension that filters out all vowels from a given string. For example, if the string is "List Comprehension", your list comprehension should return a list of the non-vowel characters.

string = "List Comprehension"
vowels = 'aeiouAEIOU'
join = [i for i in string if i not in vowels]
print(join)

# Write a list comprehension that creates a list of tuples, where each tuple contains a number and its square, for all even numbers between 1 and 20 (inclusive).

tup = [tuple((i,i**2)) for i in range(1,21) if i % 2 == 0]
print(tup)

'''
Question:
Write a list comprehension that generates a list of the first 10 Fibonacci numbers.

The Fibonacci sequence is defined as follows:

The first two numbers are 0 and 1.
Every subsequent number is the sum of the two preceding ones.

'''

def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

# Generate first 10 Fibonacci numbers
fibonacci_numbers = fibonacci(10)
print(fibonacci_numbers)

