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




