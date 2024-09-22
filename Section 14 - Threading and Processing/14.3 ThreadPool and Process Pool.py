# Multithreading with thread pool executor

'''
ThreadPoolExecutor
What It Is: A way to run multiple tasks at the same time using threads.

Use Case: Good for I/O-bound tasks, like downloading files or making network requests. This is because threads can wait for these tasks to complete without blocking others.

Example: If you're downloading multiple images from the internet, you can use ThreadPoolExecutor to start several downloads at once, speeding up the process.

ProcessPoolExecutor
What It Is: A way to run multiple tasks at the same time using separate processes.

Use Case: Best for CPU-bound tasks, like heavy calculations. 
Each process runs independently, so they can utilize multiple CPU cores.

Example: If you're processing large datasets or performing complex computations, ProcessPoolExecutor can help speed up the work by dividing it across multiple processes.

Quick Summary:

ThreadPoolExecutor: Use for tasks that wait on resources (I/O tasks).

ProcessPoolExecutor: Use for tasks that need heavy computation (CPU tasks).

'''


from concurrent.futures import ThreadPoolExecutor
import time

def print_num(num):
    time.sleep(1)
    return f'Number : {num}'

number = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,8]
t = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_num,number)

for result in results:
    print(result)


final_time = time.time() - t
print(final_time)


# Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def sqaure(num):
    time.sleep(1)
    return f'Sqaure : {num**2}'


number = [1,2,3,4,5]
if __name__ == "__main__":
    t = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sqaure,number)

    for result in results:
        print(result)

    final_time = time.time() - t
    print(final_time)


