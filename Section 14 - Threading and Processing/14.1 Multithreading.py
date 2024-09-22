# Multithreading 
# When to use Multi Threading 
# 1- i/o bound tasks: tasks that spend more time waiting for i/o operations (e.g. file operations, network requests)

## 2- concurrent execution: when we want to imporve thr throughput of your application by performing multiple operations concurrently.

import threading
import time 

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f'Number: {i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')

# creating 2 threads
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)


t = time.time()
# start the thread
t1.start()
t2.start()

# wait for the threads to complete 
t1.join()
t2.join()

finished_time = time.time() -t
print(finished_time)