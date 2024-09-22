# processes that run in parallel
# CPU bound task - task that are heavy on cpu usage ( e.g mathematical computation,Data Processing).

# Parallel execution - Multiple cores of the CPU

import multiprocessing

import multiprocessing.process
import time 

def Square_num():
    for i in range(5):
        time.sleep(2)
        print(f'Sqaure: {i*i}')

def cube():
    for i in range(5):
        time.sleep(2)
        print(f'Cube: {i*i*i}')

if __name__ == "__main__":

    # create 2 processess
    p1 = multiprocessing.Process(target=Square_num)
    p2 = multiprocessing.Process(target=cube)
    t = time.time()

    # calling the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)


'''
use threading for tasks that wait and multiprocessing for tasks that compute!

'''