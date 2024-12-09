'''
Generator

Generator are a simpler way to create iterators. they use the yeild keyword to produce a series of values laxily, which means they generate values on the fly and do not store them in memory.

'''

def square(n):
    for i in range(10):
        yield i ** 2
    
print(square(3))

for i in square(3):
    print(i)


# Example 1: Infinite Number Generator
def infinite_numbers(start=0):
    """Generates an infinite sequence of numbers starting from 'start'."""
    while True:
        yield start
        start += 1

# Using the generator
gen = infinite_numbers(10)
for _ in range(5):
    print(next(gen))




def fibonacci(n):
    """Generates the first 'n' numbers in the Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num)



